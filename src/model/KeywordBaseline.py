import numpy as np
from sklearn.metrics import classification_report, accuracy_score
from collections import Counter
from src.dataset import load_preprocessed_dataset
from src.tfidf_vectorizer import tfidf_vectorizer


class KeywordBaseline:
    def __init__(self):
        self.keyword_mapping = {}
        self.default_label = 0
        self.X_train = None
        self.y_train = None

    def prepare_data(self):
        train, _ = load_preprocessed_dataset()
        self.X_train = tfidf_vectorizer.fit_transform(train['TEXT'])
        self.y_train = train['Label'].values
    
    def extract_keywords(self, top_n=10):
        unique_labels = np.unique(self.y_train)
        
        for label in unique_labels:
            label_indices = np.where(self.y_train == label)[0]
            X_label = self.X_train[label_indices]
            word_counts = np.asarray(X_label.sum(axis=0)).flatten()
            top_indices = word_counts.argsort()[-top_n:][::-1]
            feature_names = tfidf_vectorizer.get_feature_names_out()
            keywords = [feature_names[i] for i in top_indices if word_counts[i] > 0]
            self.keyword_mapping[label] = keywords
    
    def predict(self, texts):
        X_test = tfidf_vectorizer.transform(texts)
        predictions = []
        
        for i in range(X_test.shape[0]):
            text_vector = X_test[i]
            label_scores = {label: 0 for label in self.keyword_mapping.keys()}
            
            for label, keywords in self.keyword_mapping.items():
                for keyword in keywords:
                    keyword_index = tfidf_vectorizer.vocabulary_.get(keyword)
                    if keyword_index is not None:
                        label_scores[label] += text_vector[0, keyword_index]
            
            predicted_label = max(label_scores, key=label_scores.get)
            if label_scores[predicted_label] == 0:
                predicted_label = self.default_label
            
            predictions.append(predicted_label)
        
        return predictions

if __name__ == "__main__":
    baseline = KeywordBaseline()
    baseline.prepare_data()
    baseline.extract_keywords(top_n=10)
    print(list(baseline.keyword_mapping.items())[0:5])

