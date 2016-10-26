
x =  ['homo','flikker','klootzak','hitler','nazi','zwartjoekel','bokito','hoer']

file1 = open('scheldwoorden.txt', 'r+').read()

for word in file1:
     x.append(word)

import pickle

pickle.dump(x, open('Faulword.p', 'wb'))
