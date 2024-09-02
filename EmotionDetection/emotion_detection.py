import requests
import json
import operator
def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = myobj, headers=Headers) 

    if response.status_code == 400:
        return {'anger':None,'fear':None,'disgust':None,'joy':None,'sadness':None,'dominant_emotion':None}

    formatted_response = json.loads(response.text)
    formatted_response=formatted_response['emotionPredictions'][0]

    
    anger = formatted_response['emotion']['anger']
    disgust = formatted_response['emotion']['disgust']
    fear = formatted_response['emotion']['fear']
    joy = formatted_response['emotion']['joy']
    sadness = formatted_response['emotion']['sadness']
    emotions = {'anger':anger,'disgust':disgust,'fear':fear,'joy':joy,'sadness':sadness}
    dominant = max(emotions.items(), key=operator.itemgetter(1))[0]
    emotions['dominant_emotion'] = dominant
    return emotions

