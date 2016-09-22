from wit import Wit



def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val



def get_forecast(request):
    context = request['context']
    entities = request['entities']

    loc = first_entity_value(entities, 'location')
    if loc:
        context['forecast'] = 'sunny'
    else:
        context['missingLocation'] = True
        if context.get('forecast') is not None:
            del context['forecast']

    return context

def send(request, response):
    print(response['text'])

actions = {
    'send': send,
    'first_entity_value': first_entity_value,
    'getForecast': get_forecast,
}

client = Wit('GNWSVIUT4MZLZGHNVPXKJYLKBLKNQNYQ',actions = actions)
client.interactive()

# session_id = 'my-user-session-42'
# context0 = {}
# context1 = client.run_actions(session_id, 'what is the weather in London?', context0)
# print('The session state is now: ' + str(context1))
# context2 = client.run_actions(session_id, 'and in Brussels?', context1)
# print('The session state is now: ' + str(context2))

def response(input):
    #print(input)
    resp = client.converse('my-user-session-42', input, {})
    print(resp['text'])
    return str(resp)
