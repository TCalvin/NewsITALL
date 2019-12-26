# run "python -m spacy download en_core_web_sm" before using this script, needs model to load
import spacy
from spacy.lang.en import English


class Extractor:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        self.nlp2 = English()
        self.nlp2.add_pipe(self.nlp.create_pipe('sentencizer'))

    def getSentences(self, document):
        doc = self.nlp2(document)
        return [sent.string.strip() for sent in doc.sents]

    def getEntities(self, sentence):
        entities = list()
        doc = self.nlp(sentence)
        for ent in doc.ents:
            entities.append(ent)
        return entities

    def getNounChunks(self, sentence):
        chunks = list()
        doc = self.nlp(sentence)
        for chunk in doc.noun_chunks:
            chunks.append(chunk)
        return chunks
