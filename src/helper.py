import boto3
import os
import json
import re
import time
import pandas as pd
import streamlit as st
from botocore.exceptions import ClientError
from botocore.config import Config
from dotenv import load_dotenv
from typing import List, Optional, Iterator
from pydantic import BaseModel
from fuzzywuzzy import fuzz
load_dotenv()


DEFAULT_RETURN_VALUE= '{"rows":[]}'
model_id_description = "meta.llama3-1-70b-instruct-v1:0"
model_id = "meta.llama3-1-8b-instruct-v1:0"
#model_id = "meta.llama3-2-1b-instruct-v1:0"
#model_id="mistral.mistral-7b-instruct-v0:2"
config = Config(
    read_timeout=20,
    connect_timeout=20,
    retries={"max_attempts": 0}
)
client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-west-2",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    config=config
)

with open("./src/weblinks.json", "r") as file:
    articles = json.load(file)
list_topics=[articles[0][k].keys() for k in articles[0].keys()]
list_topics = list(list_topics[0])+list(list_topics[1])

class Row(BaseModel):
    no: int
    topic: str
    count: int
    description: str
    status: str

class Table(BaseModel):
    rows: List[Row]

class PreProcess:
    def is_csv(file_path: str) -> bool:
        return file_path.endswith(".csv") 

    def is_txt(file_path: str) -> bool:
        return file_path.endswith(".txt")
    
    def df_to_string(df: pd.DataFrame) -> str:
        result = []
        for _, row in df.iterrows():
            row_strings = []
            for col, val in row.items():
                if col == df.columns[-1]:
                    row_strings.append(f"{val}")
                else:
                    row_strings.append(f"{col}: {val}")
            result.append("\n".join(row_strings))
        return "\n\n\n".join(result)


    def split_text_file(file_contents: str, min_equals: int = 3) -> List[str]:
        """
        Read a text file and split it into chunks based on separator lines containing equals signs.
        
        Args:
            file_path (str): Path to the text file
            min_equals (int): Minimum number of consecutive equals signs to consider as separator
                            Default is 3 (i.e., "===")
        
        Returns:
            List[str]: List of text chunks with whitespace trimmed
        
        Raises:
            FileNotFoundError: If the specified file doesn't exist
            ValueError: If min_equals is less than 1
        """
        if min_equals < 1:
            raise ValueError("min_equals must be at least 1")
        
        # Create regex pattern for one or more equals signs
        separator_pattern = f"^_{{{min_equals},}}$"
        
        try:
            # Read the entire file content
            content = file_contents
            
            # Split the content using regex
            # This will match lines that contain only equals signs (minimum count specified)
            chunks = re.split(separator_pattern, content, flags=re.MULTILINE)
            
            # Clean up the chunks: remove empty strings and strip whitespace
            cleaned_chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
            
            return cleaned_chunks
        
        except Exception as e:
            raise Exception(f"Error processing file: {str(e)}")


    def clump_strings_generator(strings: List[str], chunk_size: int) -> Iterator[str]:
        """
        Generator version that yields clumped strings one at a time.
        """
        for i in range(0, len(strings), chunk_size):
            yield '\n\n\n'.join(strings[i:i + chunk_size])
        
    def remove_before_pm(text, escape_char='PM)'):
        s = ""
        for line in text.split('\n'):
            if escape_char in line:
                s+= line.split(escape_char)[1]+ '\n'
        return s            

    def compress_text_chunks(chunks: List[str], escape_char='PM)') -> List[str]:
        for i, chunk in enumerate(chunks):
            chunks[i] = PreProcess.remove_before_pm(chunk, escape_char)
        return chunks

    def process_text_chunks(file_contents: str, chunk_size: int) -> List[str]:
        split = PreProcess.split_text_file(file_contents=file_contents)
        PreProcess.split = split
        #split = PreProcess.compress_text_chunks(split, escape_char='PM)')
        clumps = PreProcess.clump_strings_generator(strings=split, chunk_size=chunk_size)
        return clumps

    def extract_json_block(text: str) -> Optional[str]:
        if "```" not in text:
            json_string = text.strip()
        elif "```" in text and "json" not in text:
            pattern = r'```\s*([\s\S]*?)\s*```'
            match = re.search(pattern, text, re.DOTALL)
            if match:
                json_string=match.group(1).strip()
        elif "```json" in text:
            pattern = r'```json\s*([\s\S]*?)\s*```'
            match = re.search(pattern, text, re.DOTALL)
            if match:
                json_string=match.group(1).strip()
        else:
            print("No json block found, skipping: ", text)
            return DEFAULT_RETURN_VALUE
        #print("teXT", text)

        if json_string[1] == "'":
            json_string_adjusted=json_string.replace('"', 'TEMP').replace("'", '"').replace('TEMP', "'")
        else:
            json_string_adjusted=json_string

        return json_string_adjusted


