from wit import Wit

def send(request, response):
    print('Sending to user...', response['text'])
def my_action(request):
    print('Received from user...', request['text'])

actions = {
    'send': send,
    'my_action': my_action,
}

access_token = 'GNWSVIUT4MZLZGHNVPXKJYLKBLKNQNYQ'

client = Wit(access_token=access_token, actions=actions)

def resp(text):
	respons = client.get_message(text)
	return respons
