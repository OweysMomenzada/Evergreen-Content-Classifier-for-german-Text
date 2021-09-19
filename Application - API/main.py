import googleapiclient.discovery
from google.api_core.client_options import ClientOptions
from google.oauth2 import service_account

from flask import Flask, render_template, request, abort, jsonify

import re
from transformers import AutoTokenizer, TFAutoModel

tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-uncased")
MAX_LENGTH = 512
GERMAN_STOP_WORDS = None

PROJECT_ID = "PROJECT-ID"
MODEL_NAME = "MODELNAME"
VERSION_NAME = "v1"
REGION = "REGION"
PROJECT = 'PROJECTNAME'
KEY_PATH = "credentials.json"

credentials = service_account.Credentials.from_service_account_file(
    KEY_PATH, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api", methods=["POST"])
def get_json():
    if request.method == "POST":
        if request.json:
            request_json = request.json
            if 'text' in request_json:
                results = get_result(request_json['text'])
                json_result = {
                    "label": results[1],
                    "evergreen_probability": results[0],
                    "is_truncated": results[2]
                    }

                return jsonify(json_result)
            abort(400, 'JSON data missing text field.')
        abort(415)
    abort(405)

    
GERMAN_STOP_WORDS = load_stopwords()


def load_stopwords():
    # load own stopword list generated in the EDA and add it to the old stopwords
    with open('stopwords_nltk+eda.txt', 'r', encoding="utf-8") as f:
        stop_words = f.read().split(',')

    # cleaning the stopword list
    stop_words = [w.replace("'", '') for w in stop_words]
    stop_words = [w.replace("\n", '') for w in stop_words]
    stop_words = [w.replace(" ", '') for w in stop_words]

    return stop_words


def remove_stopwords(text):
    # load stop words
    german_stop_words = GERMAN_STOP_WORDS
    text = [word.lower() for word in text.split() if word.lower() not in german_stop_words]

    return " ".join(text)


def clean_text(text_content):
    text_content = re.sub('[»„‘’“”…]', ' ', text_content)
    text_content = re.sub(r'https?://\S+|www\.\S+', ' ', text_content)
    text_content = re.sub('[\u0080-\uffff]w{1-3}', ' ', text_content)
    text_content = re.sub(r'[^\x00-\x7F\w{1,3}]+', ' ', text_content)

    text_content = remove_stopwords(text_content)

    return text_content


def get_if_truncated(text_content):
    word_list = text_content.split()
    number_of_words = len(word_list)

    return number_of_words > MAX_LENGTH


def tokenize_slice_text(text):
    tokens = tokenizer.encode_plus(text, max_length=MAX_LENGTH, padding='max_length', add_special_tokens=True,
                                   truncation=True, return_token_type_ids=False, return_attention_mask=True,
                                   return_tensors='tf')

    Xids = tokens['input_ids']
    Xmask = tokens['attention_mask']

    return [Xids, Xmask]


def predict_json(project, region, model, instances, version=None):
    prefix = "{}-ml".format(region) if region else "ml"
    api_endpoint = "https://{}.googleapis.com".format(prefix)
    client_options = ClientOptions(api_endpoint=api_endpoint)
    service = googleapiclient.discovery.build(
        'ml', 'v1', client_options=client_options, credentials=credentials)
    name = 'projects/{}/models/{}'.format(project, model)

    if version is not None:
        name += '/versions/{}'.format(version)

    response = service.projects().predict(
        name=name,
        body={'instances': instances}
    ).execute()

    if 'error' in response:
        raise RuntimeError(response['error'])

    return response['predictions']


def predict_evergreen(text):
    #text = clean_text(text)
    is_truncated = get_if_truncated(text)
    text_tokenized = tokenize_slice_text(text)

    instances = [{
        'input_ids': [int(v.numpy()) for v in list(text_tokenized[0][0])],
        'attention_mask': [int(v.numpy()) for v in list(text_tokenized[1][0])]}]

    request = predict_json(PROJECT_ID, REGION, MODEL_NAME, instances, version=VERSION_NAME)

    return round(request[0][0], 4), is_truncated


def evergreen_label(prediction):
    if prediction < 0.4:
        return 'Ephemeral'
    elif prediction > 0.7:
        return 'Evergreen'
    else:
        return 'Uncertain'


def get_result(text):
    prediction, is_truncated = predict_evergreen(text)
    label = evergreen_label(prediction)

    return prediction, label, is_truncated


if __name__ == "__main__":
    app.run(port=9000, debug = True)