"""
title: Llama Index Pipeline
author: open-webui
date: 2024-05-30
version: 1.0
license: MIT
description: A pipeline for retrieving relevant information from a knowledge base using the Llama Index library.
requirements: llama-index
"""
import os
from typing import List, Union, Generator, Iterator, Optional
from schemas import OpenAIChatMessage
import boto3
import os
import json
import re
import pandas as pd
from botocore.exceptions import ClientError
from dotenv import load_dotenv
from typing import List, Optional, Iterator
from pydantic import BaseModel
from fuzzywuzzy import fuzz
load_dotenv()


client = boto3.client(
    "bedrock-runtime",
    region_name="us-west-2",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
)

model_id = "meta.llama3-1-70b-instruct-v1:0"

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
        separator_pattern = f"^={{{min_equals},}}$"
        
        try:
            # Read the entire file content
            content = file_contents
            
            # Split the content using regex
            # This will match lines that contain only equals signs (minimum count specified)
            chunks = re.split(separator_pattern, content, flags=re.MULTILINE)
            
            # Clean up the chunks: remove empty strings and strip whitespace
            cleaned_chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
            
            return cleaned_chunks
        
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise Exception(f"Error processing file: {str(e)}")


    def clump_strings_generator(strings: List[str], chunk_size: int) -> Iterator[str]:
        """
        Generator version that yields clumped strings one at a time.
        """
        for i in range(0, len(strings), chunk_size):
            yield '\n\n\n'.join(strings[i:i + chunk_size])

    def process_text_chunks(file_contents: str, chunk_size: int) -> List[str]:
        split = PreProcess.split_text_file(file_contents=file_contents)
        clumps = PreProcess.clump_strings_generator(strings=split, chunk_size=chunk_size)
        return clumps

    def extract_json_block(text: str) -> Optional[str]:
        if "```json" not in text:
            json_string = text.strip()
        else:
            pattern = r'```json\s*([\s\S]*?)\s*```'
            match = re.search(pattern, text, re.DOTALL)
            if match:
                json_string=match.group(1).strip()

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

                Here is an example of one issue with count and descriptions of the conversations that relate to the issue: 

                Column 1: No: 1

                Column 2: Topic: 20 Day to Close Automation Issues	

                Column 3: Count: 2	

                Column 4: Description: 

                (1) Timestamp: 2024-06-13T16:01:19Z > Visitor said "Visitor 8941852: my 20 day to close automation is not working" 

                (2) Timestamp: 2024-06-10T20:35:28Z > Visitor said "We are experiencing an issue with our text automations not going out. not sending text messages or follow-ups.".  NOTE: Put each timestamp description on a new line in that column so it is easy to read.

                Column 5: No Article Found

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
        "max_gen_len": 2048,
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

class CombineTables:
    def __init__(self, chunk_size:int, file_contents:str):
        self.table_format = {"rows":[{"no": None, "topic": None, "count": None, "description": None, "status": None}]}
        self.combined_table= {"rows":[]}
        try:
            self.clumps = PreProcess.process_text_chunks(file_contents=file_contents, chunk_size=chunk_size)
        except Exception as e:
            print(f"Error: {str(e)}")
            exit(1)

    def similarity(self, s1, s2):
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

    def get_subtable(self, clump: str):
        table_new_string = Execute.get_table(conversations=clump, existing_table=self.table_format)
        table_new = PreProcess.extract_json_block(table_new_string)
        table_new = json.loads(table_new)
        return table_new

    def combine_tables(self, table_new:dict):
        for new_row in table_new["rows"]:
            existing_row = next((row for row in self.combined_table["rows"] if (self.similarity(row["topic"],new_row["topic"]))), None) 
            if existing_row:
                print(f'sim between {existing_row["topic"]} and {new_row["topic"]}: {self.similarity(existing_row["topic"],new_row["topic"])}')
                existing_row["count"] += 1
                existing_row["description"] += f'\n #({existing_row["count"]}) {new_row["description"]}'
            else:
                current_table_length = len(self.combined_table["rows"])
                new_row["no"] = current_table_length + 1
                self.combined_table["rows"].append(new_row)


class DocParser:
    def __init__(self):
        pass

    def get_message(self, body: List[dict]) -> str:
        # get's the last possible document sent
        return body[0]["files"][0]["file"]["data"]["content"]


    def get_document_name(self, body: dict) -> str:
        # get's all the documents sent
        content = self.get_message(body)
        document_content = content.split("<context>")[-1].split("</context>")[0]
        document_name = document_content.split("</source_id>")[0].split("<source_id>")[-1]
        return document_name
    
    def get_local_document(self, name:str) -> str:
        full_path_to_dir = os.path.join(os.getenv("WEBUI_DIR"),"uploads")
        for file in os.listdir(full_path_to_dir):
            if file.endswith(name):
                with open(os.path.join(full_path_to_dir, file), "r") as f:
                    return f.read()
        
    def run(self, body: dict) -> str:
        doc_name = self.get_document_name(body)
        doc_content = self.get_local_document(doc_name)
        return doc_content


class Pipeline:
    def __init__(self):
        self.name = "Categorizing Agent"
        self.documents = None
        self.index = None
        self.user_inputs = []

    async def on_startup(self):
        # This function is called when the server is started.
        pass

    async def on_shutdown(self):
        # This function is called when the server is stopped.
        pass

    async def inlet(self, body: dict, user: Optional[dict] = None) -> dict:
        """Modifies form data before the OpenAI API request."""
        print("INLET")
        self.user_inputs.append(body)
        return body

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
    ) -> Union[str, Generator, Iterator]:
        # This is where you can add your custom RAG pipeline.
        # Typically, you would retrieve relevant information from your knowledge base and synthesize it to generate a response.
        print("PIPE")
        d = DocParser()
        file_content= d.get_message(self.user_inputs)
        return file_content
