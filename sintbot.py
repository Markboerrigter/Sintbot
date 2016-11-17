from flask import Flask, request
import json
import requests
import sys
from wit import Wit
import talkBot as tb
# from runLogin import getIt
import pickle
import random
import datetime
import mongo as mg
import pprint
from copy import copy
import pickle
from flask import g
import time
import os
# Number of presented articles

childTypes = mg.findConfig(18)
TokenStages = mg.findConfig(19)
responsemessage = mg.findConfig(20)
presentmessage1 = mg.findConfig(21)
presentmessage3 = mg.findConfig(22)
personalitymessages = mg.findConfig(23)
faulwords = mg.findConfig(24)
Tokens = mg.findConfig(25)
Triggers = mg.findConfig(50)
startmessage = mg.findConfig(51)
chitchat = mg.findConfig(52)
TriggerPhrases = Triggers['tigger']
TriggerCats = Triggers['answers']

app = Flask(__name__)

channel = 'sintbot'
if channel == 'sintbot':
    dashbotAPI, PAT, N = os.environ['dashbotAPI'], os.environ['PAT1'], int(os.environ['N'])
else: dashbotAPI, PAT, N = os.environ['dashbotAPI'], os.environ['PAT2'], int(os.environ['N'])

""" FORMULAS ON TEXT PROCESSING

Below you find all formulas needed to preprocess and process the message,
dictionaries and other data sets.
"""

def findword(string):
    string = string.lower()
    if True in [x in faulwords for x in string.split()]:
        return True
    else:
        return False

def triggered(message, sender):
    message = message.lower()
    if message in traverse(TriggerPhrases):
        i = find(message,TriggerPhrases)
        reaction = random.choice(TriggerCats[i])
        time.sleep(1.5)
        typing('off', PAT, sender)
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": PAT},
        data=json.dumps({
          "recipient": {"id": sender},
          "message": {"text": reaction}
        }),
        headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
        	print r.text
        return True
    else: return False

def find(target,L):
    for i,lst in enumerate(L):
        for j,color in enumerate(lst):
            if color == target:
                return i
    return None

def get_keys(d,target):
    result = []
    path = []
    get_key(d,target, path, result)
    return result[0]

def traverse(o, tree_types=(list, tuple)):
    if isinstance(o, tree_types):
        for value in o:
            for subvalue in traverse(value, tree_types):
                yield subvalue
    else:
        yield o

def allValues(dictionary):
    ans = []
    for k,v in dictionary.items():
        if isinstance(v,dict):
            ans.extend(allValues(v))
        else:
            ans.append(v)
    return ans

def mergedicts(L):
    intersect = []
    for item in L[0]:
        x = [True for y in L[0:] if item in y]
        if len(x) == len(L):
            intersect.append(item)
    return intersect

def findValue(L,d):
	for x in L:
		d = d[x]
	return d

def findNo(L):
	num = L.count('Nee')
	if num == 0:
		pers = 'Extraverion'
	elif num == 1:
		pers = 'Agreebableness'
	elif num == 2:
		pers = 'Openess'
	elif num == 3:
		pers = 'Conciousness'
	elif num == 4:
		pers = 'Default'
	return pers

def get_key(d, target, path, result):
    for k, v in d.iteritems():
        path.append(k)
        if isinstance(v, dict):
            get_key(v, target, path, result)
        if v == target:
            result.append(copy(path))
        path.pop()

def replace_value_with_definition(key_to_find, definition, current_dict):
    for key in current_dict.keys():
        if key == key_to_find:
            current_dict[key] = definition
    return current_dict

def word_feats(words):
    return dict([(word, True) for word in words])

""" FORMULAS TO MAKE CALLS TO FACEBOOK/DASHBOT

below all functions that make calls to dashbot and facebook to extract
or write data can be found.

"""

def makeStartScreen(token):
  r = requests.post("https://graph.facebook.com/v2.6/me/thread_settings",
    params={"access_token": token},
    data=json.dumps({
          "setting_type":"call_to_actions",
          "thread_state":"new_thread",
          "call_to_actions":[
            {
              "payload":"START"
            }
          ]
        }),
    headers={'Content-type': 'application/json'})
  if r.status_code != requests.codes.ok:
    print r.text

@app.route('/', methods=['GET'])
def verify():
    if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.challenge'):
        if not request.args.get('hub.verify_token') == os.environ['FB_VERIFY_TOKEN']:
            return 'Verification token mismatch', 403
        return request.args['hub.challenge'], 200
    return 'Hello world', 200

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

def postdashbot(id, payload):
  if id == 'human':
      print('send to dashbot ')
      r = requests.post("https://tracker.dashbot.io/track?platform=facebook&v=0.7.4-rest&type=incoming&apiKey=" + dashbotAPI,
        data=payload,
        headers={'Content-type': 'application/json'})
      if r.status_code != requests.codes.ok:
        print r.text
  if id == 'bot':
      print('send botshit to dashbot ')
      r = requests.post("https://tracker.dashbot.io/track?platform=facebook&v=0.7.4-rest&type=outgoing&apiKey=" + dashbotAPI,
        data=json.dumps({"qs":{"access_token":PAT},"uri":"https://graph.facebook.com/v2.6/me/messages","json":{"message":{"text":payload[1]},"recipient":{"id":payload[0]}},"method":"POST","responseBody":{"recipient_id":payload[0],"message_id":payload[2]}}),
        headers={'Content-type': 'application/json'})
      if r.status_code != requests.codes.ok:
        print r.text

# @app.route('/', methods=['GET'])
# def handle_verification():
#   print "Handling Verification."
#   if request.args.get('hub.verify_token', '') == 'my_voice_is_my_password_verify_me':
#     print "Verification successful!"
#     return request.args.get('hub.challenge', '')
#   else:
#     print "Verification failed!"
#     return 'Error, wrong validation token'

