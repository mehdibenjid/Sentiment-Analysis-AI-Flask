# Use the Watson NLP BERT sentiment Analysis function to analyze the sentiment of the text provided.
# The function should return the sentiment label and the confidence score of the sentiment.
# The function should be named sentiment_analyzer and should take a single argument text_to_analyse.
# The function should return the sentiment label and the confidence score of the sentiment.
# The sentiment label should be one of the following: positive, negative, neutral.
# The confidence score should be a float value between 0 and 1.
import requests
def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json=myobj, headers=header)
    return response.text