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
Tokens['Start']['New']['Introduce'] = {"Ja": 'D7JHYWLOPGPFHJRCHPWC7DBCBEK2G7RZ'}
Tokens['Start']['New']['Sinterklaas'] = {"Ja": 'TT4U2XJYSY6EZBUKIBGAJPHDNWDZVGVL'}
Tokens['Start']['New']['Story'] = {"Ja": 'JW4QZSHW2GXLJKZEGPH6ZFOOP6PBYTKL'}
Tokens['Start']['New']['Open'] = {"Ja": 'POPSPV3EUB7L3W56K4FOU7ZIMFMFKDRP'}
Tokens['Start']['New']['loose'] = {"Ja": '6YY3HTLYKJG4HJOMEDPQ4BTUBA262SCY'}
Tokens['Start']['longText'] = {"Ja": 'YZDGTRUDQU7H2BPRCWFIEVU4KSL42IK4'}
Tokens['Start']['Old'] = {}
Tokens['Start']['Old']['recognized'] = {"Ja": 'IZ5AIDU7KEVIXG6RAWEOY4W6664XGX3R'}
Tokens['Start']['Old']['oldFashioned'] = {"Ja": 'Z4NCJN2J2CJGNBVW64WQULIWCUD54HMB'}
Tokens['Start']['Old']['longText'] = {"Ja": 'YZDGTRUDQU7H2BPRCWFIEVU4KSL42IK4'}
Tokens['Start']['Old']['sintQuestioning'] = {"Ja": 'DNYI3O6EHFJ376YACLJSDCB3U7H7MXDB'}
Tokens['GiveIdea'] = {}
Tokens['GiveIdea']['Ja'] = {"Ja":'GI53VC6SX2EPKWUHYOC2MSEIZMZORHFG'}
Tokens['GiveIdea']['Nee'] = {"Nee":'4YK2BMAEKCDX2RVSRJLM22NALZL2TU33'}
Tokens['decisions'] = {}
Tokens['decisions']['age'] = {}
Tokens['decisions']['gender'] = {}
Tokens['decisions']['budget'] = {}
Tokens['decisions']['age']['findage1'] =  {"Age":'BQDMM2HIB7YSAXICR7QFULGKXQWJHKXJ'}
Tokens['decisions']['age']['findage2'] =  {"Age":'5UTS7JO3NPTOHD52HAWKQOZBUNTFC53R'}
Tokens['decisions']['gender']['findgender1'] =  {"Gender":'BBEESH7AOGULQK6L3TPYYRC4L4Y36LHH'}
Tokens['decisions']['gender']['findgender2'] =  {"Gender":'UQVGOAZSC54YYVUGHURXHY5I4U6A2X3M'}
Tokens['decisions']['budget']['findbudget1'] =  {"budget":'IJ7PMHQPAVNK6UU3C3BE3NOVXZ6MMPOJ'}
Tokens['decisions']['budget']['findbudget2'] =  {"budget":'TB4QZIZYN4AZQPHYMWDCNFVOR3MJRUGI'}
Tokens['presentchoosing'] = {}
Tokens['presentchoosing']['present'] = {}
Tokens['presentchoosing']['present']['normal'] = {"Suggest":'5YVSD6XFV4I3Q457C56YRYLED5Q6E6ZK'}
Tokens['presentchoosing']['present']['discount'] = {"Suggest Discount":'RNZHGD6QHWG6JOZF66W52XHU364H4B6Y'}
Tokens['presentchoosing']['present']['loyal'] = {"Suggest loyal":'COHIUFQKSQMSGK6SNFLDR6D74CWZIJLZ'}
# Tokens['presentchoosing']['notFound'] = {}
# Tokens['presentchoosing']['notFound']['stop1'] = {"budget":'B6ZPCLQVJDDKKRNXQFF2HFWF2LZJ27KT'}
# Tokens['presentchoosing']['notFound']['stop2'] = {"budget":'I376WUKZF6BKKUP2I3LQ4CTGF5UBYAOM'}
# Tokens['presentchoosing']['notFound']['popular'] = {"budget":'BQ44V4L72VQKETN5DRE7NKPMDPVJ276C0'}
# Tokens['presentchoosing']['notFound']['keyword1'] = {"budget":'YPRANRJYCS4VPLXM3RZBOZA7V4R73TDY'}
# Tokens['presentchoosing']['notFound']['keyword2'] = {"budget":'5CJ4C7UWBRIVLERLIU5XEMUN3WDUUM3H'}
Tokens['feedback'] = {}
Tokens['feedback']['feedback1'] = {"Feedback":'Z7V53U4LAVY3JWEU6B32ZYBXK4SK6OEJ'}
Tokens['feedback']['feedback2'] = {"Feedback":'6ZUZHBITRTWR3PEJE26DZE6ZX3HHGGES'}

