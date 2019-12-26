import spacy


class Similarity:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_md")

    def get_similarity(self, term1, term2):
        words = str(term1) + " " + str(term2)
        tokens = self.nlp(words)
        return tokens[0].similarity(tokens[1])


"""
"""