class Display:
    def text_clumps(clumps: List[str]):
        for i, clump in enumerate(clumps, 1):
            print(f"Clump {i}:\n{clump}\n")

    def dict_to_df(table: dict):
        rows = table['rows']
        df = pd.DataFrame(rows)
        return df

class Execute:
    def get_table(conversations: str, existing_table:Table)-> Table:
        system_prompt = """
                            You are an expert customer support analyst with extensive experience in the Knowledge Centered Service framework.
                            The framework is designed to generate help articles based on conversations that occur at a contact center.
                        """

        user_prompt = f"""
                **TASK**
                    - Go through all conversations in the attached file and create a list of the top issues mentioned in the conversations.  The list of issues should be in a format that will help the team create FAQ and help articles for each issue.  
                    - For each topic/issue also provide the count of conversations that relate to the specific topic and present it in a tabular format
                    - For each topic/issue also provide a summary of the conversations that relate to the topic.
                    - For each topic/issue also check if an article already exists in the current knowledge center.  

                Ensure you thoroughly check every conversation.

                **INSTRUCTIONS**

                1. Carefully read every conversation.

                2. Identify the topic of that conversation. 
                
                3. If there are multiple topics in a conversation, ensure to list all of them seperately.

                4. Add this to the list of topics. 

                5. Repeat steps 2. and 3. for every conversation in the document.

                6. If the topic is already in the table then simply add 1 to the count for that topic in the table.

                7. For each topic provide a DETAILED DESCRIPTION, the COUNT OF CONVERSATIONS, and the TOPIC of each conversation that prompted this issue in a table with 4 columns.  The detailed description would include the date/time stamp and specific question asked by the contact.  Put each time stamp description on a new line in the column so it is easy to read.

                8. For each topic, check whether an article in the knowledge center has already been created.  If an exact match is not found then look for a close match to the topic. Provide the name of the article that exists in the knowledge base and if there is no match then enter "no article found"  Here is a list of all articles in the knowledge base:  

                9. Make a final output table which contains all the unique topics along with the count of conversations for each topic, a brief description of each conversation related to the topic, and the article name found in the knowledge base (or "No Article Found" if none was found).

                10. Thoroughly check all conversations once more to ensure the topics have been identified accurately and that there are no duplicates. Here is the current status of the table: {existing_table}

                **EXAMPLES**

                Here is the columns of the table: 

                No: (Unique number for each topic)
                Topic: (Primary topic of the conversation)
                Count: (Number of conversations related to this topic)
                Description:(Description of the customer issue along with the date, time and transcripts of the conversation)
                Status:(No Article Found )

                **USER REPITITION**

                To confirm, go through every conversation and identify the primary topic for the conversation.  Then create a table of the list of unique topics, the count of conversations that relate to this topic, a brief description of each conversation related to the topic, and a link to the knowledge base article if one is found - or the words "No Article Found" if one does not exist. Do not skip any conversations and do not duplicate any topics in the list.

                **OUTPUT STRUCTURE**

                Provide an output in a table format that lists the unique topics, the count of conversations related to that topic, and a brief description of each conversation. 

                **GUARDRAILS**

                Do not add any topics that are not part of the conversations and do not try to interpret topics that are not clear.  For any unclear topics, list them as "unclear" and provide a count of those conversations.  Then provide a summary of those conversations below the table.

                Respond in a json format of the table in this schema: {existing_table} nestled between ```json and ``` to ensure the output is formatted correctly, using double quotes as json delimiters.

                **ATTACHED CONVERSATION FILE**
                {conversations}
                        """

        formatted_prompt = f"""
        <|begin_of_text|>
        <|start_header_id|>system<|end_header_id|>
        {system_prompt}
        <|start_header_id|>user<|end_header_id|>
        {user_prompt}
        <|eot_id|>
        <|start_header_id|>assistant<|end_header_id|>
        """
            
        native_request = {
        "prompt": formatted_prompt,
        "max_gen_len": 8192,
        "temperature": 0.0,
        }
        request = json.dumps(native_request)

        try:
            # Invoke the model with the request.
            response = client.invoke_model(
            modelId=model_id,
            body=request,
            contentType="application/json"
            )

            # Decode the response body.
            model_response = json.loads(response["body"].read())
            response_text = model_response["generation"]
            return response_text

        except (ClientError, Exception) as e:
            print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
            return DEFAULT_RETURN_VALUE

