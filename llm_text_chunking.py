import re
import requests

URL = "https://www.gutenberg.org/files/11/11-0.txt"
TARGET_WORDS = 250

def download_text(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^A-Za-z0-9.,!?;:'\"() -]", "", text)
    return text.strip()

def split_into_sentences(text):
    return re.split(r'(?<=[.!?])\s+', text)

def create_chunks(sentences, target_words=250):
    chunks = []
    current_chunk = []
    current_count = 0

    for sentence in sentences:
        word_count = len(sentence.split())

        if current_count + word_count > target_words and current_chunk:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_count = 0

        current_chunk.append(sentence)
        current_count += word_count

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

raw_text = download_text(URL)
cleaned_text = clean_text(raw_text)
sentences = split_into_sentences(cleaned_text)
chunks = create_chunks(sentences, TARGET_WORDS)

print("Original text length:", len(raw_text))
print("Cleaned text length:", len(cleaned_text))
print("Number of chunks generated:", len(chunks))

print("\nFirst 3 chunks:")
for i, chunk in enumerate(chunks[:3], start=1):
    print(f"\n--- Chunk {i} ---")
    print(chunk[:1000])
