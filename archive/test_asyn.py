import os
import boto3
import json
from dotenv import load_dotenv
load_dotenv()
 
#Create the connection to Bedrock
bedrock = boto3.client(
  service_name='bedrock',
  region_name='us-west-2',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

bedrock_runtime = boto3.client(
  service_name='bedrock-runtime',
  region_name='us-west-2',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)


 
# Define prompt and model parameters
prompt_data = """Write me a poem about apples"""
 
body = json.dumps({
    "inputText": prompt_data,
})
 
model_id = 'amazon.titan-embed-text-v1' #look for embeddings in the modelID
accept = 'application/json' 
content_type = 'application/json'
 
# Invoke model 
response = bedrock_runtime.invoke_model(
    body=body, 
    modelId=model_id, 
    accept=accept, 
    contentType=content_type
)
 
# Print response
response_body = json.loads(response['body'].read())
embedding = response_body.get('embedding')
 
#Print the Embedding
 
print(embedding)