import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.tokenize import word_tokenize
from sklearn.calibration import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk


def __init__(self, root):
    self.root = root
    self.root.title("ML Utils")
    dir = f"{os.getcwd()}/nltk_datasets"
    nltk.data.path.append(dir)
    nltk.download("stopwords", download_dir=dir)
    nltk.download("punkt", download_dir=dir)
    nltk.download("maxent_ne_chunker", download_dir=dir)
    nltk.download("words", download_dir=dir)
    nltk.download("tagsets", download_dir=dir)
    nltk.download("averaged_perceptron_tagger", download_dir=dir)


def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words]
    return " ".join(filtered_text)


def stem_text(text):
    stemmer = PorterStemmer()
    words = word_tokenize(text)
    stemmed_words = [stemmer.stem(word) for word in words]
    return " ".join(stemmed_words)


def extract_entities(text):
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    ne_chunks = ne_chunk(pos_tags)

    entities = []
    for chunk in ne_chunks:
        if hasattr(chunk, "label") and chunk.label():
            if chunk.label() == "NE":
                entities.append(" ".join([c[0] for c in chunk]))
    return entities


def create_tfidf_vectorizer(df):
    vectorizer = TfidfVectorizer(max_features=10000, use_idf=True)
    # Fit and transform the text data in the DataFrame column
    tfidf_matrix = vectorizer.fit_transform(df["sentence"])
    # Convert the TF-IDF matrix to a DataFrame for visualization
    return tfidf_matrix.toarray()


def tokenize_sentences(df):
    tr_text = df["sentence"]
    tokenizer = Tokenizer(num_words=10000)
    tokenizer.fit_on_texts(tr_text)

    sequences = tokenizer.texts_to_sequences(tr_text)
    return sequences


def encode_emotions(emotions):
    encoder = LabelEncoder()
    return encoder.fit_transform(emotions)


def pad_sequences_with_zeros(X, maxlen):
    return pad_sequences(X, maxlen=maxlen)


def check_frequency_of_words(df):
    # Combine all sentences into one string
    all_sentences = " ".join(df["sentence"].tolist())

    # Tokenize the combined text into words
    words = all_sentences.split()

    # Create a Pandas Series to count word frequencies
    word_freq = pd.Series(words).value_counts()

    # Plot the top 20 most frequent words
    plt.figure(figsize=(10, 6))
    word_freq.head(20).plot(kind="bar", color="skyblue")
    plt.title("Top 20 Most Frequent Words in Sentences")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
