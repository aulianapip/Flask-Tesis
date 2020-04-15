# feature_extraction.py
import numpy as np


class FeatureExtraction:

    def __init__(self):
        pass

    def fit(self, documents):

        # 0 buat vocab
        vocab = set([])
        for document in documents:
            vocab.update(document)
        vocab = list(vocab)

        # 1 hitung term frequency
        feature = np.zeros((len(documents), len(vocab)))
        for row, document in enumerate(documents):
            for word in document:
                if word in vocab:
                    column = vocab.index(word)
                    feature[row, column] += 1

        # 1.1 term frequency dibagi jumlah total kata yang ada di dokumen
        n_word_documents = feature.sum(axis=1)
        # feature N X M
        # n_words_documents 1 X N -> N x 1
        # tf N X M
        tf = feature

        # 2 hitung inverse document frequency
        # jumlah total dokomen / jumlah dokumen yg mengandung kata ke-t di
        # vocab
        n_documents = len(documents)  # scalar
        n_documents_words = (feature > 0).sum(axis=0)  # 1 X M

        # print n_documents
        # print n_documents_words

        idf = np.log10(float(n_documents) / n_documents_words)

        baru = feature * idf

        # 3 tf - idf
        tf_idf = tf * idf  # N X M * 1 x M
       

        # vocab dan idf akan dipakai waktu testing
        self.vocab = vocab
        self.idf = idf

        return tf_idf

