import paralleldots
paralleldots.set_api_key('IH4OCcC3pwUFU6jRcoyzug4ShpopFEtpLFigQEZImmk')

def ner(text):
    ner = paralleldots.ner(text)
    return ner

def sentiment_analysis(text):
    response = paralleldots.sentiment(text)
    return response

def abuse_detection(text):
        response = paralleldots.abuse(text)
        return response

def emotion_prediction(text):
        response = paralleldots.emotion(text)
        return response

def do_taxonomy(text):
    response = paralleldots.taxonomy(text)
    return response