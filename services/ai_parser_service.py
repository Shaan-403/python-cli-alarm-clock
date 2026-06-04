import os
import json

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class AIParserService:

    def __init__(self):

        api_key = os.getenv(
            "OPENAI_API_KEY"
        )

        if not api_key:
            raise Exception(
                "\nAI functionality is not configured.\n"
                "Please configure OPENAI_API_KEY "
                "or use the standard "
                "'add' command.\n"
            )

        self.client = OpenAI(
            api_key=api_key
        )

    def parse(self, text):

        prompt = f"""
Extract an alarm from this text.

Return JSON only.

Format:

{{
    "time": "HH:MM",
    "label": "string"
}}

Input:
{text}
"""

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return json.loads(
            response
            .choices[0]
            .message
            .content
        )