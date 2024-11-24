"""
title: Llama Index Pipeline
author: open-webui
date: 2024-05-30
version: 1.0
license: MIT
description: A pipeline for retrieving relevant information from a knowledge base using the Llama Index library.
requirements: llama-index
"""

from typing import List, Union, Generator, Iterator, Optional
from schemas import OpenAIChatMessage


class SorceParser:
    def __init__(self):
        pass

    def get_message(self, body: dict) -> str:
        # get's the last possible document sent
        return body["messages"][-2]["content"]

    def get_document(self, content: str) -> str:
        # get's all the documents sent
        document_content = content.split("<context>")[-1].split("</context>")[0]
        return document_content


class Pipeline:
    def __init__(self):
        self.documents = None
        self.index = None

    async def on_startup(self):
        # This function is called when the server is started.
        pass

    async def on_shutdown(self):
        # This function is called when the server is stopped.
        pass

    async def inlet(self, body: dict, user: Optional[dict] = None) -> dict:
        """Modifies form data before the OpenAI API request."""
        print(f"Received body: {body}")
        return body

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
    ) -> Union[str, Generator, Iterator]:
        # This is where you can add your custom RAG pipeline.
        # Typically, you would retrieve relevant information from your knowledge base and synthesize it to generate a response.

        print(messages)
        print(user_message)

        return str(body)
