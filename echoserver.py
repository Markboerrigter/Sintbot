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
import mongo as mg
import pprint
from copy import copy

# personality, sentiment = getIt()

from flask import g
x = dict()
pickle.dump(x, open('user_data.p', 'wb'))

user_data = pickle.load( open( "user_data.p", "rb" ) )



def word_feats(words):
    return dict([(word, True) for word in words])

import pickle

sentimentClassifier = pickle.load( open( "sentiment_analysis_final.p", "rb" ) )

app = Flask(__name__)

# with app.app_context():
#     app.session['uid'] = 'session-' + str(datetime.datetime.now()).replace(" ", "")

# TokensSave = ['F2OE72NYJ6BGKXPHC2IXPCFG6JNFPVIN','K4UKHMU3JYRF2N3GNW3ALA7BUQFWP7LM','YDN4UEPTRUHBMFTQJZZLLQW5OVVH4QJS']
# Tokens = TokensSave
Tokens = {}
Tokens['Start'] = {}
Tokens['Start']['New'] = {}
Tokens['Start']['New']['Introduce'] = 'D7JHYWLOPGPFHJRCHPWC7DBCBEK2G7RZ'
Tokens['Start']['New']['Sinterklaas'] = 'TT4U2XJYSY6EZBUKIBGAJPHDNWDZVGVL'
Tokens['Start']['New']['Story'] = 'JW4QZSHW2GXLJKZEGPH6ZFOOP6PBYTKL'
Tokens['Start']['New']['Open'] = 'POPSPV3EUB7L3W56K4FOU7ZIMFMFKDRP'
Tokens['Start']['New']['loose'] = '6YY3HTLYKJG4HJOMEDPQ4BTUBA262SCY'
Tokens['Start']['longText'] = 'YZDGTRUDQU7H2BPRCWFIEVU4KSL42IK4'
Tokens['Start']['Old'] = {}
Tokens['Start']['Old']['recognized'] = 'IZ5AIDU7KEVIXG6RAWEOY4W6664XGX3R'
Tokens['Start']['Old']['oldFashioned'] = 'Z4NCJN2J2CJGNBVW64WQULIWCUD54HMB'
Tokens['Start']['Old']['longText'] = 'YZDGTRUDQU7H2BPRCWFIEVU4KSL42IK4'
Tokens['Start']['Old']['sintQuestioning'] = 'DNYI3O6EHFJ376YACLJSDCB3U7H7MXDB'
Tokens['decisions'] = {}
Tokens['decisions']['age'] = {}
Tokens['decisions']['gender'] = {}
Tokens['decisions']['budget'] = {}
Tokens['decisions']['age']['findage1'] = 'BQDMM2HIB7YSAXICR7QFULGKXQWJHKXJ'
Tokens['decisions']['age']['findage2'] = '5UTS7JO3NPTOHD52HAWKQOZBUNTFC53R'
Tokens['decisions']['gender']['findgender1'] = 'BBEESH7AOGULQK6L3TPYYRC4L4Y36LHH'
Tokens['decisions']['gender']['findgender2'] = 'UQVGOAZSC54YYVUGHURXHY5I4U6A2X3M'
Tokens['decisions']['budget']['findbudget1'] = 'IJ7PMHQPAVNK6UU3C3BE3NOVXZ6MMPOJ'
Tokens['decisions']['budget']['findbudget2'] = 'TB4QZIZYN4AZQPHYMWDCNFVOR3MJRUGI'
Tokens['presentchoosing'] = {}
Tokens['presentchoosing']['present'] = {}
Tokens['presentchoosing']['present']['normal'] = '5YVSD6XFV4I3Q457C56YRYLED5Q6E6ZK'
Tokens['presentchoosing']['present']['discount'] = 'RNZHGD6QHWG6JOZF66W52XHU364H4B6Y'
Tokens['presentchoosing']['present']['loyal'] = 'COHIUFQKSQMSGK6SNFLDR6D74CWZIJLZ'
Tokens['presentchoosing']['notFound'] = {}
Tokens['presentchoosing']['notFound']['stop1'] = 'B6ZPCLQVJDDKKRNXQFF2HFWF2LZJ27KT'
Tokens['presentchoosing']['notFound']['stop2'] = 'I376WUKZF6BKKUP2I3LQ4CTGF5UBYAOM'
Tokens['presentchoosing']['notFound']['popular'] = 'BQ44V4L72VQKETN5DRE7NKPMDPVJ276C'
Tokens['presentchoosing']['notFound']['keyword1'] = 'YPRANRJYCS4VPLXM3RZBOZA7V4R73TDY'
Tokens['presentchoosing']['notFound']['keyword2'] = '5CJ4C7UWBRIVLERLIU5XEMUN3WDUUM3H'
Tokens['feedback'] = {}
Tokens['feedback']['feedback1'] = 'Z7V53U4LAVY3JWEU6B32ZYBXK4SK6OEJ'
Tokens['feedback']['feedback1'] = '6ZUZHBITRTWR3PEJE26DZE6ZX3HHGGES'