# startmessage = {
#         'D7JHYWLOPGPFHJRCHPWC7DBCBEK2G7RZ':
# }





TokenStages = ['Start','GiveIdea','decisions', 'presentchoosing', 'feedback']

tokenWit = 'D4CRSEOIOCHA36Y2ZSQUG7YUCUK3BJBS'
pickle.dump(tokenWit, (open("tokenWit.p", "wb")))

# returns = ['Hallo, ik ben Spot, de chatbot van Spotta! Waar kan ik u mee helpen?', 'Hallo daar, ik ben Sinterklaas. Zullen wij samen op zoek gaan naar het juiste kadootje?', ['Kent u het verhaal over Sinterklaas en het verloren kadootje?', ],
#                     'Welcome back, why are you in this screen?', 'Hi, welcombe back in the Sinterklaas chat! Bent u weer op zoek naar een kado?', 'Goedendag, ik zie dat u ons weer gevonden heeft! Kan ik u helpen met het vinden van een kadootje?',
#                     "Sorry, ik houd niet zo van die lange antwoorden. Ik stel voor om er nog eens rustig overheen te gaan. Bent u op zoek naar een kado?"]

#VERLORENKADOOTJE ID ##
# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
PAT = 'EAAEkTt8L730BAEsnAA5irYU48u4v83NZBVHFluAGNhTzJXeNMZBRdmUNohTxJ92qYGlxq6PYXc7NuF8kZBCI1QMW8aWEPESMRTKXM3NjgnQZB3nK2Ct5IBsEorZBZB47JE6cv9X1KuuZBPOAKKzsdHnYp3ShKYhldpbpeklc6MybwZDZD'
# EAAEkTt8L730BAEsnAA5irYU48u4v83NZBVHFluAGNhTzJXeNMZBRdmUNohTxJ92qYGlxq6PYXc7NuF8kZBCI1QMW8aWEPESMRTKXM3NjgnQZB3nK2Ct5IBsEorZBZB47JE6cv9X1KuuZBPOAKKzsdHnYp3ShKYhldpbpeklc6MybwZDZD'
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
  r = requests.post("https://graph.facebook.com/v2.6/me/thread_settings",
    params={"access_token": token},
    data=json.dumps({
          "setting_type":"call_to_actions",
          "thread_state":"new_thread",
          "call_to_actions":[
            {
              "payload":"USER_DEFINED_PAYLOAD"
            }
          ]
        }),
    headers={'Content-type': 'application/json'})
  if r.status_code != requests.codes.ok:
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


def typing(opt, token, recipient):
    if opt == 'on':
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": token},
        data=json.dumps({
                    "recipient":{
                    "id":recipient
                    },
                    "sender_action":"typing_on"
                    }),
        headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            print r.text
    if opt == 'off':
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": token},
        data=json.dumps({
                    "recipient":{
                    "id":recipient
                    },
                    "sender_action":"typing_off"
                    }),
        headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            print r.text

