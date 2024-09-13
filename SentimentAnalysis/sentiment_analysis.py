"""
    This module provides sentiment analysis functionality using an external API.
"""
import json
import requests
def sentiment_analyzer(text_to_analyse):
    """
    Sends text to an external API for sentiment analysis and returns the sentiment label and score.

    Args:
        text_to_analyse (str): The text to be analyzed.

    Returns:
        dict: A dictionary containing 'label' and 'score' keys for the sentiment analysis result.
    """

    # URL of the sentiment analysis service
    url = (
        'https://sn-watson-sentiment-bert.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/SentimentPredict'
    )

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header, timeout=10)


    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    label = None
    score = None
    # Extracting sentiment label and score from the response
    if response.status_code == 200 :
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500 :
        label = None
        score = None

    # Returning a dictionary containing sentiment analysis results
    return {'label': label, 'score': score}
