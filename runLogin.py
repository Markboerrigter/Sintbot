import json
import facebook
import urllib
import pickle
import pprint

import numpy
# import urlparse
import subprocess
import warnings
import requests
from PersonalityTest import getPersonality

from translateGoogle import trans, detect, allEng

# print(translate.translate('hallo ik ben Mark'))

from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()


stopset = pickle.load( open( "stopset.p", "rb" ) )

sentimentClassifier = pickle.load( open( "sentiment_analysis_final.p", "rb" ) )

FB_APP_ID = '321396144861053'
FB_APP_SECRET = '6b9ee66ca451209dd55a1dacd47932b3'
FB_PROFILE_ID = 'me'

def get_fb_token(app_id, app_secret):
    payload = {'grant_type': 'client_credentials', 'client_id': FB_APP_ID,
    'client_secret': FB_APP_SECRET, 'redirect_uri': 'https://www.facebook.com/connect/login_success.html'}
    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
    #print file.text #to test what the FB api responded with
    result = file.text.split("=")[1]
    #print file.text #to test the TOKEN
    return result

def getIt(sender):
    # print(trans('hoi ik ben mark', 'nl', 'en'))
    # print(detect('hoi ik ben mark'))
    #
    # print(allEng('Ik ben op zoek naar een huis'))
    token = 'EAAVJQyYb958BAAGBvlYuonE3VZAa2LxCZCzdzRH2USUSYEWOAy0ZBahfV0xqIKGHQ8wzQ9NDKy3eco7JfOn0jULaJJLKlfnAZBv70IJEO4uNu28GGgRZBkrj1yLPYbQrDeE4PEAGZCNKC9KDlkrcjJospRAO5ZCMToK0smK7gZB2xQZDZD'
    # token = get_fb_token(FB_APP_ID,FB_APP_SECRET)
    perm =requests.get('https://www.facebook.com/v2.8/dialog/oauth?client_id='+ FB_APP_ID + '&redirect_uri=https://www.facebook.com/connect/login_success.html')
    # Set the users profile FBML
    print(perm)
    facebook_graph = facebook.GraphAPI(token)
    permissions = requests.get('https://graph.facebook.com/v2.6/'+sender + '/permissions')

    # permissions = facebook_graph.request(sender + '/permissions')
    print(permissions.text)

    profile = facebook_graph.get_object(sender)
    print(profile)

    text = []
    # Try to post something on the wall.
    try:
        fb_response = facebook_graph.get_connections(sender, "posts", limit = 200)
        for x in fb_response['data']:
            if 'message' in x:
                text.append(x['message'])
        # for key in fb_response:
        #     print(key)
    except facebook.GraphAPIError as e:
        print('Something went wrong:', e.type, e.message)

    # for line in text:
        # line = allEng(line)
        # print(line)

    personality_text = ('\n'.join(text))


    personality = getPersonality(personality_text, profile['name'], 'facebook')
    pprint.pprint(personality)
    # print(json.dumps(json.loads(personality), indent =4, sort_keys=True))
    def word_feats(words):
        return dict([(word, True) for word in words.split() if word not in stopset])

    # Hij neemt nu letter voor letter of woord voor woord*


    sentiment = [sentimentClassifier.prob_classify(word_feats((sent))) for sent in text]

    sentiment = [[sent.prob('pos'), sent.prob('neg'), sent.prob('obj')] for sent in sentiment]

    # sentiment = numpy.mean(sentiment,axis=0)
    # print(sentiment)

    return personality, sentiment
    # ['children']['children'])

if __name__ == '__main__':
    getIt('me')