@app.route('/', methods=['POST'])
def handle_messages():
  # print "Handling Messages"
  payload = request.get_data()
  global user_data
  # print('message events')
  for sender, message in messaging_events(payload):
    # presentlist = mg.findByTrinityRange('Jongen',35, 45,9)
    # print(type(presentlist))
    # print(presentlist)
    # presents = random.sample(mg.findByTrinityRange('Jongen',35, 45,9),5)
    # print(type(presents))
    # print(presents)
    # print(presents[0])
    if sender in user_data:
        if user_data[sender]['log'] == 'end':
            user_data[sender]['log'] = {}
            user_data[sender]['log']['text'].update(user_data[sender]['text'])
            user_data[sender]['log']['feedback'].update('')
            user_data[sender]['log']['presents'].update('')
            user_data[sender]['Stage'] = TokenStages[0]
            user_data[sender]['text'] = []
            user_data[sender]['oldincoming'] = ''
            user_data[sender]['token'] = Tokens['Start']['New'][random.choice(Tokens['Start']['New'].keys())].values()[0]
            user_data[sender]['starter'] = ''
            user_data[sender]['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
            user_data[sender]['data'] = {}

        print("Incoming from %s: %s" % (sender, message))
        print(sender, message)
        if message != user_data[sender]['oldincoming']:
            print(message, user_data[sender]['oldincoming'])
            user_data[sender]['text'].append(('user',message))
            typing('on', PAT, sender)
            send_message(PAT, sender, message,user_data[sender])
            user_data[sender]['oldincoming'] = message
    else:
        makeStartScreen(PAT)
        user_data[sender] = dict()
        user_data[sender]['log'] = {}
        user_data[sender]['log']['text']= {}
        user_data[sender]['log']['feedback']= {}
        user_data[sender]['log']['presents']= {}
        user_data[sender]['Stage'] = TokenStages[0]
        user_data[sender]['text'] = []
        user_data[sender]['personality'] = ''
        user_data[sender]['oldincoming'] = ''
        user_data[sender]['oldmessage'] = ''
        user_data[sender]['token'] = Tokens['Start']['New'][random.choice(Tokens['Start']['New'].keys())].values()[0]
        user_data[sender]['starter'] = ''
        user_data[sender]['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
        user_data[sender]['data'] = {}
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
  if "messaging" in data["entry"][0]:
      messaging_events = data["entry"][0]["messaging"]
      for event in messaging_events:
        if "message" in event and "text" in event["message"] and 'is_echo' not in event["message"]:
          yield event["sender"]["id"], event["message"]["text"].encode('unicode_escape')
        # if 'postback' in payload['entry'][0]['messaging'][0]:
        #   yield event["sender"]["id"], 'Get started'

def findAnswer(response, question,witToken,data):
    session_id = data['session']
    information = getInformation(response)
    response = mergeAns(response, witToken, session_id, question)
    information.update(getInformation(response))
    return response,data, information

def mergeAns(response, witToken, session_id, question):
    if 'type' in response:
        action = response['type']
        if action == 'merge':
            return tb.response('', witToken, session_id)
        else:
            return response
    else:
        return response


def replace_value_with_definition(key_to_find, definition, current_dict):
    for key in current_dict.keys():
        if key == key_to_find:
            current_dict[key] = definition
    return current_dict

def getInformation(response):
    print(response)
    if 'entities' in response:
        entities = response['entities']
        out  = {}
        if 'hobby' in entities:
            for x in entities['hobby']:
                if x['confidence'] > 0.8:
                    out['hobby'] =  x['value']
        if 'product' in entities:
            for x in entities['product']:
                if x['confidence'] > 0.8:
                    out['product'] =  x['value']
        if 'amount_of_money' in entities and entities['amount_of_money'][0]['confidence'] > 0.8:
            out['budget'] =  abs(entities['amount_of_money'][0]['value'])
        if 'Gender' in entities and entities['Gender'][0]['confidence'] > 0.8:
            out['Gender'] = entities['Gender'][0]['value']
        if 'age_of_person' in entities and entities['age_of_person'][0]['confidence'] > 0.8:
            out['Age'] = entities['age_of_person'][0]['value']
        if 'distinction' in entities and entities['distinction'][0]['confidence'] > 0.8 and entities['distinction'][0]['value'] in ['Ja', 'Nee']:
            out['distinction'] = entities['distinction'][0]['value']
        return out
    else:
        return []

def getResponse(recipient, text, data):
  response = tb.response(text, data['token'], data['session'])
  if 'msg' not in response:
      response, data, information = findAnswer(response,text,data['token'],data)
      data['data'].update(information)
  information = getInformation(response)
  data['data'].update(information)
  return response, data

def allValues(dictionary):
    ans = []
    for k,v in dictionary.items():
        if isinstance(v,dict):
            ans.extend(allValues(v))
        else:
            ans.append(v)
    return ans

def checksuggest(token, recipient, data):
    print('in checksuggest' + data['Stage'])
    if data['Stage'] == 'presentchoosing':
        print('giving presents')
        print(data['data'])
        final_data = data['data']
        geslacht = final_data['Gender']
        budget = (final_data['budget'])
        print(budget)
        jaar = str(final_data['Age']).split(' ')[0]
        presentstasks = random.sample(mg.findByTrinityRange(geslacht,35, 45,jaar),5)
        if 'product' in data:
            presentsproduct = [findArticlesTitleAndDescription(x) for x in data['data']['product']]
            presentsproduct = list(set([item for sublist in presentsproduct for item in sublist]))
        if 'hobby' in data:
            presentshobby = [findArticlesTitleAndDescription(x) for x in data['data']['product']]
            presentshobby = list(set([item for sublist in presentshobby for item in sublist]))
        final_present = presentsproduct + presentshobby + presentstasks
        final_present = list(set(final_present))

        print(presents[0])
        # print(type(presents))
        # print(presents)
        # print(presents[0])
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": token},
        data=json.dumps({
          "recipient":{"id": recipient},
          "message":{
            "attachment":{
              "type":"template",
              "payload":{
                "template_type":"generic",
                "elements":[
                  {
                    "title":x['title'],
                    "item_url":"http://www.intertoys.nl/eastpak-padded-pak-r-rugtas-rood",
                    "image_url":x['img_link'],
                    "subtitle":x['description'],
                    "buttons":[
                      {
                        "type":"web_url",
                        "url": "https://www.spotta.nl/folders/intertoys?fid=1&page=" + str(x['page']),
                        "title":"View Website"
                      }
                    ]
                  }
                for x in presents]
              }
            }
          }
        }),
        headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            print r.text

def findToken(recipient, data, text):
  data['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
  oldToken = data['token']
  Stage = get_keys(Tokens, oldToken)[0]
  NextStage = TokenStages[TokenStages.index(Stage)+1]
  print(data['data'])
  print((k in data['data'] for k in ['budget', 'Age', 'Gender']))
  if Stage == 'decisions' and all(k in data['data'] for k in ['budget', 'Age', 'Gender']):
      print('next')
      data['token'] = random.choice(allValues(Tokens[Stage]))
      while get_keys(Tokens, data['token'])[-1] in data['data']:
          data['token'] = random.choice(allValues(Tokens[Stage]))
      data['starter'] = get_keys(Tokens, data['token'])[-1]
  elif Stage == 'Start':
      data['Stage'] = NextStage
      print(data['data'])
      if 'distinction' in data['data'] and text.lower() == 'ja':
          data['token'] = Tokens['GiveIdea']['Ja'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
      else:
          data['token'] = Tokens['GiveIdea']['Nee'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
  elif TokenStages.index(Stage) < len(TokenStages)-1:
      data['token'] = random.choice(allValues(Tokens[NextStage]))
      if isinstance(data['token'], dict):
          data['token'] = random.choice(allValues(Tokens[NextStage]))
          data['starter'] = get_keys(Tokens, data['token'])[-1]
      data['Stage'] = NextStage
  else:
      print('end of conversation')
      data['log'] = 'end'
      response = {}
  response, data = getResponse(recipient, data['starter'], data)
  return response, data

def send_message(token, recipient, text, data):
  """Send the message text to recipient with id recipient.
  """
  global user_data
  response, data = getResponse(recipient, text, data)
  if response['type'] == 'stop' or response['msg'] == data['oldmessage']:
      response, data = findToken(recipient, data, text)
  checksuggest(token, recipient, data)
  if 'msg' in response:
      print(response['msg'].decode('unicode_escape'))
      typing('off', token, recipient)
      data['text'].append(('bot',response['msg']))
      data['oldmessage'] = response['msg']
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
            print r.text
      else:
          r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
              "recipient": {"id": recipient},
              "message": {"text": response['msg'].decode('unicode_escape')}
            }),
            headers={'Content-type': 'application/json'})
          if r.status_code != requests.codes.ok:
            print r.text
  user_data[recipient] = data
  pickle.dump(user_data, open('user_data.p', 'wb'))

if __name__ == '__main__':

  # personality, sentiment = getIt()


  app.run()