TokenStages = ['Start', 'decisions', 'presentchoosing', 'feedback']

tokenWit = 'D4CRSEOIOCHA36Y2ZSQUG7YUCUK3BJBS'
pickle.dump(tokenWit, (open("tokenWit.p", "wb")))

returns = ['Hallo, ik ben Spot, de chatbot van Spotta! Waar kan ik u mee helpen?', 'Hallo daar, ik ben Sinterklaas. Zullen wij samen op zoek gaan naar het juiste kadootje?', ['Kent u het verhaal over Sinterklaas en het verloren kadootje?', ],
                    'Welcome back, why are you in this screen?', 'Hi, welcombe back in the Sinterklaas chat! Bent u weer op zoek naar een kado?', 'Goedendag, ik zie dat u ons weer gevonden heeft! Kan ik u helpen met het vinden van een kadootje?',
                    "Sorry, ik houd niet zo van die lange antwoorden. Ik stel voor om er nog eens rustig overheen te gaan. Bent u op zoek naar een kado?"]

#VERLORENKADOOTJE ID ##
# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
PAT = 'EAAEkTt8L730BAJzPxFYza8w3Ob9SlH41MwZArFoLFdGCSpgPYkoOB2zfIOJnaDhhP922PyEIayJH5HpzMKZCGM0IcbvZBZCrKRaFY1tj27pGsFcAu2KzvO8ZCusT5OvsUG9RghmR9UDMIOND2prsW5RL4taRe15YgZAtwrgRsM1QZDZD'
def get_keys(d,target):
    result = []
    path = []
    get_key(d,target, path, result)
    return result[0]


def get_key(d, target, path, result):
    for k, v in d.iteritems():
        path.append(k)
        if isinstance(v, dict):
            get_key(v, target, path, result)
        if v == target:
            result.append(copy(path))
        path.pop()

