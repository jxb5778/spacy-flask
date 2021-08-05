
import json
from flask import request

from app import app

from app import controller


@app.route('/ner', methods=['POST'])
def ner():
    data = request.data
    ner_data = controller.spacy_ner(data)
    response = json.dumps(ner_data)
    return response
