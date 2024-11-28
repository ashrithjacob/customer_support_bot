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
from pydantic import basemodel

import logging




class Pipeline:
    class Valves(BaseModel):
            target_user_roles: List[str] = ["user"]
            max_turns: Optional[int] = None

    def __init__(self):
        self.name = "pipeline_custom_name"
        self.valves = self._initialize_valves()
        self.file_contents = {}

    def _initialize_valves(self) -> Valves:
        """Initialize valves using environment variables."""
        return self.Valves()

    async def on_startup(self):
        """Called when the server is started."""
        pass

    async def on_shutdown(self):
        """Called when the server is stopped."""
        pass

    async def on_valves_updated(self):
        """Called when the valves are updated."""
        pass

    async def inlet(self, body: dict, user: dict) -> dict:
        """Modifies form data before the OpenAI API request."""

        # Extract file info for all files in the body
        # here i have created an inmemory dictionary to link users to their owned files
        file_info = self._extract_file_info(body)
        self.file_contents[user["id"]] = file_info
        return body

    def _extract_file_info(self, body: dict) -> list:
        """Extracts the file info from the request body for all files."""
        files = []
        for file_data in body.get("files", []):
            file = file_data["file"]
            file_id = file["id"]
            filename = file["filename"]
            file_content = file["data"]["content"]

            # Create a OIFile object and append it to the list
            files.append(file_content)

        return files

    def pipe(
        self, body: dict, user_message: str, model_id: str, messages: List[dict]
    ) -> Union[str, Generator, Iterator]:


        # Extract parameters from body with default fallbacks
        stream = body.get("stream", True)
        max_tokens = body.get("max_tokens", self.valves.LLM_MAX_TOKENS)
        temperature = body.get("temperature", self.valves.LLM_TEMPERATURE)

        # Extract user ID from the body
        user = body.get("user", {})
        user_id = user.get("id", "")

        # Extract user files if available
        if user_id in self.file_contents:
            user_files = self.file_contents[user_id]
        else:
            user_files = None
        return user_files

    async def outlet(self, body: dict, user: Optional[dict] = None) -> dict:
        print(f"outlet:{__name__}")
        print(f"Received body: {body}")

        if user["id"] in self.file_contents:
            del self.file_contents[user["id"]]

        return body
