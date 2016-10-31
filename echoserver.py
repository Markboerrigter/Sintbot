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
import pickle
from flask import g
import time

# personality, sentiment = getIt()


x = dict()
pickle.dump(x, open('user_data.p', 'wb'))

user_data = pickle.load( open( "user_data.p", "rb" ) )



faulwords = pickle.load(open('Faulword.p', 'rb'))
stoplist = []

sentimentClassifier = pickle.load( open( "sentiment_analysis_final.p", "rb" ) )

app = Flask(__name__)

Starttext = pickle.load(open('Starttext.p', 'rb'))

responsemessage = ['Hartstikke bedankt voor het leuke gesprek en tot de volgende keer!', 'Bedankt dat ik je kon helpen en een fijne pakjesavond', 'Bedankt voor het fijne gesprek!', 'Tot de 5de van December!', 'Bedankt voor het gesprek, ik zie je op mijn verjaardag!']
presentmessage1 = ['Bedankt voor je informatie, ik ga is even op zoek naar kadootjes.', 'Oke, ik ga even zoeken! Ben zo terug.', 'Oke, ik weet genoeg! Ik zal is even wat ideeen opzoeken!']
presentmessage3 = ['Ben je tevreden met deze ideeen?', 'Zat er wat leuks tussen?','Heb ik je de juiste keuzes gegeven?']
personalitymessages = [["""
{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"generic",
        "elements":[
          {
            "title": "What do you prefer?",
            "image_url":"http://nl.stockfresh.com/thumbs/nickylarson974/5847697_vakantie-werk-keuze-illustratie-Blauw-Rood.jpg",
          }
        ]
      }
    }
  }
""", 'Do you prefer A or B', 'A', 'B'],[
"""
{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"generic",
        "elements":[
          {
            "title": "What do you prefer?",
            "image_url":"https://pixabay.com/static/uploads/photo/2015/10/06/08/46/directory-973992_960_720.jpg",
          }
        ]
      }
    }
  }
""", 'Do you prefer A or B', 'A', 'B']
,["""
  {
      "attachment":{
        "type":"template",
        "payload":{
          "template_type":"generic",
          "elements":[
            {
              "title": "What do you prefer?",
              "image_url":"http://us.123rf.com/450wm/draganmilenkovic/draganmilenkovic1604/draganmilenkovic160400014/55164130-beste-prijs-en-keuze-illustratie-in-kleurrijke.jpg?ver=6",
            }
          ]
        }
      }
    }
""", 'Do you prefer A or B', 'A', 'B']]
Tokens = pickle.load(open('Tokens.p', 'rb'))

dashbotAPI = 'p2UanZNzFIcjKS321Asc9zIk0lnziYFHodZwV9fh'

TokenStages = ['Start','Connection', 'Personality', 'bridge', 'GiveIdea','decisions', 'presentchoosing', 'feedback', 'response']

tokenWit = 'D4CRSEOIOCHA36Y2ZSQUG7YUCUK3BJBS'
pickle.dump(tokenWit, (open("tokenWit.p", "wb")))

# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
PAT = 'EAAVJQyYb958BAAGBvlYuonE3VZAa2LxCZCzdzRH2USUSYEWOAy0ZBahfV0xqIKGHQ8wzQ9NDKy3eco7JfOn0jULaJJLKlfnAZBv70IJEO4uNu28GGgRZBkrj1yLPYbQrDeE4PEAGZCNKC9KDlkrcjJospRAO5ZCMToK0smK7gZB2xQZDZD'
# PAT for vraag het sint
# EAAVJQyYb958BACIXNdGspAZBwmazFxZBXLNPi7qQVU7JaSZA2TJIDePd5qITVVvEBLA03ocRn4yDYCRXYOtrZCBL7FZCA5VViZAHzunrK2A5LWZAJM5VnuAxcXrcBIORXZBQXGIGvZAZCD7Nt3P7QJZAgQrMvLBJNvqD3Lr0jV7lwFbnAZDZD
# PAT for echoobotje
# EAAVJQyYb958BAAGBvlYuonE3VZAa2LxCZCzdzRH2USUSYEWOAy0ZBahfV0xqIKGHQ8wzQ9NDKy3eco7JfOn0jULaJJLKlfnAZBv70IJEO4uNu28GGgRZBkrj1yLPYbQrDeE4PEAGZCNKC9KDlkrcjJospRAO5ZCMToK0smK7gZB2xQZDZD'

