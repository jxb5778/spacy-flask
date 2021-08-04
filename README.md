# spaCy - Flask API
This is a template project for hosting an ML model as an API.

---

## Setup
1. To get started, first create a conda environment.
    1. `conda create --name spacyner python=3.8`
 
2. Next, activate the new env, change directory to this project,
and install the requirements.txt.
    1. `conda activate spacyner`
    2. `cd path/to/your/local/spacy-flask/`
    3. `pip install -r requirements.txt`

3. Download the spaCy model used in this project.
    1. `python -m spacy download en_core_web_sm`

4. That's it! Your local environments should be set up and ready to run!

---

## Scripts
Here's the script to test using the API

1. scripts/run_test_api.py
    1. You first need to start the API endpoint, either in your IDE 
    or with GUnicorn.
    2. This script sends the example text to the endpoint
     and decodes the response.
