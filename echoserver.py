from flask import Flask, request
import sys
from wit import Wit
import json
import requests

w = Wit('GNWSVIUT4MZLZGHNVPXKJYLKBLKNQNYQ')

print(w.get_message('Hi, I was in Rome today')


# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
PAT = 'EAAEkTt8L730BAJzPxFYza8w3Ob9SlH41MwZArFoLFdGCSpgPYkoOB2zfIOJnaDhhP922PyEIayJH5HpzMKZCGM0IcbvZBZCrKRaFY1tj27pGsFcAu2KzvO8ZCusT5OvsUG9RghmR9UDMIOND2prsW5RL4taRe15YgZAtwrgRsM1QZDZD' #'EAAEkTt8L730BAFzZAvriuEFRYN47gpEtI0UIY0Ylsj5GXvw9qp7GnUhlqoIBt2fXZBp3WVs3YIpm6pgnZCeryREd9evbl9wziWQelGcHPxaNtHpU3J7piv9V4fCPfpr5YOMevt8ZC7LXx4PEBXVOvIJluclnOhZB4st8FpYYXJQZDZD'

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
  for sender, message in messaging_events(payload):
    print "Incoming from %s: %s" % (sender, message)
    send_message(PAT, sender, message)
  return "ok"

def messaging_events(payload):
  """Generate tuples of (sender_id, message_text) from the
  provided payload.
  """
  data = json.loads(payload)
  messaging_events = data["entry"][0]["messaging"]
  for event in messaging_events:
    if "message" in event and "text" in event["message"]:
      yield event["sender"]["id"], event["message"]["text"].encode('unicode_escape')
    else:
      yield event["sender"]["id"], "I can't echo this"

def send_message(token, recipient, text):
	
  """Send the message text to recipient with id recipient.
  """
  resp = client.converse('my-user-session-42', text, {})
  r = requests.post("https://graph.facebook.com/v2.6/me/messages",
    params={"access_token": token},
    data=json.dumps({
      "recipient": {"id": recipient},
      "message": {"text": resp.decode('unicode_escape')}
    }),
    headers={'Content-type': 'application/json'})
  if r.status_code != requests.codes.ok:
    print r.resp


session_id = 'my-user-session-42'
context0 = {}
context1 = client.run_actions(session_id, 'what is the weather in London?', context0)
print('The session state is now: ' + str(context1))
context2 = client.run_actions(session_id, 'and in Brussels?', context1)
print('The session state is now: ' + str(context2))



if __name__ == '__main__':
  app.run()
