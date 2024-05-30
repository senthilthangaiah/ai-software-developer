# AI Software Developer

This project is an AI-powered tool that processes program files (Python, C, C++, etc.), extracts business logic using OpenAI's GPT model, generates embeddings using the `sentence-transformers/all-MiniLM-L6-v2` model, and stores the extracted information in an SQLite database. Additionally, it includes a Streamlit app to perform semantic searches and get suggestions for implementing business logic changes in programs.

## Features

- Read and process various program files to extract business logic.
- Generate embeddings using `sentence-transformers/all-MiniLM-L6-v2` model.
- Store program name, content, business logic, and embeddings in an SQLite database.
- Streamlit app to:
  - Accept input business logic.
  - Perform semantic searches on stored programs.
  - Get suggestions from OpenAI for implementing the business logic in matched programs.

## Installation

### Requirements

- Python 3.7+
- OpenAI API key

### Setup

# 1. Clone the repository:

```sh
git clone https://github.com/your-username/ai-software-developer.git
cd ai-software-developer
```

# 2. Install the required packages:
```sh
pip install -r requirements.txt
```
# 3. Set up your OpenAI API key:

Replace "your-openai-api-key" in the scripts with your actual OpenAI API key.

## Running the Application

## Extracting and Storing Business Logic:

Run the script to read a program file, extract business logic, generate embeddings, and store the data in the SQLite database.

```sh
Copy code
python extract_store_logic.py
``` 

### Streamlit App:

Launch the Streamlit app to perform semantic searches and get suggestions for business logic implementation.

```sh
streamlit run app.py
```

## File Structure
   extract_store_logic.py: Script to read program files, extract business logic, generate embeddings, and store data in the database.
   app.py: Streamlit app for semantic search and business logic suggestions.
   requirements.txt: List of dependencies required for the project.
   programs.db: SQLite database storing the program data (created when running the script).

## Usage
Extract and Store Business Logic
Update file_path in extract_store_logic.py to the path of your program file.

Enter the business logic in the text area and click "Process" to find matching programs and get suggestions for implementing the business logic.
### Results.

# Changes Required
![screenshot](https://github.com/senthilthangaiah/ai-software-developer/blob/8d4d6aaada2470c7de5bbd97ac1527e8071262bf/image/aicoder1.png)

# Existing Logic & Code
![screenshot](https://github.com/senthilthangaiah/ai-software-developer/blob/8d4d6aaada2470c7de5bbd97ac1527e8071262bf/image/aicoder2.png)

# Proposed Logic & Code
![screenshot](https://github.com/senthilthangaiah/ai-software-developer/blob/8d4d6aaada2470c7de5bbd97ac1527e8071262bf/image/aicoder3.png)


## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements
OpenAI for the GPT-3.5 model.
Sentence Transformers for the all-MiniLM-L6-v2 model.
Streamlit for the web app framework.
