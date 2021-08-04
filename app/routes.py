
import json

from app import app

from app.controller.spacy_ner_handler import spacy_ner_handler


@app.route('/')
@app.route('/ner')
def ner(data):
    ner_data = spacy_ner_handler(data)
    response = json.dumps(ner_data)
    return response
