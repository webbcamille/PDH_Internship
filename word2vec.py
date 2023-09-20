from gensim.models import Word2Vec
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')  # Download NLTK's punkt tokenizer data

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def tokenize_text(text):
    # Tokenize the text into words
    tokens = word_tokenize(text)
    return tokens

def train_word2vec_model(sentences):
    model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
    return model

def main():
    
    file_path = r"C:\Users\Administrator\Documents\ParaDocsHealthPrototypes-main\ParaDocsHealthPrototypes-main\Input Files\2023_First1Last1.txt"
    text = read_text_from_file(file_path)
    tokens = tokenize_text(text)

    # Train the Word2Vec model
    model = train_word2vec_model([tokens])

    # Now you have a trained Word2Vec model that can be used to generate word embeddings.
    # You can use model.wv to access the word embeddings.

if __name__ == "__main__":
    main()
   