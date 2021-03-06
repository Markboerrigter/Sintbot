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
import emoji

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
            "title": "Liever creatief of lekker lui?",
            "image_url":"http://support.greenorange.com/sint/images/IG_vraag2_Maken_Internet.jpg",
          }
        ]
      }
    }
  }
""", 'Maak jij een hele mooie originele surprise of een gedichtje van het internet? :)', ['Surprise', "https://support.greenorange.com/sint/images/geel_suprise_maken.png"], ['Gedichtje', "https://support.greenorange.com/sint/images/rood_gedicht_internet.png"]],[
"""
{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"generic",
        "elements":[
          {
            "title": "Geef of krijg jij liever een kado?",
            "image_url":"http://support.greenorange.com/sint/images/IG_vraag3_Geven_Ontvangen.jpg",
          }
        ]
      }
    }
  }
""", 'Geef jij liever een kado, of krijg je liever iets? :)', ['Geven', "https://support.greenorange.com/sint/images/blauw_kado_geven.png"], ['Krijgen', "https://support.greenorange.com/sint/images/groen_kado_krijgen.png"]]
,["""
  {
      "attachment":{
        "type":"template",
        "payload":{
          "template_type":"generic",
          "elements":[
            {
              "title": "Lees of schrijf jij liever een gedicht?",
              "image_url":"http://support.greenorange.com/sint/images/IG_vraag1_Lezen_Schrijven.jpg",
            }
          ]
        }
      }
    }
