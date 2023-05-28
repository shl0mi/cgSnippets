import os
import re
import requests
import concurrent.futures
from ratelimiter import RateLimiter
from tenacity import retry, stop_after_attempt, wait_fixed
import logging
import tempfile
import jieba

MAX_CHUNK_SIZE = 5000  # Maximum number of tokens per API call

@retry(stop=stop_after_attempt(3), wait=wait_fixed(5))
def translate_chunk(chunk):
    # ...
    # Perform your API request here
    # ...

def split_into_sentences(text):
    start = 0
    sentences = []
    for match in re.finditer("。|！|？", text):
        end = match.end()
        sentence = text[start:end]
        sentences.append(sentence)
        start = end
    if start < len(text):
        sentences.append(text[start:])
    return sentences

def split_into_chunks(filename):
    with open(filename, 'r') as file:
        text = file.read()
    sentences = split_into_sentences(text)
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 > MAX_CHUNK_SIZE:
            if current_chunk:  # Only add non-empty chunks
                chunks.append(current_chunk)
            current_chunk = sentence
        else:
            current_chunk += sentence
    if current_chunk:  # Add the last chunk
        chunks.append(current_chunk)
    return chunks

if __name__ == '__main__':
    # Define your rate limiter
    rate_limiter = RateLimiter(max_calls=10, period=1)

    # Define your list of files
    files = ["file1.txt", "file2.txt", "file3.txt"]

    # Create a dictionary to hold translated chunks
    translated_data = {}

    # Create chunks of text from each file
    chunks_to_translate = []
    for file in files:
        chunks = split_into_chunks(file)
        for i, chunk in enumerate(chunks):
            chunks_to_translate.append((file, i, chunk))

    # Create a ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_chunk = {executor.submit(translate_chunk, chunk): chunk for chunk in chunks_to_translate}

        for future in concurrent.futures.as_completed(future_to_chunk):
            chunk = future_to_chunk[future]
            try:
                translated_text = future.result()
                if chunk[0] not in translated_data:
                    translated_data[chunk[0]] = {}
                translated_data[chunk[0]][chunk[1]] = translated_text
            except Exception as exc:
                logging.error(f"{chunk[0]} generated an exception: {exc}")

    # Reassemble the translated text for each file
    for file in files:
        filename = os.path.basename(file)
        chunks = translated_data[filename]
        with open(f"translated_{filename}", 'w') as out_file:
            for i in sorted(chunks):
                out_file.write(chunks[i])
        logging.info(f"Translated file saved: translated_{filename}")
