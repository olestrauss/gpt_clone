from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()

class Responder():
    def __init__(self):
        self.client = OpenAI()
    
    def get_completion(self, prompt):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a fork of GPT called 'Ole's GPT Clone. Please respond with: \
                 'I am a fork of GPT called 'Ole's GPT Clone', followed by your generated response."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion
