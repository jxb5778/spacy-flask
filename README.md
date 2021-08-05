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

### Usage
You can run the API locally with Flask or on a server with Gunicorn.

1. First, open a command prompt and activate your spacyner conda env 
    1. `conda activate spacyner`
2. Then change directory to this project 
    1.`cd /your/local/copy/of/spacy_flask`
3. To run with locally with Flask, run the command
    1. `python spacy_flask.py`
    2. **You can also run the API locally by running the 
    spacy_flask.py script in an IDE.
4. When running the API on a server, run using Gunicorn with command
    1. `gunicorn --bind 0.0.0.0:5000 wsgi:app`
    
---

## Scripts
Here's the scripts to test using the API, 
see what you get when you change the example text!

1. scripts/
    1. run_test_api.py
        1. You first need to start the API endpoint, either in 
        your IDE or with GUnicorn.
        2. This script sends the example text to the endpoint
        and decodes the response.
    2. command_list_text.txt
        1. First start the API using Flask or Gunicorn.
        2. Next, open a command prompt and run the command in the txt file.
