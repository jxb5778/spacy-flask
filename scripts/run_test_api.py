
import requests
import json

from pprint import pprint


URL = 'http://localhost:5000/ner'

TEST_TEXT = "Justin lives in D.C."

resp_data = requests.post(url=URL, data=TEST_TEXT, headers={'Content-type': 'text/plain'})
resp = json.loads(resp_data.content)

pprint(resp)