""" FORMULAS ON TEXT PROCESSING

Below you find all formulas needed to preprocess and process the message,
dictionaries and other data sets.
"""

def findword(string):
    if True in [x in faulwords for x in string.split()]:
        print([x in faulwords for x in string.split()])
        return True
    else:
        return False

def get_keys(d,target):
    result = []
    path = []
    get_key(d,target, path, result)
    return result[0]

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
              "payload":"USER_DEFINED_PAYLOAD"
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
  print('boe')
  # if id == 'human':
  #     print('send to dashbot ')
  #     r = requests.post("https://tracker.dashbot.io/track?platform=facebook&v=0.7.4-rest&type=incoming&apiKey=" + dashbotAPI,
  #       data=payload,
  #       headers={'Content-type': 'application/json'})
  #     if r.status_code != requests.codes.ok:
  #       print r.text
  # if id == 'bot':
  #     print('send botshit to dashbot ')
  #     print('payload: ', payload)
  #     r = requests.post("https://tracker.dashbot.io/track?platform=facebook&v=0.7.4-rest&type=outgoing&apiKey=" + dashbotAPI,
  #       data={"qs":{"access_token":PAT},"uri":"https://graph.facebook.com/v2.6/me/messages","json":{"message":{"text":payload[1]},"recipient":{"id":payload[0]}},"method":"POST","responseBody":{"recipient_id":payload[0],"message_id":payload[2]}},
  #       headers={'Content-type': 'application/json'})
  #     if r.status_code != requests.codes.ok:
  #       print r.text

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
        if 'budget' in entities and entities['budget'][0]['confidence'] > 0.8:
            out['budget'] = entities['budget'][0]['value']
        if 'Gender' in entities and entities['Gender'][0]['confidence'] > 0.8:
            out['Gender'] = entities['Gender'][0]['value']
        if 'age_of_person' in entities and entities['age_of_person'][0]['confidence'] > 0.8:
            out['Age'] = entities['age_of_person'][0]['value']
        if 'distinction' in entities and entities['distinction'][0]['confidence'] > 0.8 and entities['distinction'][0]['value'] in ['Ja', 'Nee']:
            out['distinction'] = entities['distinction'][0]['value']
        if 'Feedback' in entities and entities['Feedback'][0]['confidence'] > 0.8:
            out['Feedback'] = entities['Feedback'][0]['value']
        return out
    else:
        return []

def findAnswer(response, question,witToken,data):
    session_id = data['session']
    information = getInformation(response,question)
    response = mergeAns(response, witToken, session_id, question)
    information.update(getInformation(response,question))
    return response,data, information

def getResponse(recipient, text, data):
  print(text, data['token'], data['session'])
  response = tb.response(text, data['token'], data['session'])
  if 'msg' not in response:
      response, data, information = findAnswer(response,text,data['token'],data)
      data['data'].update(information)
  information = getInformation(response, text)

  data['data'].update(information)
  return response, data

