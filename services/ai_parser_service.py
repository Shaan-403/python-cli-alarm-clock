from openai import OpenAI
from dotenv import load_dotenv
import json
load_dotenv()

client = OpenAI()
class AIParserService:

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

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return json.loads(
            response.choices[0]
            .message.content
        )