""", 'Lees jij liever je gedicht voor aan de groep, of schijf je liever een gedicht voor een ander? :)', ['Lezen', "https://support.greenorange.com/sint/images/groen_gedicht_lezen.png"], ['Schrijven',"https://support.greenorange.com/sint/images/blauw_gedicht_schrijven.jpg"]]]


# personality, sentiment = getIt()
# print(emoji.emojize('Python is :thumbs_up_sign:'))
childTypes = ['Kleine ontdekkers', "Kleine papa's, mama's en dierenvriendjes", 'Knutselaars', 'Verhalenmakers en superhelden', 'Knappe koppen en boekenwurmen', 'Spelletjesgekken en puzzelfans', 'Bouwers en onderzoekers', 'Sporters, stunters en stoere kids', 'Razende racers en stoere stuurders', 'Rocksterren en stijliconen', 'Gadget- en gamekings']
# typeResponse = ['Houd het kind van games, puzzles of gadgets?', 'Ah, dus het kind houd van dieren, ontdekken of oudertje spelen? ', 'Een slim kind dus, dat graag verhalen verteldt, bouwt of zelf dingen uitzoekt?','Het kind houd dus van muziek of knutselen?',"Dus het kind houd van auto's, stunten of sporten? :)"]
# childTypes = [x.encode('utf-8') for x in childTypes]

# for x in childTypes:
#     print(x)
# err

x = dict()
pickle.dump(x, open('user_data.p', 'wb'))

user_data = pickle.load( open( "user_data.p", "rb" ) )

N = 3
# Number of presented articles


faulwords = pickle.load(open('Faulword.p', 'rb'))
stoplist = []

# sentimentClassifier = pickle.load( open( "sentiment_analysis_final.p", "rb" ) )

app = Flask(__name__)

Starttext = pickle.load(open('Starttext.p', 'rb'))


Tokens = pickle.load(open('Tokens.p', 'rb'))

dashbotAPI = 'p2UanZNzFIcjKS321Asc9zIk0lnziYFHodZwV9fh'

TokenStages = ['Start','Connection', 'Personality', 'bridge', 'GiveIdea','decisions', 'presentchoosing', 'feedback', 'response']

tokenWit = 'D4CRSEOIOCHA36Y2ZSQUG7YUCUK3BJBS'
pickle.dump(tokenWit, (open("tokenWit.p", "wb")))

# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
PAT = 'EAAEkTt8L730BAHjWMPZBB2TwmUlCIoO1moPuJx8wBzsSZCd7vJoSCLXEZAaYcCXQxYOv54i4OpgvdqOnm7BNO4IoedMvLSZBZBnCaHs5hzQqPDssQgEuSiKJRYCgPG8ZBIjLQHZAxYGBlzT104bweesw01bfMijSCNVPWw4ZC5Bu1gZDZD'
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
  print('make starting screen')
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
    print(token, recipient)
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
            print('something is going wrong')
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
        if 'typeChild' in entities and entities['typeChild'][0]['confidence'] > 0.8:
            out['typeChild'] = entities['typeChild'][0]['value']
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
  mg.updateUser(recipient, data)
  return response, data

def checksuggest(token, recipient, data,n):
    print('in checksuggest ' + data['Stage'])
    if data['Stage'] == 'presentchoosing':
        print('giving presents')
        print(data['data'])
        final_data = data['data']
        geslacht = final_data['Gender'].split(' ')[1]
        budget = (final_data['budget']).split('-')
        age = str(final_data['Age']).split(' ')[0]
        category = data['data']['type']
        if 'product' in final_data:
            idea = final_data['product']
        else: idea = ''
        # presentstasks = mg.findByTrinityRange(geslacht,budgetl, budgeth,jaar)
        # if 'product' in data:
        #     if isinstance(data['data']['product'], str):
        #         presentsproduct = mg.findArticlesTitleAndDescription(data['product'])
        #     else:
        #         presentsproduct = [mg.findArticlesTitleAndDescription(x) for x in (data['product'])]
        #         presentsproduct = list(set([item for sublist in presentsproduct for item in sublist]))
        #     L = [presentsproduct,presentstasks]
        #     if len(L[0])+len(L[1])==len(L[0]+L[1]):
        #         presents = L[0]+L[1]
        #     else:
        #
        #         presents = mergedics(L)
        # elif 'hobby' in data:
        #     if isinstance(data['data']['hobby'], str):
        #         presentsproduct = mg.findArticlesTitleAndDescription(data['data']['hobby'])
        #     else:
        #         presentsproduct = [mg.findArticlesTitleAndDescription(x) for x in (data['data']['hobby'])]
        #         presentsproduct = list(set([item for sublist in presentsproduct for item in sublist]))
        #     L = [presentshobby,presentstasks]
        #     if len(L[0])+len(L[1])==len(L[0]+L[1]):
        #         presents = L[0]+L[1]
        #     else:
        #         presents = mergedics(L)
        # else:
        #     presents = presentstasks
        presents = mg.findRightProduct(geslacht, budget, age, category, idea,3*N)[n-N:n]
        data['presents'] = presents
        postdashbot('bot',(recipient,'presents', data['message-id']) )
        typing('off', PAT, recipient)
        # print(presents)

        for x in presents:
            if not x[0]['img_link']:
                print('image is missing')

                if x[0]['retailer'] == 'intertoys':
                    x.append('http://support.greenorange.com/sint/intertoys/'+ 'p' + str(x[0]['page']) + '_' + str(x[0]['article_number']) + '.png')
                else:
                    x.append('http://support.greenorange.com/sint/bartsmit/'+ 'p' + str(x[0]['page']) + '-' + str(x[0]['article_number']) + '.jpg')
            else:
                x.append(x[0]['img_link'])
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
                    "title":x[0]['title'],
                    "item_url":"https://www.spotta.nl/folders/intertoys?fid=1&page=" + str(x[0]['page']),
                    "image_url":x[2],
                    "subtitle":x[0]['description'],
                    "buttons":[
                      {
                        "type":"web_url",
                        "url": "https://www.spotta.nl/folders/intertoys?fid=1&page=" + str(x[0]['page']),
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
    mg.updateUser(recipient, data)
    return data

def findToken(recipient, data, text):
  data['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
  oldToken = data['token']
  Stage = data['Stage']
  print(data['data'])
  print(Stage)
  if data['Stage'] == 'bridge':
      if text.lower() == 'ja':
          typing('on', PAT, recipient)
          NextStage = TokenStages[TokenStages.index(Stage)+1]
          data['token'] = random.choice(allValues(Tokens[NextStage]))
          if isinstance(data['token'], dict):
              data['token'] = random.choice(allValues(Tokens[NextStage]))
              data['starter'] = get_keys(Tokens, data['token'])[-1]
          data['Stage'] = NextStage
          mg.updateUser(recipient, data)
        #   response, data = getResponse(recipient, data['starter'], data)
          send_message(PAT, recipient, data['starter'], data)
      else:
          r = requests.post("https://graph.facebook.com/v2.6/me/messages",
          params={"access_token": PAT},
          data=json.dumps({
          "recipient": {"id": recipient},
          "message": {"text": 'Oke, dan gaan we samen op zoek!'}
          }),
          headers={'Content-type': 'application/json'})
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
        #   response, data = getResponse(recipient, data['starter'], data)
          send_message(PAT, recipient, data['starter'], data)
  elif Stage == 'feedback':
      NextStage = TokenStages[TokenStages.index(Stage)+1]
      data['Stage'] = NextStage
      response = {}
      print(data['Stage'])
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
      NextStage = TokenStages[TokenStages.index(Stage)+1]
      data['token'] = random.choice(allValues(Tokens[NextStage]))
      if isinstance(data['token'], dict):
          data['token'] = random.choice(allValues(Tokens[NextStage]))
          data['starter'] = get_keys(Tokens, data['token'])[-1]
      data['Stage'] = NextStage
      r = requests.post("https://graph.facebook.com/v2.6/me/messages",
      params={"access_token": PAT},
      data=json.dumps({
      "recipient": {"id": recipient},
      "message": {"text": 'Ik wil graag nog wat andere dingen weten om zeker te zijn wat je zoekt!'}
      }),
      headers={'Content-type': 'application/json'})
      if r.status_code != requests.codes.ok:
      	print r.text
      mg.updateUser(recipient, data)
    #   response, data = getResponse(recipient, data['starter'], data)
      send_message(PAT, recipient, data['starter'], data)
  elif Stage == 'decisions':
      if not all(k in data['data'] for k in ['budget', 'Age', 'Gender', 'type']):
          print('next')
          data['token'] = random.choice(allValues(Tokens[Stage]))
          while get_keys(Tokens, data['token'])[-1] in data['data']:
              data['token'] = random.choice(allValues(Tokens[Stage]))
          data['starter'] = get_keys(Tokens, data['token'])[-1]
        #   response, data = getResponse(recipient, data['starter'], data)
          mg.updateUser(recipient, data)
          send_message(PAT, recipient, data['starter'], data)
      else:
          NextStage = TokenStages[TokenStages.index(Stage)+1]
          data['Stage'] = NextStage
          response = {}
          print(data['Stage'])
          mg.updateUser(recipient, data)
          send_message(PAT, recipient, '', data)
  elif Stage == 'Personality':
      print(data['personality'])
      print("let's go to the bridge")
      Nextstage = TokenStages[TokenStages.index(Stage)+1]
      data['Stage'] = Nextstage
      print(Nextstage)
      print(data['personality'][1:])
      print(set(data['personality'][1:]))
      print(set(['Geven', 'Gedichtje']))
      print(data['token'])
      if set(data['personality'][1:]) == set(['Geven', 'Surprise']):
          data['token'] = Tokens[Nextstage]['1'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
          print('changing something')
      elif set(data['personality'][1:]) == set(['Geven', 'Gedichtje']):
          data['token'] = Tokens[Nextstage]['2'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
          print('changing something')
      elif set(data['personality'][1:]) == set(['Geven', 'Lezen']):
          data['token'] = Tokens[Nextstage]['3'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
          print('changing something')
      elif set(data['personality'][1:]) == set(['Geven', 'Schrijven']):
          data['token'] = Tokens[Nextstage]['4'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
          print('changing something')
      elif set(data['personality'][1:]) == set(['Krijgen', 'Surprise']):
          data['token'] = Tokens[Nextstage]['5'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
          print('changing something')
      elif set(data['personality'][1:]) == set(['Krijgen', 'Gedichtje']):
          data['token'] = Tokens[Nextstage]['6'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
          print('changing something')
      elif set(data['personality'][1:]) == set(['Krijgen', 'Lezen']):
          data['token'] = Tokens[Nextstage]['7'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
          print('changing something')
      elif set(data['personality'][1:]) == set(['Krijgen', 'Schrijven']):
          data['token'] = Tokens[Nextstage]['8'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
          print('changing something')
      elif set(data['personality'][1:]) == set(['Schrijven', 'Surprise']):
          data['token'] = Tokens[Nextstage]['9'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
          print('changing something')
      elif set(data['personality'][1:]) == set(['Schrijven', 'Gedichtje']):
          data['token'] = Tokens[Nextstage]['10'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
          print('changing something')
      elif set(data['personality'][1:]) == set(['Lezen', 'Surprise']):
          data['token'] = Tokens[Nextstage]['11'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
          print('changing something')
      elif set(data['personality'][1:]) == set(['Lezen', 'Gedichtje']):
          print('changing something')
          data['token'] = Tokens[Nextstage]['12'].values()[0]
          data['starter'] = get_keys(Tokens, data['token'])[-1]
      else:
          print('something went wrong')
          print(Nextstage)
          print(data['personality'][1:])
      print(data['token'])
      mg.updateUser(recipient, data)
      send_message(PAT, recipient, data['starter'], data)
  elif TokenStages.index(Stage) < len(TokenStages)-1:
      NextStage = TokenStages[TokenStages.index(Stage)+1]
      data['token'] = random.choice(allValues(Tokens[NextStage]))
      if isinstance(data['token'], dict):
          data['token'] = random.choice(allValues(Tokens[NextStage]))
          data['starter'] = get_keys(Tokens, data['token'])[-1]
      data['Stage'] = NextStage
      mg.updateUser(recipient, data)
    #   response, data = getResponse(recipient, data['starter'], data)
      send_message(PAT, recipient, data['starter'], data)
  else:
      print('end of conversation')
      typing('off', PAT, recipient)
      data['dolog'] = 'end'
      response = {}
      mg.updateUser(recipient, data)

  # return response, data

""" FUNCTIONS TO RECEIVE AND SEND MESSAGES

