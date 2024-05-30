import os
import openai
import sqlite3
import torch
from sentence_transformers import SentenceTransformer

# Initialize the SentenceTransformer model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# OpenAI API key setup
openai.api_key = "asdd222112111asfadsvdsdfd"

# Function to read the program file
def read_program_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to get business logic from OpenAI

def get_business_logic(program_content):
    input1=f"Extract the business logic from the following code:\n\n{program_content}",
    response = openai.Completion.create(
           engine="gpt-35-instruct",
           prompt=input1,
           temperature=1,
           max_tokens=2000,
           top_p=0.8,
           frequency_penalty=0, 
           presence_penalty=0,
           best_of=1,   
           stop=None
    )
    return response.choices[0].text.strip()

# Function to get embeddings from SentenceTransformer model
def get_embeddings(business_logic):
    return model.encode(business_logic).tolist()

# Function to store data in SQLite database
def store_in_db(program_name, program_content, business_logic, embedding):
    conn = sqlite3.connect('programs.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS programs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            program_name TEXT,
            program_content TEXT,
            business_logic TEXT,
            embedding BLOB
        )
    ''')
    cursor.execute('''
        INSERT INTO programs (program_name, program_content, business_logic, embedding)
        VALUES (?, ?, ?, ?)
    ''', (program_name, program_content, business_logic, sqlite3.Binary(torch.tensor(embedding).numpy().tobytes())))
    conn.commit()
    conn.close()

# Main function
def main():
    file_path = 'app1.py'  # Change this to the path of your program file
    program_name = os.path.basename(file_path)
    program_content = read_program_file(file_path)
    business_logic = get_business_logic(program_content)
    print('Business Logic ', business_logic)
    embedding = get_embeddings(business_logic)
    print(' embedding ', embedding )
    store_in_db(program_name, program_content, business_logic, embedding)

if __name__ == "__main__":
    main()