class CombineTables:
    def __init__(self, chunk_size:int, file_contents:str):
        self.table_format = {"rows":[{"no": None, "topic": None, "count": None, "description": None, "status": None}]}
        self.combined_table= {"rows":[]}
        try:
            self.clumps = PreProcess.process_text_chunks(file_contents=file_contents, chunk_size=chunk_size)
            st.session_state["clumps"] = self.clumps
            self.total_clumps = PreProcess.split
        except Exception as e:
            print(f"Error: {str(e)}")
            exit(1)

    def similarity(self, s1, s2):
        if not(s1==s2==None):
            s1 = s1.lower()
            s2 = s2.lower()
            if "issue" in s1 and "issue" in s2:
                s1 = s1.replace("issue", "")
                s2 = s2.replace("issue", "")
            sim = fuzz.ratio(s1, s2)
            if sim >= 80:
                return True
            else:
                return False
        else:
            return False
        
    def is_article_found(self, s1:str, s2:str):
        if not(s1==s2==None):
            s1 = s1.lower()
            s2 = s2.lower()
            if "issue" in s1 and "issue" in s2:
                s1 = s1.replace("issue", "")
                s2 = s2.replace("issue", "")
            sim = fuzz.ratio(s1, s2)
            if sim >= 50:
                return True
            else:
                return False
        else:
            return False
        
    def get_subtable(self, clump: str):
        table_new_string = Execute.get_table(conversations=clump, existing_table=self.table_format)
        table_new = PreProcess.extract_json_block(table_new_string)
        try :
            table_new = json.loads(table_new)
            return table_new
        except json.JSONDecodeError as e:
            print(f"Error: {str(e)}")
            return self.table_format
    
    def get_status(self, topic:str):
        for topic_web in list_topics:
            if self.is_article_found(topic, topic_web):
                return "Article Found"
        return "No Article Found"

    def combine_tables(self, table_new:dict):
        for new_row in table_new["rows"]:
            existing_row = next((row for row in self.combined_table["rows"] if (self.similarity(row["topic"],new_row["topic"]))), None) 
            if existing_row:
                existing_row["count"] += 1
                existing_row["description"] += f'\n #({existing_row["count"]}) {new_row["description"]}'
                existing_row["status"] =self.get_status(existing_row["topic"])
            else:
                current_table_length = len(self.combined_table["rows"])
                new_row["no"] = current_table_length + 1
                new_row["status"] = self.get_status(new_row["topic"])
                self.combined_table["rows"].append(new_row)

def generate_article(description, topic):
        system_prompt = """
                            You are an expert customer support analyst with extensive experience in the Knowledge Centered Service framework.
                            The framework is designed to generate help articles based on conversations that occur at a contact center.
                        """

        user_prompt = f"""
                **TASK**
                    You are provided a issue:{topic} and a detailed description of the conversations containing the solution to the issue:{description}
                    - Create a help article that can be used to address the issue.  The article should ONLY CONTAIN information from: {description}.
                    DO NOT MAKE UP ANY INFORMATION
                    """

        formatted_prompt = f"""
        <|begin_of_text|>
        <|start_header_id|>system<|end_header_id|>
        {system_prompt}
        <|start_header_id|>user<|end_header_id|>
        {user_prompt}
        <|eot_id|>
        <|start_header_id|>assistant<|end_header_id|>
        """
            
        native_request = {
        "prompt": formatted_prompt,
        "max_gen_len": 8192,
        "temperature": 0.0,
        }
        request = json.dumps(native_request)

        try:
            # Invoke the model with the request.
            response = client.invoke_model(
            modelId=model_id_description,
            body=request,
            contentType="application/json"
            )

            # Decode the response body.
            model_response = json.loads(response["body"].read())
            response_text = model_response["generation"]
            return response_text

        except (ClientError, Exception) as e:
            print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
            return "Error generating article"
'''
if __name__ == "__main__":
    start = time.time()
    with open("./docs/test100redacted.txt", "r") as file:
        file_contents = file.read()
    runner = CombineTables(chunk_size=3, file_contents=file_contents)
    for (idx,clump) in enumerate(runner.clumps):
        print(f"clump #{idx}")
        table_new=runner.get_subtable(clump)
        #print(f"new table #{idx}:{json.dumps(table_new, indent=2)}")
        runner.combine_tables(table_new)
    end = time.time()
    print(f"Time taken: {end-start}")

'''