import requests

def getGeneratedImage(textPrompt: str):
    url = 'http://localhost:8000/image/generate'
    myobj = {'textPrompt': textPrompt}
    apiResponse = requests.post(url, json = myobj)
    return apiResponse.json()