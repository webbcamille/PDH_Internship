import io
import re
import string
import tqdm
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from gensim.models import Word2Vec
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')  # Download NLTK's punkt tokenizer data
import sklearn
from sklearn.metrics.pairwise import cosine_similarity
from Pull_plan import extract_Plan

file_name = input("Enter the path to the .txt file: ")

Plan_data = extract_Plan(file_name)

# Split the text based on 2 or more newlines
blocks = re.split(r'\n\n+', Plan_data.strip())

wb = Workbook()
ws = wb.active

for block in blocks:
    # Extract the header by finding the first newline or the first uppercase letter followed by a lowercase letter
    match = re.search(r'([A-Z][a-z])', block)
    if match:
        start = match.start()
        header = block[:start].strip()
        content = block[start:].strip()

        # Write to Excel
        ws.append([header, content])

wb.save("output.xlsx")








