import streamlit as st
import openai
import sqlite3
import torch
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize the SentenceTransformer model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# OpenAI API key setup
openai.api_key = "12121212XXXXXXXXXXXX"

# Function to get embeddings from SentenceTransformer model
def get_embeddings(text):
    return model.encode(text).tolist()

# Function to retrieve data from SQLite database
def retrieve_data():
    conn = sqlite3.connect('programs.db')
    cursor = conn.cursor()
    cursor.execute('SELECT program_name, program_content, business_logic, embedding FROM programs')
    data = cursor.fetchall()
    conn.close()
    return data

# Function to perform semantic search
def semantic_search(input_embedding, data):
    embeddings = [np.frombuffer(row[3], dtype=np.float32) for row in data]
    similarities = cosine_similarity([input_embedding], embeddings)
    max_index = np.argmax(similarities)
    return data[max_index]

# Function to get suggestions from OpenAI
def get_openai_suggestions(program_content, input_logic):
    inp1=f"Given the program:\n{program_content}\n\nand the business logic:\n{input_logic}\n\nSuggest changes to the program to implement the business logic.",
    response = openai.Completion.create(
           engine="gpt-35-instruct",
           prompt=inp1,
           temperature=1,
           max_tokens=2000,
           top_p=0.8,
           frequency_penalty=0, 
           presence_penalty=0,
           best_of=1,   
           stop=None
    )
    return response.choices[0].text.strip()

# Streamlit app
st.title("Business Logic Processor")

# Input text for business logic
input_logic = st.text_area("Enter the business logic:")

if st.button("Process"):
    if input_logic:
        # Generate embeddings for the input logic
        input_embedding = get_embeddings(input_logic)
        
        # Retrieve data from database
        data = retrieve_data()
        
        if data:
            # Perform semantic search
            matched_program = semantic_search(input_embedding, data)
            
            if matched_program:
                program_name, program_content, business_logic, _ = matched_program
                st.write(f"Matched Program: {program_name}")
                st.write(f"Program Content:\n{program_content}")
                st.write(f"Existing Business Logic:\n{business_logic}")
                
                # Get suggestions from OpenAI
                suggestions = get_openai_suggestions(program_content, input_logic)
                st.write("Suggested Changes to Implement the Business Logic:")
                st.write(suggestions)
            else:
                st.write("No matching program found.")
        else:
            st.write("No data available in the database.")
    else:
        st.write("Please enter the business logic.")