def checksuggest(token, recipient, data):
    print('in checksuggest ' + data['Stage'])
    if data['Stage'] == 'presentchoosing':
        print('giving presents')
        print(data['data'])
        final_data = data['data']
        geslacht = final_data['Gender'].split(' ')[1]
        budget = (final_data['budget']).split('-')
        if len(budget) == 2:
            budgetl = int(budget[0])
            budgeth = int(budget[1])
        else:
            budgetl = [int(s) for s in budget[0].split() if s.isdigit()][0]
            budgeth = 1000
        jaar = str(final_data['Age']).split(' ')[0]
        print(geslacht,budgetl, budgeth,jaar)
        presentstasks = mg.findByTrinityRange(geslacht,budgetl, budgeth,jaar)
        if 'product' in data:
            if isinstance(data['data']['product'], str):
                presentsproduct = mg.findArticlesTitleAndDescription(data['product'])
            else:
                presentsproduct = [mg.findArticlesTitleAndDescription(x) for x in (data['product'])]
                presentsproduct = list(set([item for sublist in presentsproduct for item in sublist]))
            L = [presentsproduct,presentstasks]
            if len(L[0])+len(L[1])==len(L[0]+L[1]):
                presents = L[0]+L[1]
            else:

                presents = mergedics(L)
        elif 'hobby' in data:
            if isinstance(data['data']['hobby'], str):
                presentsproduct = mg.findArticlesTitleAndDescription(data['data']['hobby'])
            else:
                presentsproduct = [mg.findArticlesTitleAndDescription(x) for x in (data['data']['hobby'])]
                presentsproduct = list(set([item for sublist in presentsproduct for item in sublist]))
            L = [presentshobby,presentstasks]
            if len(L[0])+len(L[1])==len(L[0]+L[1]):
                presents = L[0]+L[1]
            else:
                presents = mergedics(L)
        else:
            presents = presentstasks
        presents = random.sample(presents,min(len(presents),5))
        data['presents'] = presents
        typing('off', PAT, recipient)
        postdashbot('bot',(recipient,'presents', data['message-id']) )
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
    return data

