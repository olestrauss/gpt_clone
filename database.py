import sqlite3
import os
from datetime import datetime, timedelta
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
            # Get time limit from environment variable or default to 7
            time_limit_days = os.getenv('TIME_LIMIT_DAYS', '7')
            
            # Calculate the date for the time limit
            time_limit_date = datetime.now() - timedelta(days=int(time_limit_days))
            
            # Convert the date to yyyy-mm-dd format for comparison
            time_limit_str = time_limit_date.strftime('%Y-%m-%d')

            # Adjust the SQL query to compare dates in yyyy-mm-dd format
            query = """
            SELECT interaction FROM memory 
            WHERE strftime('%Y-%m-%d', datetime(substr(time, 7, 4) || '-' || 
            substr(time, 4, 2) || '-' || substr(time, 1, 2))) > ?
            """
            self.cursor.execute(query, (time_limit_str,))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error reading from memory: {e}")
            return []


    def write_to_memory(self, user_input, response):
        current_time = datetime.now().strftime("%d/%m/%Y")
        self.cursor.execute("INSERT INTO memory (time, interaction) VALUES (?, ?)",
                            (current_time, f'{user_input} --- {response}'))
        self.connection.commit()

    def close(self):
        self.connection.close()
