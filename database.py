import sqlite3
import os
import time
from dotenv import load_dotenv

class Memory():
    def __init__(self):
        load_dotenv()

        self.root_directory = os.path.abspath(os.path.dirname(__file__))
        self.db_path = os.path.join(self.root_directory, "Databases", "memory.db")
        self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS memory (
                time TEXT,
                interaction TEXT
            )
        """)
        self.connection.commit()

    def read_from_memory(self):
        try:
            self.time_limit_days = int(os.getenv('TIME_LIMIT_DAYS', '7'))
            self.time_limit_epoch = int(time.time()) - (self.time_limit_days * 86400)

            self.cursor.execute("SELECT interaction FROM memory WHERE time > ?", (self.time_limit_epoch,))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error reading from memory: {e}")
            return []



    def write_to_memory(self, user_input, response):
        self.current_time = int(time.time())
        self.cursor.execute("INSERT INTO memory (time, interaction) VALUES (?, ?)",
                            (self.current_time, f'{user_input} --- {response}'))
        self.connection.commit()

    def close(self):
        self.connection.close()