def findToken(recipient, data, text):
  data['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
  oldToken = data['token']
  Stage = data['Stage']
  print(data['data'])
  print(Stage)
  if data['Stage'] == 'bridge':
      if text.lower() == 'ja':
          data['Stage'] = 'GiveIdea'
          response = {}
          send_message(PAT, recipient, '', data)
      else:
          NextStage = TokenStages[TokenStages.index(Stage)+1]
          data['token'] = random.choice(allValues(Tokens[NextStage]))
          if isinstance(data['token'], dict):
              data['token'] = random.choice(allValues(Tokens[NextStage]))
              data['starter'] = get_keys(Tokens, data['token'])[-1]
          data['Stage'] = NextStage
          response, data = getResponse(recipient, data['starter'], data)
          send_message(PAT, recipient, response['msg'], data)
  elif Stage == 'Connection':
      NextStage = TokenStages[TokenStages.index(Stage)+1]
      data['Stage'] = NextStage
      response = {}
      send_message(PAT, recipient, '', data)
  elif Stage == 'decisions' and not all(k in data['data'] for k in ['budget', 'Age', 'Gender']):
      print('next')
      data['token'] = random.choice(allValues(Tokens[Stage]))
      while get_keys(Tokens, data['token'])[-1] in data['data']:
          data['token'] = random.choice(allValues(Tokens[Stage]))
      data['starter'] = get_keys(Tokens, data['token'])[-1]
      response, data = getResponse(recipient, data['starter'], data)
      send_message(PAT, recipient, response['msg'], data)
  elif Stage == 'decisions':
      NextStage = TokenStages[TokenStages.index(Stage)+1]
      data['Stage'] = NextStage
      response = {}
      send_message(PAT, recipient, '', data)
  elif TokenStages.index(Stage) < len(TokenStages)-1:
      NextStage = TokenStages[TokenStages.index(Stage)+1]
      data['token'] = random.choice(allValues(Tokens[NextStage]))
      if isinstance(data['token'], dict):
          data['token'] = random.choice(allValues(Tokens[NextStage]))
          data['starter'] = get_keys(Tokens, data['token'])[-1]
      data['Stage'] = NextStage
      response, data = getResponse(recipient, data['starter'], data)
      send_message(PAT, recipient, response['msg'], data)
  else:
      print('end of conversation')
      typing('off', PAT, recipient)
      data['dolog'] = 'end'
      response = {}

  return response, data

""" FUNCTIONS TO RECEIVE AND SEND MESSAGES

below the receive and send functions can be found.

"""

@app.route('/', methods=['POST'])
def handle_messages():
  # print "Handling Messages"
  payload = request.get_data()
  pprint(payload)
  global user_data
  for sender, message, mid, recipient in messaging_events(payload) :
    if findword(message):
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": PAT},
        data=json.dumps({
          "recipient": {"id": sender},
          "message": {"text": 'Wij houden hier niet zo van schelden. Zou je alsjeblieft nogmaals mijn vraag willen beantwoorden.'}
        }),
        headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
        	print r.text
    else:
        print(payload)
        print('message events')
        postdashbot('human', payload)
        print(sender,message)
        if sender in user_data:
            print(mid,user_data[sender]['message-id'])
            if mid != user_data[sender]['message-id']:
                # if user_data[sender]['Startpos']:
                # 	user_data[sender]['Startpos'] = False
                # 	user_data[sender]['data']['distinction'] = message
                # 	user_data[sender]['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
                # 	if message.lower() == 'ja':
                # 	  user_data[sender]['token'] = Tokens['GiveIdea']['Ja'].values()[0]
                # 	  user_data[sender]['starter'] = get_keys(Tokens, user_data[sender]['token'])[-1]
                # 	  message = user_data[sender]['starter']
                # 	else:
                # 	  user_data[sender]['token'] = Tokens['GiveIdea']['Nee'].values()[0]
                # 	  print(user_data[sender]['token'])
                # 	  user_data[sender]['starter'] = get_keys(Tokens, user_data[sender]['token'])[-1]
                # 	  message = user_data[sender]['starter']
                # _data[sender]['Stage'] == 'Start':
                #     user_data[sender]['startans'].append(message)
                if user_data[sender]['dolog'] == 'end':
                    print(user_data[sender]['log']['text'])
                    print(user_data[sender]['text'])
                    mg.addUserScore(sender, user_data[sender]['personality'], user_data[sender]['text'], user_data[sender]['presents'],  user_data[sender]['data']['Feedback'])
                    user_data[sender]['log']['text'].update({(max(list(user_data[sender]['log']['text'].keys()))+1):user_data[sender]['text']})
                    user_data[sender]['log']['feedback'].update('')
                    user_data[sender]['log']['presents'].update('')
                    user_data[sender]['Stage'] = TokenStages[0]
                    user_data[sender]['text'] = []
                    user_data[sender]['Startpos'] = False
                    user_data[sender]['dolog'] = ''
                    user_data[sender]['token'] = Tokens['Start']['Old'][random.choice(Tokens['Start']['New'].keys())].values()[0]
                    user_data[sender]['starter'] = ''
                    user_data[sender]['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
                    user_data[sender]['data'] = {}
                    user_data[sender]['personQuestions'] = []
                print("Incoming from %s: %s" % (sender, message))
                print(sender, message)
                user_data[sender]['try'] = 0
                print(message, user_data[sender]['oldincoming'])
                print(mid,user_data[sender]['message-id'])
                user_data[sender]['text'].append(('user',message))
                user_data[sender]['message-id'] = mid
                typing('on', PAT, sender)
                send_message(PAT, sender, message,user_data[sender])
                user_data[sender]['oldincoming'] = message
        else:
            user_info = getdata(sender)
            print(user_info)
            print('NEWUSER')
            makeStartScreen(PAT)
            # persFB, sent = getIt()
            # pprint(persFB)
            user_data[sender] = dict()
            user_data[sender]['log'] = {}
            user_data[sender]['try'] = 0
            # user_data[sender]['persFB'] = persFB
            user_data[sender]['Startpos'] = False
            user_data[sender]['log']['text']= {0:'first conversation'}
            user_data[sender]['log']['feedback']= {}
            user_data[sender]['log']['presents']= {}
            user_data[sender]['dolog'] = ''
            user_data[sender]['startans'] = []
            user_data[sender]['Stage'] = TokenStages[0]
            user_data[sender]['text'] = []
            user_data[sender]['personQuestions'] = []
            user_data[sender]['message-id'] = mid
            user_data[sender]['personality'] = ''
            user_data[sender]['oldincoming'] = message
            user_data[sender]['oldmessage'] = ''
            user_data[sender]['token'] = random.choice(allValues(Tokens['Start']['New']))
            # Tokens['Start']['Personalities']['Extraversion'].values()[0]
            user_data[sender]['starter'] = ''
            user_data[sender]['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
            user_data[sender]['data'] = {}
            typing('on', PAT, sender)
            send_message(PAT, sender, message, user_data[sender])
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
        # if "messaging" in event and "attachment" in event["messaging"][0] and event["messaging"][0]["message"]['attachment']['payload']['elements'][0]['buttons'][1]['type'] == 'postback':
        #   yield event["messaging"][0]["recipient"]['id'], event["messaging"][0]["message"]['attachment']['payload']['elements'][0]['buttons'][1]['title'].encode('unicode_escape'), event["messaging"][0]["message"]['mid'], event['messaging'][0]['recipient']['id']

def send_message(token, recipient, text, data):
  """Send the message text to recipient with id recipient.
  """
  print('And now we will send a message to: '+ recipient)
  print(data['Stage'])
  global user_data
  # if text == 'Get started':
  #  data['startans'] = []
  # if data['Stage'] in ['Personality', 'GiveIdea', 'presentchoosing', 'response']:
  if data['Stage'] == 'Personality':

    message = random.choice(personalitymessages)
    while personalitymessages.index(message) in data['personQuestions']:
        message = random.choice(personalitymessages)
    data['personQuestions'].append(personalitymessages.index(message))
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
    time.sleep(1.5)
    typing('off', PAT, recipient)
	r = requests.post("https://graph.facebook.com/v2.6/me/messages",
	params={"access_token": token},
	data=json.dumps({
	  "recipient": {"id": recipient},
	  "message": {"text": message[1],
	  "quick_replies":{
	                "content_type":"text",
	                "title":message[2],
	                "payload":message[2]
	              },{	                "content_type":"text",
                  	                "title":message[3],
                  	                "payload":message[3]}}
	}),
	headers={'Content-type': 'application/json'})
	if r.status_code != requests.codes.ok:
		print r.text
		print(recipient)
    print('send personality')
    if len(data['personQuestions']) > 2:
        response, data = findToken(recipient, data, text)

  elif data['Stage'] == 'GiveIdea':
    typing('off', PAT, recipient)
    message = 'Waar ben je naar op zoek?'
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": token},
        data=json.dumps({
          "recipient": {"id": recipient},
          "message": {"text": message}
        }),
        headers={'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        	print r.text
    response, data = findToken(recipient, data, text)
  elif data['Stage'] == 'presentchoosing':
    typing('off', PAT, recipient)
    message = random.choice(presentmessage1)
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": token},
        data=json.dumps({
          "recipient": {"id": recipient},
          "message": {"text": message}
        }),
        headers={'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        	print r.text
    typing('on', PAT, recipient)
    checksuggest(PAT, recipient, data)
    message = random.choice(presentmessage3)
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": token},
        data=json.dumps({
          "recipient": {"id": recipient},
          "message": {"text": message},
          "quick_replies":[{
                        "content_type":"text",
                        "title":'Ja',
                        "payload":'Ja'
                      },{
                        "content_type":"text",
                        "title":'Nee',
                        "payload":'Nee'
                      }
                      ]
        }),
        headers={'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        	print r.text
    response, data = findToken(recipient, data, text)
  elif data['Stage'] == 'response':
    typing('off', PAT, recipient)
    message = random.choice(responsemessage)
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": token},
        data=json.dumps({
          "recipient": {"id": recipient},
          "message": {"text": message}
        }),
        headers={'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        	print r.text
    response, data = findToken(recipient, data, text)



  else:
    data['try'] +=1
    time0 = time.time()
    response, data = getResponse(recipient, text, data)
    print(response)
    time1 = time.time()
    print('getresponse',time1-time0)
    # or response['msg'] == data['oldmessage']
    if response['type'] == 'stop' or response['msg'] == data['oldmessage']:
    	response, data = findToken(recipient, data, text)
    	time2 = time.time()
    	print('stopthing',time2 - time1)
    	time1 = time2
        print(data['data'])
        # checksuggest(token, recipient, data)
        time3 = time.time()
        print('checksuggest',time3- time1)
    elif 'msg' in response and response['msg'] != data['oldmessage']:
    	print(response['msg'].decode('unicode_escape', 'ignore'))

    	data['text'].append(('bot',response['msg']))
    	data['oldmessage'] = response['msg']
    	postdashbot('bot',(recipient,response['msg'], data['message-id']) )
    	typing('off', token, recipient)
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
    			print(recipient)
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
    	time4 = time.time()
    	print('sendmessage', time4 - time3)
  user_data[recipient] = data
  pickle.dump(user_data, open('user_data.p', 'wb'))

if __name__ == '__main__':
  # personality, sentiment = getIt()
  app.run()
