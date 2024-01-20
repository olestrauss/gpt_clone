from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()

class Responder():
    def __init__(self):
        self.client = OpenAI()
        self.time_limit = os.getenv('TIME_LIMIT_DAYS')
    
    def get_completion(self, prompt, memory=''):
        completion = self.client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'system', 'content': 'You are a fork of GPT. If asked who you are, say "I am a fork of GPT made by Ole S."'},
                {'role': 'assistant', 'content': memory},
                {'role': 'user', 'content': prompt}
                
            ]
        )
        return completion.choices[0].message.content
