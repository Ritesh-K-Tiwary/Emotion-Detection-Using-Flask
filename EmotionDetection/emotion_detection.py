import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # predictions = formatted_response.get('emotionPredictions', [])
    # if predictions and 'emotion' in predictions[0]:
    #     emotions = predictions[0]['emotion']

    #     # Find the emotion with the highest score
    #     label = max(emotions, key=emotions.get)
    #     score = emotions[label]

    #     return {'label': label, 'score': score}
    if formatted_response.status_code == 200:
        return formatted_response
    elif formatted_response.status_code == 400:
        predictions = formatted_response.get('emotionPredictions', [])
        predictions[]['emotion'].key = None
        return prediction
        
