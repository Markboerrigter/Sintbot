import mongo as mg
import numpy as np

data = mg.getConvos()
users = mg.getUsers()

convlen = []
convlen1 = []
pers = []
for x in users:
    if x['personality']:
        pers.append(1)
    convlen.append(len(x['text']))
    if len(x['text'])>4:
        convlen1.append(len(x['text']))

print(len(users))
print(len(pers))
print(len(convlen1))
print(np.mean(convlen))
print(np.mean(convlen1))

fb = []

for x in data:
    if x['feedback'] != '0':
        fb.append(x['feedback'])

print(len(fb))
print(len(data))

fb = [int(i) for i in fb]
print(np.mean(fb))
