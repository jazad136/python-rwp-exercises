def downloads():
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('averaged_perceptron_tagger')

if __name__ == '__main__':
    downloads()