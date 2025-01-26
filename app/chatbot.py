import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import re
import os

class BankChatbot:
    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(__file__), '../data/BankFAQs.csv')
        self.df = pd.read_csv(self.data_path)
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = None
        self._prepare_data()

    def _clean_text(self, text):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return text.strip()

    def _prepare_data(self):
        self.df['clean_question'] = self.df['Question'].apply(self._clean_text)
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['clean_question'])

    def get_answer(self, question):
        clean_question = self._clean_text(question)
        question_vec = self.vectorizer.transform([clean_question])
        similarity_scores = cosine_similarity(question_vec, self.tfidf_matrix)
        best_match_idx = similarity_scores.argmax()
        return self.df.iloc[best_match_idx]['Answer']

    def save_model(self):
        model_dir = os.path.join(os.path.dirname(__file__), 'models')
        os.makedirs(model_dir, exist_ok=True)
        
        with open(os.path.join(model_dir, 'chatbot_model.pkl'), 'wb') as f:
            pickle.dump(self, f)
        with open(os.path.join(model_dir, 'tfidf_vectorizer.pkl'), 'wb') as f:
            pickle.dump(self.vectorizer, f)

    @classmethod
    def load_model(cls):
        model_path = os.path.join(os.path.dirname(__file__), 'models/chatbot_model.pkl')
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model

if __name__ == '__main__':
    chatbot = BankChatbot()
    chatbot.save_model()
    print("Model trained and saved successfully!")