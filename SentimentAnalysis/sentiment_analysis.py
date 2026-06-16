import requests
import json
def analyze(text):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text } }
    response = requests.post(url, json = myobj, headers=header)
    formatted = json.loads(response.text)
    if response.status_code==200:
        label = formatted['documentSentiment']['label']
        score = formatted['documentSentiment']['score']
    else:
        label = None
        score = None
    return {'score' : score , 'label' : label}
    