def makeStartScreen(token):
    print('hoi')
    print(type([{"payload":"LEUK BERICHTJES"}]))
    r = requests.post("https://graph.facebook.com/v2.6/me/thread_settings?access_token=" + token,
        {"setting_type":"call_to_actions",
        "thread_state":"new_thread",
        "call_to_actions":["LEUK BERICHTJES"]},
    headers={'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        print(dir(r))
        print r.reason
        print r.text

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
  print('message events')
  print(len([[sender, message] for sender, message in messaging_events(payload)]))
  for sender, message in messaging_events(payload):

    if sender in user_data:
        if 'stop' in user_data[sender]:
            user_data[sender]['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
            user_data[sender]['token'] = Tokens['Start']['Old'][random.choice(Tokens['Start']['Old'].keys())]
            user_data[sender]['Stage'] = 'StartOld'
        # else:
        #     # """" def findToken()
        #     # This formula should include a way to extract the old token and from this find the next
        #     # Token. In this the context and session should be used to find where in the story we are and therefore which deck of cards should be opened
        #     # It should return the old message and a new token.
        #     # """
        print("Incoming from %s: %s" % (sender, message))
        print(sender, message)
        send_message(PAT, sender, message,user_data[sender])
    else:
        # """"
        # First a introduction screen should be shown, this should happen whenever a user enters the chat.
        # After clicking the get start screen, the screen will show the chat with a first introductory text, which can be found in the Startnew dict
        # """"
        print('new')
        makeStartScreen(PAT)
        user_data[sender] = dict()
        user_data[sender]['oldmessage'] = ''
        user_data[sender]['token'] = Tokens['Start']['New'][random.choice(Tokens['Start']['New'].keys())]
        user_data[sender]['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
        user_data[sender]['Stage'] = 'StartNew'
        print(user_data)
        user_data[sender]['data'] = {}
        print(sender, message)
        send_message(PAT, sender, message, user_data[sender])
  return "ok"

def find_sender():
    payload = request.get_data()
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
    response = mergeAns(response, witToken, session_id, question)
    # print('Response in find answer')
    # print(response)
    if 'msg' in response:
        msg = response['msg'].split(',')
        # if msg[0] == 'Stop':
        #     # global session_id
        #     print(response)
        #     print('Stop Message')
        #     print(msg)
        #     data['token'] = TokensSave[int(msg[2]):][0]
        #     # pickle.dump(tokenWit,(open("tokenWit.p", "wb")))
        #     #  app.session['uid'] = 'session-' + str(datetime.datetime.now()).replace(" ", "")
        #     data['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
        #     print('new id :' + data['session'])
        #     #  pickle.dump(session_id,(open("tokenWit.p", "wb")))
        #     return tb.response(msg[1], data['token'], data['session']), data
        # else:
        return response, data
    else:
        return response,data

# def findContext(resp):
#     entities = resp['entities']
#     for x in entities:
#         if x != 'intent':
#             print('entities')
#             print(x)
#             return entities[x]

def mergeAns(response, witToken, session_id, question):
    if 'type' in response:
        action = response['type']
        if action == 'merge':
            # print(response['entities'])
            return tb.response('', witToken, session_id)
        else:
            return response
    else:
        return response

def getInformation(response):
    # print('Response in getInformation')
    # print(response)
    if 'entities' in response:

        entities = response['entities']
        out  = []

        # print(entities)
        if 'Budget' in entities and entities['Budget'][0]['confidence'] > 0.8:
            out.append(['Budget', entities['Budget'][0]['value']])
        if 'Gender' in entities and entities['Gender'][0]['confidence'] > 0.8:
            out.append(['Gender', entities['Gender'][0]['value']])
        if 'distinction' in entities and entities['distinction'][0]['confidence'] > 0.8:
            out.append(['distinction', entities['distinction'][0]['value']])
        return out
    else:
        return []

def getResponse(recipient, text, data):
  response, data = findAnswer(tb.response(text, data['token'], data['session']),text,data['token'],data)
  information = getInformation(response)
  for x in information:
      data['data'][x[0]] = x[1]
  print(text)
  return response, data

def allValues(dictionary, ans = []):
    for k,v in dictionary.items():
        if isintance(v,dict):
            ans.append(allValues(v)
        else:
            ans.append(v)
            return ans

def send_message(token, recipient, text, data):
  # witToken = pickle.load( open( "tokenWit.p", "rb" ) )
  """Send the message text to recipient with id recipient.
  """
  response, data = getResponse(recipient, text, data)
  if response['type'] == 'stop' or response['msg'] == data['oldmessage']:
    #   response,data = findAnswer(tb.response(text, data['token'], data['session']),text,data['token'],data)
    #   if response['type'] == 'stop':
      data['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
      print('new id :' + data['session'])
      oldToken = data['token']
      Stage = get_keys(Tokens, oldToken)[0]
      if TokenStages.index(Stage) < len(TokenStages):
          NextStage = TokenStages[TokenStages.index(Stage)+1]
          data['token'] = Tokens[NextStage][random.choice(Tokens[NextStage].keys())]
          if isinstance(data['token'], dict):
              data['token'] = random.choice(allValues(data['token']))
          token = data['token']
          response, data = getResponse(recipient, text, data)
      else:
          print('end of conversation')

  # personality, sentiment = getIt()
  # print(pprint.pprint(personality))
  # print(response)
  if 'msg' in response:
      data['oldmessage'] = response['msg']
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
        #   print(response)
          r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
              "recipient": {"id": recipient},
              "message": {"text": response['msg'].decode('unicode_escape')}
            }),
            headers={'Content-type': 'application/json'})
          if r.status_code != requests.codes.ok:
            print r.response
    #   print(response['msg'])
    #   print(data['data'])
      if response['msg'] == 'Bedankt!':
        output = mg.findByTrinity(data['data']['Gender'].lower().split(' ')[1] ,data['data']['Budget'].lower().split(' ')[0],int(data['data']['Budget'].lower().split(' ')[2]),8)
        output = output.split('<br>')
        speelgoed = []
        for x in output:
            x = x.split(',')
            # print(x)
            if len(x[-1]) > 16 and len(speelgoed) < 6:
                speelgoed.append([x[0],x[-1]])
            # print(len(x))

            # speelgoed.append(x[0] + ' voor maar ' + x[2] + ' euro.')
        messages = ['Zocht u een kado voor ' + data['data']['Gender'].lower() + ' voor ' + data['data']['Budget'].lower() + '?',
        'Dan bent u vast op zoek naar deze kadootjes:']
        messages.extend(speelgoed)
        messages.append('En tot de volgende keer')
        # print(message)
        data['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
        print('new id :' + data['session'])
        data['oldmessage'] = messages[-1]
        for message in messages:
            if isinstance(message,unicode) or isinstance(message,str):

                r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                params={"access_token": token},
                data=json.dumps({
                  "recipient": {"id": recipient},
                  "message": {"text": message.decode('unicode_escape')}
                }),
                headers={'Content-type': 'application/json'})
                if r.status_code != requests.codes.ok:
                  print r.text
            else:
                r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                params={"access_token": token},
                data=json.dumps({
                  "recipient": {"id": recipient},
                  "message": {"text": message[0].decode('unicode_escape')}
                }),
                headers={'Content-type': 'application/json'})
                if r.status_code != requests.codes.ok:
                  print r.response
                image = message[1].split('"')[1]
                r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                params={"access_token": token},
                data=json.dumps({
                  "recipient": {"id": recipient},
                  "message":{
                            "attachment":{
                              "type":"image",
                              "payload":{
                                "url":image
                              }
                            }
                          }}),
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