def getdata(id):
    return requests.get('https://graph.facebook.com/v2.6/'+ id+ '?fields=first_name,last_name,profile_pic,locale,timezone,gender&access_token=' + PAT).text

""" FUNCTIONS TO RETRIEVE THE REIGHT ANSWER FROM WIT.AI.

below all functions that talk with wit.ai or search for a token are found.
"""

def mergeAns(response, witToken, session_id, question):
    if 'type' in response:
        action = response['type']
        if action == 'merge':
            return tb.response('', witToken, session_id)
        else:
            return response
    else:
        return response

def getInformation(response, tekst):
    feedback = tekst
    x = 0
    out  = {}
    if feedback == '\U0001f600':
        x = '5'
    if feedback == '\U0001f60a':
        x = '4'
    if feedback == '\U0001f610':
        x = '3'
    if feedback == '\U0001f614':
        x = '2'
    if feedback == '\U0001f620':
        x = '1'
    if int(x) > 0:
        out['Feedback'] = x
    if 'entities' in response:
        entities = response['entities']

        if 'hobby' in entities:
            for x in entities['hobby']:
                if x['confidence'] > 0.8:
                    out['hobby'] =  x['value']
        if 'product' in entities:
            for x in entities['product']:
                if x['confidence'] > 0.8:
                    out['product'] =  x['value']
        if 'budget' in entities and entities['budget'][0]['confidence'] > 0.8:
            out['budget'] = entities['budget'][0]['value']
        if 'Gender' in entities and entities['Gender'][0]['confidence'] > 0.8:
            out['Gender'] = entities['Gender'][0]['value']
        if 'age_of_person' in entities and entities['age_of_person'][0]['confidence'] > 0.8:
            out['Age'] = entities['age_of_person'][0]['value']
        if 'typeChild' in entities and entities['typeChild'][0]['confidence'] > 0.8:
            out['typeChild'] = entities['typeChild'][0]['value']
        if 'distinction' in entities and entities['distinction'][0]['confidence'] > 0.8 and entities['distinction'][0]['value'] in ['Ja', 'Nee']:
            out['distinction'] = entities['distinction'][0]['value']
        # if 'Feedback' in entities and entities['Feedback'][0]['confidence'] > 0.6:
        #     out['Feedback'] = entities['Feedback'][0]['value']
    return out

def findAnswer(response, question,witToken,data):
    session_id = data['session']
    information = getInformation(response,question)
    response = mergeAns(response, witToken, session_id, question)
    information.update(getInformation(response,question))
    return response,data, information

def getResponse(recipient, text, data):
  response = tb.response(text, data['token'], data['session'])
  if 'msg' not in response:
      response, data, information = findAnswer(response,text,data['token'],data)
      data['data'].update(information)
  information = getInformation(response, text)
  data['data'].update(information)
  mg.updateUser(recipient, data)
  return response, data

def getFeedback(data):
    feedback = data['data']['Feedback']
    if feedback == '\U0001f600':
        return '5'
    if feedback == '\U0001f60a':
        return '4'
    if feedback == '\U0001f610':
        return '3'
    if feedback == '\U0001f614':
        return '2'
    if feedback == '\U0001f620':
        return '1'


