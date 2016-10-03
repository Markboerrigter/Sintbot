from googleapiclient.discovery import build
import json
import requests

API_KEY = 'AIzaSyAkFppBmrChhtF6UlvxoVcx7kJg3U8YCOM'

def trans(text, langin, langout):
    translation = requests.get('https://www.googleapis.com/language/translate/v2?key='+ API_KEY +
    '&q='+text+'&source='+ langin+ '&target='+ langout).text
    return(translation.split('t": "')[1].split('"')[0])

def detect(text):
    language = requests.get('https://www.googleapis.com/language/translate/v2/detect?key=' + API_KEY + '&q=' + text ).text
    return(language.split('ge": "')[1].split('"')[0])

def allEng(text):
    if detect(text) == 'nl':
        text = trans(text, 'nl', 'en')
    return text
