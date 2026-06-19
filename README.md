# LLM Text Chunking

This project demonstrates preprocessing and chunking of public unstructured text for LLM prompt preparation.

## Features

- Downloads a public text document from Project Gutenberg
- Cleans the text by removing extra whitespace and special characters
- Splits text into sentences
- Creates contextually coherent chunks of approximately 250 words
- Displays original text length
- Displays number of chunks generated
- Displays the first three chunks as examples

## Technologies Used

- Python
- Requests
- Regular Expressions (re)

## Output

The script prints:
1. Original text length
2. Cleaned text length
3. Number of chunks generated
4. First three text chunks