def checksuggest(token, recipient, data,n):
    if data['Stage'] == 'presentchoosing':
        if 'Gender' not in data['data']:
            data['secondchoice'] = True
            presents = data['presentFound']
            data['presents'] = presents
            print('direct')
        else:
            final_data = data['data']
            if len(final_data['Gender'].split())>1:
                geslacht = final_data['Gender'].split(' ')[1]
            else: geslacht = final_data['Gender']
            budget = (final_data['budget']).split('-')
            age = str(final_data['Age']).split(' ')[0]
            category = data['data']['type']
            if 'product' in final_data:
                idea = final_data['product']
            else: idea = ''
            presents = mg.findRightProduct(geslacht, budget, age, category, idea,3*N)
            data['presents'] = [x for x in presents in x not in data['presented']]
        newpres = []
        for x in presents:
            if x['retailer'] == 'intertoys':
                x['item_url'] = "https://www.spotta.nl/folders/intertoys?fid=1&page=" + str(x['page'])
                if not  x['img_link'].startswith('http'):
                    print('no pic')
                    x.update({'img_link':'https://support.greenorange.com/sint/intertoys/'+ 'p' + str(x['page']) + '-' + str(x['article_number']) + '.png'})
            else:
                x['item_url'] = "https://www.spotta.nl/folders/bart-smit?fid=116&page=" + str(x['page'])
                if not x['img_link'].startswith('http'):
                    print('no pic')
                    x.update({'img_link':'https://support.greenorange.com/sint/bartsmit/'+ 'p' + str(x['page']) + '_' + str(x['article_number']) + '.png'})
            newpres.append(x)
        presents = newpres[:N]
        postdashbot('bot',(recipient,'presents', data['message-id']) )
        data['presented'].extend(presents)
        typing('off', PAT, recipient)
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
                    "item_url":x['item_url'],
                    "image_url":x['img_link'],
                    "subtitle":x['description'],
                    "buttons":[
                      {
                        "type":"web_url",
                        "url": x['item_url'],
                        "title":"Bekijk de folder!"

                        # "payload":'clicked ' +  str(x['article_number'])
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
    mg.updateUser(recipient, data)
    # return data

def findType(string):
    if string == "Ontdek & Verhaal":
        return ['Kleine ontdekkers', 'Verhalenmakers en superhelden']
    if string == "Zorgzaam":
        return ["Kleine papa's, mama's en dierenvriendjes"]
    if string == "Maak & Bouw":
        return ['Knutselaars', 'Bouwers en onderzoekers']
    if string == "Denk & Puzzel":
        return ['Knappe koppen en boekenwurmen', 'Spelletjesgekken en puzzelfans']
    if string == "Sport& Stunt":
        return ['Sporters, stunters en stoere kids']
    if string == "Race & Rock":
        return ['Razende racers en stoere stuurders', 'Rocksterren en stijliconen']
    if string == "Tech & Game":
        return ['Gadget en gamekings']
    else:
        return ''


def findToken(recipient, data, text):
  data['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
  oldToken = data['token']
  Stage = data['Stage']
  if data['Stage'] == 'bridge':
      if text.lower() == 'ja':
          typing('on', PAT, recipient)
          NextStage = TokenStages[TokenStages.index(Stage)+1]
          data['token'] = random.choice(allValues(Tokens[NextStage]))
          data['oldmessage'] = ''
          if isinstance(data['token'], dict):
              data['token'] = random.choice(allValues(Tokens[NextStage]))
              data['starter'] = get_keys(Tokens, data['token'])[-1]
          data['Stage'] = NextStage
          mg.updateUser(recipient, data)
        #   response, data = getResponse(recipient, data['starter'], data)
          send_message(PAT, recipient, data['starter'], data)
      else:
          message = random.choice(['Oke, dan gaan we samen op zoek!', 'Ah, oke! Daarom ben ik er he!', 'Dat is niet erg;) We gaan samen wat vinden!'])
          data['text'].append(('bot',message))
          data['oldmessage'] = message
          postdashbot('bot',(recipient,message, data['message-id']) )
          typing('off', PAT, recipient)
          r = requests.post("https://graph.facebook.com/v2.6/me/messages",
          params={"access_token": PAT},
          data=json.dumps({
          "recipient": {"id": recipient},
          "message": {"text": message}
          }),
          headers={'Content-type': 'application/json'})
        #   data['oldmessage'] = message
          if r.status_code != requests.codes.ok:
          	print r.text
          typing('on', PAT, recipient)
          time.sleep(1)
          NextStage = TokenStages[TokenStages.index(Stage)+2]
          data['token'] = random.choice(allValues(Tokens[NextStage]))
          if isinstance(data['token'], dict):
              data['token'] = random.choice(allValues(Tokens[NextStage]))
              data['starter'] = get_keys(Tokens, data['token'])[-1]
          data['Stage'] = NextStage
          mg.updateUser(recipient, data)
        #   print(NextStage)
        #   response, data = getResponse(recipient, data['starter'], data)
          send_message(PAT, recipient, data['starter'], data)
  elif Stage == 'feedback':
      NextStage = TokenStages[TokenStages.index(Stage)+1]
      data['Stage'] = NextStage
      response = {}
      mg.updateUser(recipient, data)
      send_message(PAT, recipient, '', data)
  elif Stage == 'Connection':
      if not data['personality']:
          NextStage = TokenStages[TokenStages.index(Stage)+1]
          data['Stage'] = NextStage
          response = {}
          mg.updateUser(recipient, data)
          send_message(PAT, recipient, '', data)
      else:
          NextStage = TokenStages[TokenStages.index(Stage)+2]
          data['Stage'] = NextStage
          response = {}
          mg.updateUser(recipient, data)
          send_message(PAT, recipient, 'we weten de persoonlijkheid al', data)
  elif Stage == 'GiveIdea':
      products = mg.findArticlesTitle(text)[:6]
      message = random.choice(['Goed dat je het al weet!','Wat een leuk idee!', 'Ah oke, dat klinkt heel leuk!'])
      data['text'].append(('bot',message))
      data['oldmessage'] = message
      postdashbot('bot',(recipient,message, data['message-id']) )
      typing('off', PAT, recipient)
      r = requests.post("https://graph.facebook.com/v2.6/me/messages",
      params={"access_token": PAT},
      data=json.dumps({
      "recipient": {"id": recipient},
      "message": {"text": message}
      }),
      headers={'Content-type': 'application/json'})
      if r.status_code != requests.codes.ok:
        print r.text
      time.sleep(1)
      #   for x in products:
    #       print(x['title'])
      if products:
        message = random.choice(['Ik heb het zelfs al gevonden!', 'Ik zie het al staan!'])
        data['text'].append(('bot',message))
        data['oldmessage'] = message
        postdashbot('bot',(recipient,message, data['message-id']) )
        typing('off', PAT, recipient)
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": PAT},
        data=json.dumps({
        "recipient": {"id": recipient},
        "message": {"text": message}
        }),
        headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
          print r.text
        NextStage = 'presentchoosing'
        data['presentFound'] = (products)
        # data['token'] = random.choice(allValues(Tokens[NextStage]))
        data['Stage'] = NextStage
        response = {}
        mg.updateUser(recipient, data)
        # send_message(PAT, recipient, '', data)
      else:
          NextStage = TokenStages[TokenStages.index(Stage)+1]
          data['token'] = random.choice(allValues(Tokens[NextStage]))
          if isinstance(data['token'], dict):
              data['token'] = random.choice(allValues(Tokens[NextStage]))
              data['starter'] = get_keys(Tokens, data['token'])[-1]
          message = random.choice(['Ik wil graag nog wat andere dingen weten om zeker te zijn wat je zoekt!', 'Ik vraag me nog wat andere dingen af!', 'Ik heb nog wat andere vraagjes.'])
          data['Stage'] = NextStage
          data['text'].append(('bot',message))
          data['oldmessage'] = message
          postdashbot('bot',(recipient,message, data['message-id']) )
          typing('off', PAT, recipient)
          r = requests.post("https://graph.facebook.com/v2.6/me/messages",
          params={"access_token": PAT},
          data=json.dumps({
          "recipient": {"id": recipient},
          "message": {"text": message}
          }),
          headers={'Content-type': 'application/json'})
          if r.status_code != requests.codes.ok:
          	print r.text
          mg.updateUser(recipient, data)
    #   response, data = getResponse(recipient, data['starter'], data)
      send_message(PAT, recipient, data['starter'], data)
  elif Stage == 'decisions':
      if not all(k in data['data'] for k in ['budget', 'Age', 'Gender', 'type']):
          data['token'] = random.choice(allValues(Tokens[Stage]))
          while get_keys(Tokens, data['token'])[-1] in data['data']:
              data['token'] = random.choice(allValues(Tokens[Stage]))
          data['starter'] = get_keys(Tokens, data['token'])[-1]
          mg.updateUser(recipient, data)
          send_message(PAT, recipient, data['starter'], data)
      else:
          NextStage = TokenStages[TokenStages.index(Stage)+1]
          data['Stage'] = NextStage
          response = {}
          mg.updateUser(recipient, data)
          send_message(PAT, recipient, '', data)
  elif Stage == 'Personality':
      Nextstage = TokenStages[TokenStages.index(Stage)+1]
      data['Stage'] = Nextstage
      if set(data['personality'][1:]) == set(['Geven', 'Surprise']):
          data['token'] = Tokens[Nextstage]['1'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
      elif set(data['personality'][1:]) == set(['Geven', 'Gedichtje']):
          data['token'] = Tokens[Nextstage]['2'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
      elif set(data['personality'][1:]) == set(['Geven', 'Lezen']):
          data['token'] = Tokens[Nextstage]['3'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
      elif set(data['personality'][1:]) == set(['Geven', 'Schrijven']):
          data['token'] = Tokens[Nextstage]['4'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
      elif set(data['personality'][1:]) == set(['Krijgen', 'Surprise']):
          data['token'] = Tokens[Nextstage]['5'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
      elif set(data['personality'][1:]) == set(['Krijgen', 'Gedichtje']):
          data['token'] = Tokens[Nextstage]['6'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
      elif set(data['personality'][1:]) == set(['Krijgen', 'Lezen']):
          data['token'] = Tokens[Nextstage]['7'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
      elif set(data['personality'][1:]) == set(['Krijgen', 'Schrijven']):
          data['token'] = Tokens[Nextstage]['8'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
      elif set(data['personality'][1:]) == set(['Schrijven', 'Surprise']):
          data['token'] = Tokens[Nextstage]['9'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
      elif set(data['personality'][1:]) == set(['Schrijven', 'Gedichtje']):
          data['token'] = Tokens[Nextstage]['10'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
      elif set(data['personality'][1:]) == set(['Lezen', 'Surprise']):
          data['token'] = Tokens[Nextstage]['11'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
      elif set(data['personality'][1:]) == set(['Lezen', 'Gedichtje']):
          data['token'] = Tokens[Nextstage]['12'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
      else:
          print('something went wrong')
      mg.updateUser(recipient, data)
      send_message(PAT, recipient, data['starter'], data)
  elif Stage == 'Start':
      data['type'] = text
      if text == 'Cadeauadvies':
          NextStage = TokenStages[TokenStages.index(Stage)+2]
          data['Stage'] = NextStage
          mg.updateUser(recipient, data)
          send_message(PAT, recipient, data['starter'], data)
      elif text == 'Beter leren kennen':
          NextStage = TokenStages[TokenStages.index(Stage)+1]
          while data['token'] in data['chitchat']:
              data['token'] = random.choice(allValues(Tokens[NextStage]))
              if isinstance(data['token'], dict):
                  data['token'] = random.choice(allValues(Tokens[NextStage]))
                  data['starter'] = get_keys(Tokens, data['token'])[-1]
          data['chitchat'].append(data['token'])
          data['Stage'] = NextStage
          mg.updateUser(recipient, data)
          send_message(PAT, recipient, data['starter'], data)
  # elif Stage == 'presentchoosing' and 'Gender' not in data['data']:
  #     NextStage = 'decisions'
  #     data['Stage'] = NextStage
  #     response = {}
  #     mg.updateUser(recipient, data)
  #     send_message(PAT, recipient, '', data)

  elif TokenStages.index(Stage) < len(TokenStages)-1:
      NextStage = TokenStages[TokenStages.index(Stage)+1]
      data['token'] = random.choice(allValues(Tokens[NextStage]))
      if isinstance(data['token'], dict):
          data['token'] = random.choice(allValues(Tokens[NextStage]))
          data['starter'] = get_keys(Tokens, data['token'])[-1]
      data['Stage'] = NextStage
      mg.updateUser(recipient, data)
      send_message(PAT, recipient, data['starter'], data)
  else:
      print('end of conversation')
      typing('off', PAT, recipient)
      data['dolog'] = 'end'
      response = {}
      mg.updateUser(recipient, data)

""" FUNCTIONS TO RECEIVE AND SEND MESSAGES

below the receive and send functions can be found.

"""


@app.route('/', methods=['POST'])
def handle_messages():
  payload = request.get_data()
  for sender, message, mid, recipient in messaging_events(payload) :
    try:
        print("Incoming from %s: %s" % (sender, message))
        postdashbot('human', payload)
        if not mg.findUser(sender):
            typing('on', PAT, sender)
            user_info = getdata(sender)
            data = {}
            data['info'] = user_info
            data['log'] = {}
            data['log']['text']= {'0':'first conversation'}
            data['log']['feedback']= []
            data['log']['data'] = {}
            data['log']['presents']= []
            data['dolog'] = ''
            data['secondchoice'] = False
            data['secondRow'] = False
            data['Stage'] = TokenStages[0]
            data['text'] = []
            data['track'] = ''
            data['personQuestions'] = []
            data['message-id'] = mid
            data['clicked'] = ''
            data['chitchat'] = []
            data['personality'] = []
            data['oldincoming'] = message
            data['oldmessage'] = ''
            data['presentFound'] = []
            data['intype'] = False
            data['trig'] = False
            data['presented'] = []
            data['token'] = random.choice(allValues(Tokens['Start']['New']))
            data['starter'] = ''
            data['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
            data['data'] = {}
            mg.insertUser(sender,data)
            typing('on', PAT, sender)
            data = send_message(PAT, sender, message,data)
            mg.insertUser(sender,data)
            if data['trig']:
                if text == 'Ja':
                    send_message(PAT, sender, data['oldmessage'],data)
                else:
                    typing('on', PAT, sender)
                    time.sleep(1.5)
                    typing('off', PAT, sender)
                    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                    params={"access_token": PAT},
                    data=json.dumps({
                      "recipient": {"id": sender},
                      "message": {"text": 'Oke! Toch bedankt voor het fijne gesprek en veel plezier tijdens pakjesavond!'
                    }}),
                    headers={'Content-type': 'application/json'})
                    if r.status_code != requests.codes.ok:
                    	print r.text
                    data['dolog'] = 'end'
                    mg.updateUser(recipient, data)
        else:
            data = mg.findUser(sender)
            if findword(message):
                typing('on', PAT, sender)
                time.sleep(1.5)
                typing('off', PAT, sender)
                message = 'Wij houden hier niet zo van schelden. Zou je hier alsjeblieft mee willen stoppen!.'
                data['text'].append(('bot',message))
                data['oldmessage'] = message
                postdashbot('bot',(sender,message, data['message-id']) )
                typing('off', PAT, sender)
                r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                params={"access_token": PAT},
                data=json.dumps({
                  "recipient": {"id": sender},
                  "message": {"text": message}
                }),
                headers={'Content-type': 'application/json'})
                if r.status_code != requests.codes.ok:
                	print r.text
                time.sleep(1.5)
                message = 'Wil je nu verder met het zoeken van een leuk cadeau?'
                data['text'].append(('bot',message))
                data['oldmessage'] = message
                postdashbot('bot',(sender,message, data['message-id']) )
                typing('off', PAT, sender)
                r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                params={"access_token": PAT},
                data=json.dumps({
                  "recipient": {"id": sender},
                  "message": {"text": message,
                  "quick_replies":[{
                                 "content_type":"text",
                                 "title":'Ja',
                                 "payload":'Ja'
                               },{	                "content_type":"text",
                                                  "title":'Nee',
                                                  "payload":'Nee'
                                                 }]}
                }),
                headers={'Content-type': 'application/json'})
                if r.status_code != requests.codes.ok:
                	print r.text
                data['trig'] = True
                mg.updateUser(recipient, data)
            elif message.split()[0] == 'clicked':
                data['clicked'] = message.split()[1]
            elif triggered(message, sender):
                typing('on', PAT, sender)
                print('Trigger send')
                typing('on', PAT, sender)
                time.sleep(1.5)
                message = 'Wil je nu verder met het zoeken van een leuk cadeau?'
                data['text'].append(('bot',message))
                data['oldmessage'] = message
                postdashbot('bot',(sender,message, data['message-id']) )
                typing('off', PAT, sender)
                r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                params={"access_token": PAT},
                data=json.dumps({
                  "recipient": {"id": sender},
                  "message": {"text": 'Wil je nu verder met het zoeken van een leuk cadeau?',
                  "quick_replies":[{
                                 "content_type":"text",
                                 "title":'Ja',
                                 "payload":'Ja'
                               },{	                "content_type":"text",
                                                  "title":'Nee',
                                                  "payload":'Nee'
                                                 }]}
                }),
                headers={'Content-type': 'application/json'})
                if r.status_code != requests.codes.ok:
                	print r.text
                data['trig'] = True
                mg.updateUser(recipient, data)
            elif data['trig']:
                if text == 'Ja':
                    send_message(PAT, sender, data['oldmessage'],data)
                    data['trig'] = False
                else:
                    typing('on', PAT, sender)
                    data['trig'] = False
                    time.sleep(1.5)
                    typing('off', PAT, sender)
                    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                    params={"access_token": PAT},
                    data=json.dumps({
                      "recipient": {"id": sender},
                      "message": {"text": 'Oke! Toch bedankt voor het fijne gesprek en veel plezier tijdens pakjesavond!'
                    }}),
                    headers={'Content-type': 'application/json'})
                    if r.status_code != requests.codes.ok:
                    	print r.text
                    data['dolog'] = 'end'
                    mg.updateUser(recipient, data)
            elif mid != data['message-id']:
                typing('on', PAT, sender)
                if data['dolog'] == 'end':
                    if 'Feedback' in data['data']:
                        data['log']['feedback'].append(data['data']['Feedback'])
                    else:
                        data['log']['feedback'].append('0')
                    if data['data']:
                        data['log']['data'].update(data['data'])
                    if data['presents']:
                        data['log']['presents'].append(data['presented'])
                    if data['text']:
                        data['log']['text'].update({str(max([ int(x) for x in list(data['log']['text'].keys())])+1):data['text']})
                    data['presents'] = []
                    data['Stage'] = TokenStages[0]
                    data['text'] = []
                    data['clicked'] = []
                    data['presented'] = []
                    if len (data['chitchat']) > 3:
                        data['chitchat'] = []
                    data['dolog'] = ''
                    data['trig'] = False
                    data['secondRow'] = False
                    data['presentFound'] = []
                    data['token'] = '2'
                    data['starter'] = ''
                    data['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
                    data['data'] = {}
                    data['secondchoice'] = False
                    data['intype'] = False
                    data['personQuestions'] = []
                data['text'].append(('user',message))
                data['message-id'] = mid
                data['oldincoming'] = message
                mg.updateUser(recipient, data)
                data = send_message(PAT, sender, message,data)
            mg.updateUser(recipient, data)
    except KeyboardInterrupt as e:
        data['message-id'] = mid
        data['oldincoming'] = message
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": PAT},
        data=json.dumps({
          "recipient": {"id": 1042410335857237},
          "message": {"text": str(e)
        }}),
        headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
        	print r.text
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": PAT},
        data=json.dumps({
          "recipient": {"id": sender},
          "message": {"text": 'Sorry, daar ging even iets fout'
        }}),
        headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
        	print r.text
        raise
    except Exception as e:
        print "Caught it!"
        data['message-id'] = mid
        data['oldincoming'] = message
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": PAT},
        data=json.dumps({
          "recipient": {"id": 1042410335857237},
          "message": {"text": str(e)
        }}),
        headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
        	print r.text
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": PAT},
        data=json.dumps({
          "recipient": {"id": sender},
          "message": {"text": 'Sorry, daar ging even iets fout'
        }}),
        headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
        	print r.text
        raise
  return "ok", 200

def messaging_events(payload):
  """Generate tuples of (sender_id, message_text) from the
  provided payload.
  """
  data = json.loads(payload)
  if "messaging" in data["entry"][0]:
      messaging_events = data["entry"][0]["messaging"]
      for event in messaging_events:
        if "message" in event and "text" in event["message"] and 'is_echo' not in event["message"]:
          yield event["sender"]["id"], event["message"]["text"].encode('unicode_escape'), event["message"]['mid'], event["recipient"]['id']
        if 'postback'in event:
          yield event["sender"]["id"], event["postback"]["payload"].encode('unicode_escape'), 'Postback', event["recipient"]['id']

def send_message(token, recipient, text, data):
  """Send the message text to recipient with id recipient.
  """
  a = random.choice([True,False,False,False,False,False,False])
  print('send_message', text)
  if data['dolog'] == 'end':
      print('done')
  # elif message == 'Get started' or message =='Aan de slag':
  #     data['dolog'] == 'end'
  #     mg.updateUser(recipient, data)
  elif a and data['Stage'] == 'decisions' and 'Lezen' in data['personality'] and 'Krijgen' in data['personality']:
      message = random.choice(chitchat)
      data['text'].append(('bot',message))
      data['oldmessage'] = message
      postdashbot('bot',(recipient,message, data['message-id']) )
      typing('off', PAT, recipient)
      r = requests.post("https://graph.facebook.com/v2.6/me/messages",
          params={"access_token": token},
          data=json.dumps({
            "recipient": {"id": recipient},
            "message": {"text": message}
          }),
          headers={'Content-type': 'application/json'})
      if r.status_code != requests.codes.ok:
          print r.text
  elif data['oldmessage'] == 'Weet je dit keer al wat je zoekt? :)':
      data['token'] = '1'
      findToken(recipient, data, text)
  elif data['token'] == '1' and data['Stage'] == 'decisions':
    if data['intype']:
        data['data']['type'] =  findType(text)
        findToken(recipient, data, text)
        mg.updateUser(recipient, data)
    else:
      data['intype'] = True
      message = 'Ik vroeg me nog af, welk type past het meest bij het kind?'
      data['text'].append(('bot',message))
      data['oldmessage'] = message
      postdashbot('bot',(recipient,message, data['message-id']) )
      typing('off', PAT, recipient)
      r = requests.post("https://graph.facebook.com/v2.6/me/messages",
          params={"access_token": token},
          data=json.dumps({
            "recipient": {"id": recipient},
            "message":{"text": message,
            "quick_replies":[{
                          "content_type":"text",
                          "title":x,
                          "payload":x
                        } for x in childTypes
                        ]
          }}),
          headers={'Content-type': 'application/json'})
      if r.status_code != requests.codes.ok:
          	print r.text
      mg.updateUser(recipient, data)
  elif text == 'we weten de persoonlijkheid al':
      message = 'Weet je dit keer al wat je zoekt? :)'
      data['text'].append(('bot',message))
      data['oldmessage'] = message
      data['Stage'] = 'bridge'

      postdashbot('bot',(recipient,message, data['message-id']) )
      typing('off', PAT, recipient)
      r = requests.post("https://graph.facebook.com/v2.6/me/messages",
          params={"access_token": token},
          data=json.dumps({
            "recipient": {"id": recipient},
            "message":{"text": message ,
            "quick_replies":[{
                           "content_type":"text",
                           "title":'Ja',
                           "payload":'Ja'
                         },{	                "content_type":"text",
                         	                "title":'Nee',
                         	                "payload":'Nee'
                                           }]}}),
          headers={'Content-type': 'application/json'})
      if r.status_code != requests.codes.ok:
          	print r.text
      mg.updateUser(recipient, data)
  elif data['Stage'] == 'Personality':
    if not data['personQuestions']:
        message = 'Ah, leuk!'
        data['text'].append(('bot',message))
        data['oldmessage'] = message
        postdashbot('bot',(recipient,message, data['message-id']) )
        typing('off', PAT, recipient)
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
              "recipient": {"id": recipient},
              "message":{"text": message}}),
            headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            	print r.text
        typing('on', PAT, recipient)
        time.sleep(1)
        message = 'Het grote boek van Sinterklaas kent alle kinderen, maar weet wat minder van de volwassenen.'
        data['text'].append(('bot',message))
        data['oldmessage'] = message
        postdashbot('bot',(recipient,message, data['message-id']) )
        typing('off', PAT, recipient)
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
              "recipient": {"id": recipient},
              "message":{"text": message}}),
            headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            	print r.text
        typing('on', PAT, recipient)
        message = 'Ik Gga je een aantal keuzes geven om je beter te leren kennen!'
        data['text'].append(('bot',message))
        data['oldmessage'] = message
        postdashbot('bot',(recipient,message, data['message-id']) )
        typing('off', PAT, recipient)
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
              "recipient": {"id": recipient},
              "message":{"text": message}}),
            headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            	print r.text
        mg.updateUser(recipient, data)
        time.sleep(1.5)
    else:
        data['personality'].append(text)
        mg.updateUser(recipient, data)
    if len(data['personQuestions']) > 2:
        findToken(recipient, data, text)
    else:
        message = random.choice(personalitymessages)
        while personalitymessages.index(message) in data['personQuestions']:
            message = random.choice(personalitymessages)
        data['personQuestions'].append(personalitymessages.index(message))
        data['text'].append(('bot',message))
    	data['oldmessage'] = message
    	postdashbot('bot',(recipient,message[1], data['message-id']) )
        typing('off', PAT, recipient)
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
              "recipient": {"id": recipient},
              "message":message[0]}),
            headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            	print r.text
        typing('on', PAT, recipient)
        time.sleep(1)
        typing('off', PAT, recipient)
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": token},
        data=json.dumps({
          "recipient": {"id": recipient},
          "message": {"text": message[1],
          "quick_replies":[{
                        "content_type":"text",
                        "title":message[2][0],
                        "payload":message[2][0],
                        "image_url":message[2][1]
                      },{	                "content_type":"text",
                      	                "title":message[3][0],
                      	                "payload":message[3][0],
                                        "image_url":message[3][1]}]}
        }),
        headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
        	print r.text
        	print(recipient)
        mg.updateUser(recipient, data)
  elif data['token'] == '2':
      if text == 'Oke!':
          findToken(recipient, data, text)
      else:
          message = 'Welkom terug, zullen we weer op zoek gaan naar een cadeau? :)'
          data['text'].append(('bot',message))
          data['oldmessage'] = message
          postdashbot('bot',(recipient,message, data['message-id']) )
          typing('off', PAT, recipient)
          r = requests.post("https://graph.facebook.com/v2.6/me/messages",
              params={"access_token": token},
              data=json.dumps({
                "recipient": {"id": recipient},
                "message": {"text": message.encode('utf-8'),
                "quick_replies":[{
                              "content_type":"text",
                              "title":'Oke!',
                              "payload":'Oke!'
                            }
                            ]}
              }),
              headers={'Content-type': 'application/json'})
          if r.status_code != requests.codes.ok:
              print r.text
          mg.updateUser(recipient, data)
  elif data['Stage'] == 'presentchoosing':
    if text == 'Gevonden!':
        for present in data['presents'][-3:]:
            mg.addPositive(present['article_number'],2)
        for present in data['presents'][:-3]:
            mg.addDislike(present['article_number'])
        mg.updateUser(recipient, data)
        findToken(recipient, data, text)
    elif text == 'Andere' and 'Gender' not in data['data']:
        data['Stage'] = 'bridge'
        findToken(recipient, data, text)
    elif text == 'Andere keuzes!':
        message = 'Oke, bedankt dat je zo eerlijk bent! Wat denk je hier van?'
    	data['text'].append(('bot',message))
    	data['oldmessage'] = message
    	postdashbot('bot',(recipient,message, data['message-id']) )
        typing('off', PAT, recipient)
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
              "recipient": {"id": recipient},
              "message": {"text": message.encode('utf-8')}
            }),
            headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            	print r.text
        typing('on', PAT, recipient)
        checksuggest(PAT, recipient, data,N)
        typing('on', PAT, recipient)
        time.sleep(1)
        message = random.choice(presentmessage3)
        typing('off', PAT, recipient)
        if 'budget' in data['data']:
            r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                params={"access_token": token},
                data=json.dumps({
                  "recipient": {"id": recipient},
                  "message": {"text": message,
                  "quick_replies":[{
                                "content_type":"text",
                                "title":'Andere keuzes!',
                                "payload":'Andere'
                              },
                    {
                                  "content_type":"text",
                                  "title":'Gevonden!',
                                  "payload":'Gevonden'
                                },{
                                              "content_type":"text",
                                              "title":'Andere categorie!',
                                              "payload":'Categorie'
                                            },{
                                                          "content_type":"text",
                                                          "title":'Ander bedrag!',
                                                          "payload":'bedrag'
                                                        }]}
                }),
                headers={'Content-type': 'application/json'})
            if r.status_code != requests.codes.ok:
                print r.text
        else:
                        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                            params={"access_token": token},
                            data=json.dumps({
                              "recipient": {"id": recipient},
                              "message": {"text": message,
                              "quick_replies":[{
                                            "content_type":"text",
                                            "title":'Andere keuzes!',
                                            "payload":'Andere'
                                          },
                                {
                                              "content_type":"text",
                                              "title":'Gevonden!',
                                              "payload":'Gevonden'
                                            }]}
                            }),
                            headers={'Content-type': 'application/json'})
                        if r.status_code != requests.codes.ok:
                            print r.text
        mg.updateUser(recipient, data)
    # elif text == 'Nee' and data['secondchoice']:
    #     message = 'Sorry, ik denk dat ik niet helemaal weet wat je zoekt. Je zou zelf verder kunnen zoeken in de folders. Die kun je vinden via de volgende links'
    # 	data['text'].append(('bot',message))
    # 	data['oldmessage'] = message
    # 	postdashbot('bot',(recipient,message, data['message-id']) )
    #     typing('off', PAT, recipient)
    #     r = requests.post("https://graph.facebook.com/v2.6/me/messages",
    #         params={"access_token": token},
    #         data=json.dumps({
    #           "recipient": {"id": recipient},
    #           "message":{
    #             "attachment":{
    #               "type":"template",
    #               "payload":{
    #                 "template_type":"button",
    #                 "text":message,
    #                 "buttons":[
    #                   {
    #                     "type":"web_url",
    #                     "url":"https://www.spotta.nl/folders/intertoys?fid=1",
    #                     "title":"Intertoys"
    #                   },
    #                   {
    #                     "type":"web_url",
    #                     "url":"https://www.spotta.nl/folders/bart-smit?fid=116",
    #                     "title":"Bart Smit"
    #                   }]}}}}),
    #         headers={'Content-type': 'application/json'})
    #     if r.status_code != requests.codes.ok:
    #         	print r.text
    #     typing('on', PAT, recipient)
    #     mg.updateUser(recipient, data)
    #     findToken(recipient, data, text)
    elif text == 'Andere categorie!':
        data['data']['oldType'] = data['data']['type']
        data['data']['type'] = ''
        data['Stage'] = 'decisions'
        mg.updateUser(recipient, data)
        findToken(recipient, data, text)
    elif text == 'Ander bedrag!':
        data['data']['oldBudget'] = data['data']['budget']
        data['data']['budget'] = ''
        data['Stage'] = 'decisions'
        mg.updateUser(recipient, data)
        findToken(recipient, data, text)
    else:
        if data['oldmessage'] != 'Ik heb het zelfs al gevonden!':
            message = random.choice(presentmessage1)
        	data['text'].append(('bot',message))
        	data['oldmessage'] = message
        	postdashbot('bot',(recipient,message, data['message-id']) )
            typing('off', PAT, recipient)
            r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                params={"access_token": token},
                data=json.dumps({
                  "recipient": {"id": recipient},
                  "message": {"text": message.encode('utf-8')}
                }),
                headers={'Content-type': 'application/json'})
            if r.status_code != requests.codes.ok:
                	print r.text
        typing('on', PAT, recipient)
        time.sleep(2)
        checksuggest(PAT, recipient, data,N)
        message = random.choice(presentmessage3)
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
              "recipient": {"id": recipient},
              "message": {"text": message,
              "quick_replies":[{
                            "content_type":"text",
                            "title":'Andere keuzes!',
                            "payload":'Andere'
                          },
                {
                              "content_type":"text",
                              "title":'Gevonden!',
                              "payload":'Gevonden'
                            },{
                                          "content_type":"text",
                                          "title":'Andere categorie!',
                                          "payload":'Categorie'
                                        },{
                                                      "content_type":"text",
                                                      "title":'Ander bedrag!',
                                                      "payload":'bedrag'
                                                    }]}
            }),
            headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            print r.text
        mg.updateUser(recipient, data)
  elif data['Stage'] == 'response':
    if 'Feedback' in data['data']:
        if int(data['data']['Feedback']) > 2:
            message = random.choice(responsemessage)
        else:
            message = 'Jammer dat je het niet zo leuk vond, ik hoop dat je wel geniet van het feest!'
    else:
        message = 'Jammer dat je het niet zo leuk vond, ik hoop dat je wel geniet van het feest!'
    data['text'].append(('bot',message))
    data['oldmessage'] = message
    postdashbot('bot',(recipient,message, data['message-id']) )
    typing('off', PAT, recipient)
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": token},
        data=json.dumps({
          "recipient": {"id": recipient},
          "message": {"text": message}
        }),
        headers={'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        print r.text
    mg.updateUser(recipient, data)
    findToken(recipient, data, text)
  elif data['Stage'] == 'bridge' and data['type'] == 'Snel':
    if text == 'Ja' or text == 'Nee':
        findToken(recipient, data, text)
        mg.updateUser(recipient, data)
    else:
        message = 'Oke! Weet je al wat je zoekt?'
        data['text'].append(('bot',message))
        data['oldmessage'] = message
        postdashbot('bot',(recipient,message, data['message-id']) )
        typing('off', PAT, recipient)
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
              "recipient": {"id": recipient},
              "message": {"text": message,
              "quick_replies":[{
                            "content_type":"text",
                            "title":'Ja',
                            "payload":'Ja'
                          },
                {
                              "content_type":"text",
                              "title":'Nee',
                              "payload":'Nee'
                            }]}
            }),
            headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            print r.text
        mg.updateUser(recipient, data)
  elif data['Stage'] == 'Start':
    if text == 'Uniek cadeau' or text == 'Snel cadeau':
        findToken(recipient, data, text)
    else:
        message = random.choice(startmessage)
        data['text'].append(('bot',message))
        data['oldmessage'] = message
        postdashbot('bot',(recipient,message, data['message-id']) )
        typing('off', PAT, recipient)
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
              "recipient": {"id": recipient},
              "message": {"text": message}
            }),
            headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            print r.text
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
              "recipient": {"id": recipient},
              "message": {"text": 'Zullen we elkaar eerst wat beter leren kennen of wil je snel cadeau advies?',
              "quick_replies":[{
                            "content_type":"text",
                            "title":'Beter leren kennen',
                            "payload":'Uniek'
                          },
                {
                              "content_type":"text",
                              "title":'Cadeau advies',
                              "payload":'Snel'
                            }]}
            }),
            headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            print r.text
        mg.updateUser(recipient, data)
  else:
    time0 = time.time()
    response, data = getResponse(recipient, text, data)
    time1 = time.time()
    print('getresponse',time1-time0)
    if response['type'] == 'stop' or response['msg'] == data['oldmessage']:
    	findToken(recipient, data, text)
    	time2 = time.time()
    	print('stopthing',time2 - time1)
    	time1 = time2
        mg.updateUser(recipient, data)

    elif 'msg' in response and response['msg'] != data['oldmessage']:
        data['text'].append(('bot',response['msg']))
        data['oldmessage'] = response['msg']
        postdashbot('bot',(recipient,response['msg'], data['message-id']))
        mg.updateUser(recipient, data)
        print('joo')
        if 'quickreplies' in response:
            replies = response['quickreplies']
            typing('off', token, recipient)
            r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
              "recipient": {"id": recipient},
              "message": {"text": response['msg'].encode('utf-8'),
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
            typing('off', token, recipient)
            r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
              "recipient": {"id": recipient},
              "message": {"text": response['msg'].encode('utf-8')}
            }),
            headers={'Content-type': 'application/json'})
            if r.status_code != requests.codes.ok:
            	print r.text
	time4 = time.time()
	print('sendmessage', time4 - time0)
  return data

if __name__ == '__main__':
  # personality, sentiment = getIt()
  app.run()
