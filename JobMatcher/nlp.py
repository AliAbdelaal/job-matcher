import os
import numpy as np
import pandas as pd
import spacy
from sklearn.metrics.pairwise import cosine_distances

ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
DATA_PATH = os.path.join(ASSETS_PATH, "cleaned_data.csv")
VECTORS_PATH = os.path.join(ASSETS_PATH, "jobs_vectors.npy")

class Matcher():

    def __init__(self):
        self.nlp = spacy.load("en_core_web_md")
        # check for the data
        if not os.path.exists(DATA_PATH):
            raise Exception(f"Data file {DATA_PATH} was not found, please check the readme file")
        if not os.path.exists(VECTORS_PATH):
            raise Exception(f"Vectors file {DATA_PATH} was not found, please check the readme file")
        self.jobs_df = pd.read_csv(DATA_PATH)
        # remove nan values as they are not serializable
        self.jobs_df.fillna("N/A", inplace=True)
        self.vectors = np.load(VECTORS_PATH)

    def sent2vec(self, text):
        """Convert input text to vector

        Parameters
        ----------
        text : str
            the input string by the user

        Returns
        -------
        np.array
            a vector array of shape (300,)
        """
        vector = np.zeros(300,)
        valid_tokens = 0
        for token in self.nlp(text):
            if not token.is_stop and not token.is_punct and token.has_vector:
                vector += token.vector
                valid_tokens += 1
        vector = vector/valid_tokens if valid_tokens > 1 else vector
        return vector


    def get_top_similar(self, query, top_k=5)->list:
        """get most similar jobs to the user input

        Parameters
        ----------
        query : str
            the user prompt
        top_k : int, optional
            how many similar jobs to search, by default 5

        Returns
        -------
        list
            list of dictionaries where each one represent a job, sorted by their relevance
        """
        vector = self.sent2vec(query)
        # get similarity scores
        distances = cosine_distances([vector], self.vectors)
        most_similar = np.argsort(distances).flatten()[:top_k]
        # retrieve the jobs
        jobs = self.jobs_df.iloc[most_similar].to_dict(orient='records')    
        return jobs