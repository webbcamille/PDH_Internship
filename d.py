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

def extract_Plan(plan):
    '''Extracts the section between - Assessment - and - Plan -'''
    with open(plan, 'r') as file:
        lines = file.readlines()

    # Identify the start and end of the desired section
    try:
        start_index = lines.index('- Plan -\n') + 1
        #Identify the end index by looking for the pattern "- ANY_WORDS -"
        pattern = r"CPT"
        end_index = next((i for i, line in enumerate(lines[start_index:], start=start_index) if re.match(pattern, line) and line.strip()), None)
        
    except ValueError:
        print("Section not found")
        return []
    
    return lines[start_index:end_index]

lines = extract_Plan(r"C:\Users\Administrator\Documents\ParaDocsHealthPrototypes-main\ParaDocsHealthPrototypes-main\Input Files\2023_First1Last1.txt")

# Tokenize each line into words
tokens = [word_tokenize(line.lower()) for line in lines]

# Flatten the list of lists to get a single list of tokens
flattened_tokens = [word for line_tokens in tokens for word in line_tokens]

###print(len(flattened_tokens))

vocab, index = {}, 1  # start indexing from 1
vocab['<health>'] = 0  # add a padding token
for token in flattened_tokens:
  if token not in vocab:
    vocab[token] = index
    index += 1
vocab_size = len(vocab)

print(vocab['pain'])

model = Word2Vec(vocab, vector_size=100, window=5, min_count=1, workers=4)

# Get the word embeddings (vectors)
word_embeddings = model.wv

word1 = 'pain'

vector_word1 = word_embeddings[word1]

print(vector_word1)