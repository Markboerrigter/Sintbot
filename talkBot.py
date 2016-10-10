from wit import Wit
#
import pyowm
owm = pyowm.OWM


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

def merge(request):
    context = request['context']
    entities = request['entities']
    if 'relative' in context:
        del context['relative']
    rela = first_entity_value(entities,'relative')
    if rela:
        context['relative'] = rela
    return context


    print(response['context'])

actions = {
    'send': send,
    'merge': merge,
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



# session_id = 'my-user-session-42'
# context0 = {}
# context1 = client.run_actions(session_id, 'what is the weather in London?', context0)
# print('The session state is now: ' + str(context1))
# context2 = client.run_actions(session_id, 'and in Brussels?', context1)
# print('The session state is now: ' + str(context2))

def response(input,token, session_id, context):
    client = Wit(token,actions = actions)
    #print(input)
    resp = client.converse(session_id, input, context)

    return resp