below the receive and send functions can be found.

"""

@app.route('/', methods=['POST'])
def handle_messages():
  # print "Handling Messages"
  payload = request.get_data()
  print(payload)
  global user_data
  print('in sintbot')

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
    if not mg.findUser(sender):
        user_info = getdata(sender)
        data = {}
        data['info'] = user_info
        data['log'] = {}
        # data['persFB'] = persFB
        data['log']['text']= {'0':'first conversation'}
        data['log']['feedback']= {}
        data['log']['presents']= {}
        data['dolog'] = ''
        data['secondchoice'] = False
        data['secondRow'] = False
        data['Stage'] = TokenStages[0]
        data['text'] = []
        data['personQuestions'] = []
        data['message-id'] = mid
        data['personality'] = []
        data['oldincoming'] = message
        data['oldmessage'] = ''
        data['intype'] = False
        data['token'] = random.choice(allValues(Tokens['Start']['New']))
        # data['token'] = '1'
        # Tokens['Start']['Personalities']['Extraversion'].values()[0]
        data['starter'] = ''
        data['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
        data['data'] = {}
        mg.insertUser(sender,data)
        typing('on', PAT, sender)
        data = send_message(PAT, sender, message,data)
        # user_data[recipient] = data
        # pickle.dump(user_data, open('user_data.p', 'wb'))
    else:
        data = findUser(id)
        print(data)
        print(message)
        print('message events')
        postdashbot('human', payload)
        print(sender,message)
        print(mid,data['message-id'])
        if mid != data['message-id']:
            if data['dolog'] == 'end':
                # print(user_data[sender]['log']['text'])
                # print(user_data[sender]['text'])
                # mg.addUserScore(sender, user_data[sender]['personality'], user_data[sender]['text'], user_data[sender]['presents'],  user_data[sender]['data']['Feedback'])
                data['log']['text'].update({str(max([ int(x) for x in list(data['log']['text'].keys())])+1):data['text']})
                data['log']['feedback'].update('')
                data['log']['presents'].update('')
                data['Stage'] = TokenStages[0]
                data['text'] = []
                data['dolog'] = ''
                data['secondRow'] = False
                data['token'] = '2'
                data['starter'] = ''
                data['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
                data['data'] = {}
                data['secondchoice'] = False
                data['intype'] = False
                data['personQuestions'] = []
            print("Incoming from %s: %s" % (sender, message))
            print(sender, message)
            print(message, data['oldincoming'])
            print(mid,data['message-id'])
            data['text'].append(('user',message))
            data['message-id'] = mid
            data['oldincoming'] = message
            typing('on', PAT, sender)
            data = send_message(PAT, sender, message,data)
  return "ok", 200

def messaging_events(payload):
  """Generate tuples of (sender_id, message_text) from the
  provided payload.
  """
  data = json.loads(payload)
  if "messaging" in data["entry"][0]:
      messaging_events = data["entry"][0]["messaging"]
      for event in messaging_events:
        print(event)
        if "message" in event and "text" in event["message"] and 'is_echo' not in event["message"]:
          yield event["sender"]["id"], event["message"]["text"].encode('unicode_escape'), event["message"]['mid'], event["recipient"]['id']
        if 'postback'in event:
          print('postback event')
          yield event["sender"]["id"], event["postback"]["payload"].encode('unicode_escape'), 'Postback', event["recipient"]['id']
        # if "messaging" in event and "attachment" in event["messaging"][0] and event["messaging"][0]["message"]['attachment']['payload']['elements'][0]['buttons'][1]['type'] == 'postback':
        #   yield event["messaging"][0]["recipient"]['id'], event["messaging"][0]["message"]['attachment']['payload']['elements'][0]['buttons'][1]['title'].encode('unicode_escape'), event["messaging"][0]["message"]['mid'], event['messaging'][0]['recipient']['id']
  # if 'postback'in data["entry"][0]:
  #     messaging_events = data["entry"][0]
  #     for event in messaging_events:

def send_message(token, recipient, text, data):
  """Send the message text to recipient with id recipient.
  """
  print('And now we will send a message to: '+ recipient)
  print(data['Stage'])

  if data['dolog'] == 'end':
      print('done')

  elif data['token'] == '1' and data['Stage'] == 'decisions':
    print('text for this phase',text)
    print(text.encode('utf-8'))
    print(childTypes)
    print(text)
    if text.isdigit() and data['intype']:
        print(text)
        if int(text) in range(1,12):
            print('jeeeej')
            x = int(text)
            if data['secondRow'] == False and text == '6':
                data['secondRow'] = True
                message = 'Ik vroeg me nog af, tot welke van onderstaande categorieen behoort het kind het best? \n' +'\n'.join([str(i) + ': ' + childTypes[i-1] for i in range(6,12)])
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
                                  "title":str(x),
                                  "payload":str(x)
                                } for x in range(6,12)
                                ]
                  }}),
                  headers={'Content-type': 'application/json'})
                if r.status_code != requests.codes.ok:
                  	print r.text
                mg.updateUser(recipient, data)
            else:
                data['data']['type'] =  childTypes[x-1]
                print(data['data'])
                findToken(recipient, data, text)
                mg.updateUser(recipient, data)
    else:
      data['intype'] = True
      print('start cat')
      message = 'Ik vroeg me nog af, tot welke van onderstaande categorieen behoort het kind het best? \n' +'\n'.join([str(i) + ': ' + childTypes[i-1] for i in range(1,6)]) + '\n6: Een andere categorie'
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
                          "title":str(x),
                          "payload":str(x)
                        } for x in range(1,7)
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
    print(data['personality'], 'in send mess')
    if not data['personQuestions']:
        print(text)
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
        time.sleep(1)
        message = 'Het grote boek van Sinterklaas kent alle kinderen, maar weet wat minder van de volwassenen. Ik wil wat vragen stellen om je beter te leren kennen!'
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
        time.sleep(3)

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
    	postdashbot('bot',(recipient,message, data['message-id']) )
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
        print('send personality')


  # elif data['Stage'] == 'GiveIdea':
  #
  #   message = 'Waar ben je naar op zoek?'
  #   if message == data['oldmessage']:
  #       information = getInformation(tb.response(text, 'GI53VC6SX2EPKWUHYOC2MSEIZMZORHFG' , 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')), text)
  #       data['data'].update(information)
  #       findToken(recipient, data, text)
  #   else:
  #   	data['text'].append(('bot',message))
  #   	data['oldmessage'] = message
  #   	postdashbot('bot',(recipient,message, data['message-id']) )
  #       typing('off', PAT, recipient)
  #       r = requests.post("https://graph.facebook.com/v2.6/me/messages",
  #           params={"access_token": token},
  #           data=json.dumps({
  #             "recipient": {"id": recipient},
  #             "message": {"text": message}
  #           }),
  #           headers={'Content-type': 'application/json'})
  #       if r.status_code != requests.codes.ok:
  #           	print r.text

  elif data['token'] == '2':
      if text == 'Oke!':
          findToken(recipient, data, text)
      else:
          message = 'Welkom Terug, zullen we weer op zoek gaan naar een kado? :)'
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
    if text == 'Ja':
        findToken(recipient, data, text)
    elif text == 'Nee' and not data['secondchoice']:

        data['secondchoice'] = True
        message = 'Oke, bedankt dat je zo eerlijk bent! Ik zal nog een keer kijken.'
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
        checksuggest(PAT, recipient, data,N+N)
        message = random.choice(presentmessage3)

        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
              "recipient": {"id": recipient},
              "message": {"text": message.encode('utf-8'),
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
            }}),
            headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            print r.text
        mg.updateUser(recipient, data)
    elif text == 'Nee' and data['secondchoice']:
        message = 'Sorry, ik denk dat ik niet helemaal weet wat je zoekt. Je zou zelf verder kunnen zoeken in de folders. Die kun je vinden via de volgende links'
    	data['text'].append(('bot',message))
    	data['oldmessage'] = message
    	postdashbot('bot',(recipient,message, data['message-id']) )
        typing('off', PAT, recipient)
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
              "recipient": {"id": recipient},
  "message":{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"button",
        "text":message,
        "buttons":[
          {
            "type":"web_url",
            "url":"https://www.spotta.nl/folders/intertoys?fid=1",
            "title":"Intertoys"
          },
          {
            "type":"web_url",
            "url":"https://www.spotta.nl/folders/bart-smit?fid=116",
            "title":"Bart Smit"
          }
        ]
      }
    }
  }
            }),
            headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            	print r.text
        typing('on', PAT, recipient)
        mg.updateUser(recipient, data)
        findToken(recipient, data, text)

    else:
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
        checksuggest(PAT, recipient, data,N)
        message = random.choice(presentmessage3)
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
              "recipient": {"id": recipient},
              "message": {"text": message.encode('utf-8'),
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
            }}),
            headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            print r.text
        mg.updateUser(recipient, data)
  elif data['Stage'] == 'response':
    typing('off', PAT, recipient)
    message = random.choice(responsemessage)
    data['text'].append(('bot',message))
    data['oldmessage'] = message
    postdashbot('bot',(recipient,message, data['message-id']) )
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
  else:
    time0 = time.time()
    response, data = getResponse(recipient, text, data)
    print(response)
    time1 = time.time()
    print('getresponse',time1-time0)
    if response['type'] == 'stop' or response['msg'] == data['oldmessage']:
    	findToken(recipient, data, text)
    	time2 = time.time()
    	print('stopthing',time2 - time1)
    	time1 = time2
        print(data['data'])
        # checksuggest(token, recipient, data)
        mg.updateUser(recipient, data)
    elif 'msg' in response and response['msg'] != data['oldmessage']:
        # print(response['msg'])
        time3 = time.time()
        print('checksuggest',time3- time1)
        data['text'].append(('bot',response['msg']))
        data['oldmessage'] = response['msg']
        postdashbot('bot',(recipient,response['msg'], data['message-id']))
        mg.updateUser(recipient, data)
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
            	print(recipient)
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
    	print('sendmessage', time4 - time3)
  return data

if __name__ == '__main__':
  # personality, sentiment = getIt()
  app.run()
