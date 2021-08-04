
import json
from flask import request

from app import app

from app.controller.spacy_ner_handler import spacy_ner_handler


@app.route('/ner', methods=['POST'])
def ner():
    data = request.data
    ner_data = spacy_ner_handler(data)
    response = json.dumps(ner_data)
    return response
