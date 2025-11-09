import numpy as np
import scipy.sparse as sp

def save_tfidf_matrix_sparse(X_tfidf, file_prefix):
    sp.save_npz(f'{file_prefix}_sparse.npz', X_tfidf)
    
    np.save(f'{file_prefix}_feature_names.npy', tfidf_vectorizer.get_feature_names_out())

save_tfidf_matrix_sparse(X_tfidf, 'tfidf_matrix')

def load_tfidf_matrix_sparse(file_prefix):
    X_loaded = sp.load_npz(f'{file_prefix}_sparse.npz')
    feature_names = np.load(f'{file_prefix}_feature_names.npy', allow_pickle=True)
    return X_loaded, feature_names

X_loaded, feature_names = load_tfidf_matrix_sparse('tfidf_matrix')