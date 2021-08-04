
import spacy

from app.controller.base_handler import BaseHandler


class SpacyNERHandler(BaseHandler):
    def __init__(self):
        self.is_initialized = False

    def initialize(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.is_initialized = True

    def preprocess(self, data):
        if isinstance(data, (bytes, bytearray)):
            data = data.decode('utf-8')
        return data

    def inference(self, data):
        doc = self.nlp(data)
        return doc

    def postprocess(self, data):
        
        entities = {
            'results': [
                {
                    'text': ent.text,
                    'start_idx': ent.start_char,
                    'end_idx': ent.end_char,
                    'type': ent.label_
                }
                for ent in data.ents
            ]
        }
                
        return entities

    def handle(self, data):

        data = self.preprocess(data)
        data = self.inference(data)
        data = self.postprocess(data)

        return data

    def __call__(self, data):
        return self.handle(data)


spacy_ner_handler = SpacyNERHandler()
spacy_ner_handler.initialize()
