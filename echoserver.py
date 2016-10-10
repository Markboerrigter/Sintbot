from flask import Flask, request
import json
import requests
import sys
from wit import Wit
import talkBot as tb
from runLogin import getIt
import pickle
import random
import datetime

# personality, sentiment = getIt()

from flask import g
# x = dict()
# pickle.dump(x, open('user_data.p', 'wb'))

user_data = pickle.load( open( "user_data.p", "rb" ) )


def word_feats(words):
    return dict([(word, True) for word in words])

import pickle

sentimentClassifier = pickle.load( open( "sentiment_analysis_final.p", "rb" ) )

app = Flask(__name__)

# with app.app_context():
#     app.session['uid'] = 'session-' + str(datetime.datetime.now()).replace(" ", "")

TokensSave = ['F2OE72NYJ6BGKXPHC2IXPCFG6JNFPVIN','K4UKHMU3JYRF2N3GNW3ALA7BUQFWP7LM','YDN4UEPTRUHBMFTQJZZLLQW5OVVH4QJS']
Tokens = TokensSave
tokenWit = Tokens[0]
pickle.dump(tokenWit, (open("tokenWit.p", "wb")))
# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
PAT = 'EAAEkTt8L730BAJzPxFYza8w3Ob9SlH41MwZArFoLFdGCSpgPYkoOB2zfIOJnaDhhP922PyEIayJH5HpzMKZCGM0IcbvZBZCrKRaFY1tj27pGsFcAu2KzvO8ZCusT5OvsUG9RghmR9UDMIOND2prsW5RL4taRe15YgZAtwrgRsM1QZDZD'

@app.route('/', methods=['GET'])
def handle_verification():
  print "Handling Verification."
  if request.args.get('hub.verify_token', '') == 'my_voice_is_my_password_verify_me':
    print "Verification successful!"
    return request.args.get('hub.challenge', '')
  else:
    print "Verification failed!"
    return 'Error, wrong validation token'

@app.route('/', methods=['POST'])
def handle_messages():
  print "Handling Messages"
  payload = request.get_data()
  print payload
  global user_data
  for sender, message in messaging_events(payload):
    if sender in user_data:
        if 'stop' in user_data[sender]:
            user_data[sender]['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
            user_data[sender]['token'] = tokenWit
        print "Incoming from %s: %s" % (sender, message)
        print(sender, message)
        send_message(PAT, sender, message,user_data[sender])
    else:
        r = requests.post("https://graph.facebook.com/v2.6/me/thread_settings",
          params={"access_token": PAT},
          data=json.dumps({  "setting_type":"greeting",
          "greeting":{
            "text":"Timeless apparel for the masses."
          }}),
          headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
          print r.response
        # user_data[sender= [Tokens]
        user_data[sender] = dict()
        user_data[sender]['token'] = tokenWit
        user_data[sender]['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
        print(sender, message)
        send_message(PAT, sender, message, user_data[sender])
  return "ok"

def find_sender():
    payload = request.get_data()
    data = json.loads(payload)
    messaging_events = data["entry"][0]["messaging"]
    for sender, message in messaging_events(payload):
        return sender

def messaging_events(payload):
  """Generate tuples of (sender_id, message_text) from the
  provided payload.
  """
  data = json.loads(payload)
  messaging_events = data["entry"][0]["messaging"]
  for event in messaging_events:
    if "message" in event and "text" in event["message"]:
      yield event["sender"]["id"], event["message"]["text"].encode('unicode_escape')

def findAnswer(response, question,witToken,data):
    # if response['type'] == 'stop':
    #     if 'ja_nee' in response['entities']:
    #         text = response['entities']['ja_nee'][0]['value']
    #         response = tb.response(text, witToken, session_id, {})
    #         print(response)
    session_id = data['session']
    response = mergeAns(response, witToken, session_id)
    if 'msg' in response:
        msg = response['msg'].split(',')
        if msg[0] == 'Stop':
            # global session_id
            print(response)
            print('Stop Message')
            print(msg)
            data['token'] = TokensSave[int(msg[2]):][0]
            # pickle.dump(tokenWit,(open("tokenWit.p", "wb")))
            #  app.session['uid'] = 'session-' + str(datetime.datetime.now()).replace(" ", "")
            data['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
            print('new id :' + data['session'])
            #  pickle.dump(session_id,(open("tokenWit.p", "wb")))
            return tb.response(msg[1], data['token'], data['session'], {}), data
        else:
            return response, data
    else:
        return response,data

def mergeAns(response, witToken, session_id):
    if 'type' in response:
        action = response['type']
        if action == 'merge':

            print(response['entities'])
            text = ''
            return tb.response(text, witToken, session_id, tb.merge(response))
        else:
            return response
    else:
        return response


def send_message(token, recipient, text, data):
  # witToken = pickle.load( open( "tokenWit.p", "rb" ) )
  """Send the message text to recipient with id recipient.
  """
  print(data)
  # global session_id
  # print(witToken)
  #print(response['text'])
  response, data = findAnswer(tb.response(text, data['token'], data['session'], {}),text,data['token'],data)
  # print(session_id)
  print(response)
  print('sending response')
  # response = mergeAns(response, witToken, session_id)
  if response['type'] == 'stop':
      response,data = findAnswer(tb.response(text, data['token'], data['session'], {}),text,data['token'],data)
      print(response)
      if response['type'] == 'stop':
          data['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
          print('new id :' + data['session'])

  # print(response)
  if 'msg' in response:
      print('pos: ' + str(sentimentClassifier.prob_classify(word_feats((response['msg']))).prob('pos')))
      if 'quickreplies' in response:
          replies = response['quickreplies']
          r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
              "recipient": {"id": recipient},
              "message": {"text": response['msg'].decode('unicode_escape'),
              "quick_replies":[{
                            "content_type":"text",
                            "title":x,
                            "payload":x
                          } for x in replies]}

            }),
            headers={'Content-type': 'application/json'})
          if r.status_code != requests.codes.ok:
            print r.response
      else:
          r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
              "recipient": {"id": recipient},
              "message": {"text": response['msg'].decode('unicode_escape')}
            }),
            headers={'Content-type': 'application/json'})
          if r.status_code != requests.codes.ok:
            print r.response
  pickle.dump(user_data, open('user_data.p', 'wb'))

if __name__ == '__main__':
  # for i in range(len(Tokens)):
  #     Stop = False
  #
  #     while not Stop:
  #         keuze =
  #         witToken = Tokens[i]


  # personality, sentiment = getIt()
  # recipient = find_sender()
  # print(sentiment)
  # send_message(PAT, recipient, 'Welkom bij Spotta, waarmee kan ik u van dienst zijn?')


  app.run()
