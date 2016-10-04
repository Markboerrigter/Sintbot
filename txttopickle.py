import pickle
file = open('test_data.txt', 'r+')


text = file.read()[:-1]
text = text.splitlines()

print(text[-1])
data = [line.split( '||') for line in text]

pickle.dump(data, open( "text_data_v1.p", "wb" ) )
