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
import boto3
import os
import json
import re
import pandas as pd
from dotenv import load_dotenv
from typing import List, Optional, Iterator
from pydantic import BaseModel
load_dotenv()


model_id = "meta.llama3-1-70b-instruct-v1:0"

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
        self.documents = None
        self.index = None
        self.user_inputs = []

    def get_filename(self, body: List[dict]) -> str:
        return body[0]["files"][0]["file"]["name"]
    
    def get_contents(self, body: List[dict]) -> str:
        return body[0]["files"][0]["file"]["data"]["content"]
   
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
        table = d.get_message(self.user_inputs)
        return table
