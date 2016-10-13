from wit import Wit
from flask import Flask, request
import json
import requests
import sys
from wit import Wit

from runLogin import getIt
import pickle
import random
import datetime
import mongo as mg
import pprint


#
import pyowm
owm = pyowm.OWM
import datetime

def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def get_weather(location):
    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    return w.get_status()


Tokens = {}
Tokens['StartNew'] = {}
Tokens['StartNew']['Introduce'] = 'D7JHYWLOPGPFHJRCHPWC7DBCBEK2G7RZ'
Tokens['StartNew']['Sinterklaas'] = 'TT4U2XJYSY6EZBUKIBGAJPHDNWDZVGVL'
Tokens['StartNew']['Story'] = 'JW4QZSHW2GXLJKZEGPH6ZFOOP6PBYTKL'
Tokens['StartNew']['Open'] = 'POPSPV3EUB7L3W56K4FOU7ZIMFMFKDRP'
Tokens['StartNew']['loose'] = '6YY3HTLYKJG4HJOMEDPQ4BTUBA262SCY'
Tokens['longText'] = 'YZDGTRUDQU7H2BPRCWFIEVU4KSL42IK4'
Tokens['StartOld'] = {}
Tokens['StartOld']['usual'] = 'IZ5AIDU7KEVIXG6RAWEOY4W6664XGX3R'





# def getOntvanger(request):
#     return request['entities'][]
#     {u'type': u'msg', u'msg': u'Stop, Nee, 2', u'entities': {u'ja_nee': [{u'type': u'value', u'suggested': True, u'value': u'Tokens', u'confidence': 0.45982073550975217}], u'intent': [{u'value': u'zoekt kado', u'confidence': 0.5284788122969792}]}, u'confidence': 0.011277662821231825}
#

def get_forecast(request):
    context = request['context']
    entities = request['entities']

    loc = first_entity_value(entities, 'location')
    print(loc)
    if loc:
        context['forecast'] = get_weather(loc)
    else:
        context['missingLocation'] = True
        if context.get('forecast') is not None:
            del context['forecast']
    return context

def computeRes(request):
    entities = request['entities']
    print('entities: ', entities)

def send(request, response):
    print(response['text'])

# def merge(request):
#     context = request['context']
#     entities = request['entities']
#     if 'relative' in context:
#         del context['relative']
#     rela = first_entity_value(entities,'relative')
#     if rela:
#         context['relative'] = rela
#     return context
#
#
#     print(response['context'])

actions = {
    'send': send,
    # 'merge': merge,
    # 'getOntvanger': getOntvanger
    'computeRes': computeRes,
    'first_entity_value': first_entity_value,
    'getForecast': get_forecast,
}
#
# def interact(token):
#
# # clients: ELLWPVMW4P6CEU77HYWBMNUOF45SDSYR 'weather', OP72DHYVY77FZY2U6RCOGN2SNFXXIODJ 'present'
#
#
#     client.interactive()

def findAnswer(response, question,witToken):
    # if response['type'] == 'stop':
    #     if 'ja_nee' in response['entities']:
    #         text = response['entities']['ja_nee'][0]['value']
    #         response = tb.text, witToken, session_id, {})
    #         print(response)
    session_id = data['session']
    response = mergeAns(response, witToken, session_id, question)
    # print('Response in find answer')
    # print(response)
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
            return getResponse(msg[1], data['token'], data['session']), data
        else:
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
            return getResponse('', witToken, session_id)
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

# session_id = 'my-user-session-42'
# context0 = {}
# context1 = client.run_actions(session_id, 'what is the weather in London?', context0)
# print('The session state is now: ' + str(context1))
# context2 = client.run_actions(session_id, 'and in Brussels?', context1)
# print('The session state is now: ' + str(context2))

def getResponse(input,token, session_id):

    client = Wit(token,actions = actions)
    print(input, token, session_id)
    resp = client.converse(session_id, input, {})

    print(resp)
    return resp

def send(token, session_id, text, data):
    response, data = findAnswer(getResponse(text, token, session_id),text, token, session_id)
    information = getInformation(response)
    # print(information)
    for x in information:
        data[x[0]] = x[1]
    if response['type'] == 'stop' and text != 'Bedankt!':
        response,data = findAnswer(getResponse(text, data['token'], data['session']),text,data['token'],data)
        if response['type'] == 'stop':
            data['session'] = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
            print('new id :' + data['session'])
    print(pprint.pprint(personality))
    if 'msg' in response:
        if response['msg'] == 'Bedankt!':
            output = mg.findByTrinity(data['Gender'].lower().split(' ')[1] ,data['Budget'].lower().split(' ')[0],int(data['Budget'].lower().split(' ')[2]),8)
            output = output.split('<br>')
            speelgoed = []
            for x in output:
                x = x.split(',')
                # print(x)
                if len(x[-1]) > 16 and len(speelgoed) < 6:
                    speelgoed.append([x[0],x[-1]])
                # print(len(x))

                # speelgoed.append(x[0] + ' voor maar ' + x[2] + ' euro.')
            messages = [response['msg'] , 'Zocht u een kado voor ' + data['Gender'].lower() + ' voor ' + data['Budget'].lower() + '?',
            'Dan bent u vast op zoek naar deze kadootjes:']
            messages.extend(speelgoed)
            messages.append('En tot de volgende keer')
            # print(message)
            session_id = 'GreenOrange-session-' + str(datetime.datetime.now()).replace(" ", '')
            print('new id :' + data['session'])
            response['output']
            return response, data, session_id
        else:
            return response, data, session_id
    else:
        return response, data, session_id

def findToken(text, token):
    print('Not done yet')


if __name__ == '__main__':
    session_id = 'session_local_' +  str(datetime.datetime.now()).replace(" ", '')
    token = 'ALPOT2MDSZ5OHBIA3ARNA2ZHI76YAQVZ'
    stop = False
    message = 'type your message here: '
    data = {}
    new = True
    while not stop:

        if new :
            token = Tokens['StartNew'][random.choice(Tokens['StartNew'].keys())]
        elif message == 'type your message here: ':
            token = Tokens['StartOld']['usual']
        elif message.split(', ')[0] == 'Stop':
            token = findToken(message,token)

        input = raw_input(message)
        rsp, data, session_id = send(input,token, session_id, data)
        if 'msg' in rsp:
            message = rsp['msg']
        if 'output' in rsp:
            message = rsp['output']
        if rsp['type'] == 'stop':
            print(response)
            stop = True
            if raw_input('Do you want to restart? ') == 'Yes':
                stop = False
                message = 'type your message here: '
                session_id = 'session_local_d' +  str(datetime.datetime.now()).replace(" ", '')
