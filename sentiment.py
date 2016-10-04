import pickle
from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()

data = pickle.load( open( "text_data_v1.p", "rb" ) )
##print(data[0])
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.classify import ConditionalExponentialClassifier
from nltk.classify import DecisionTreeClassifier
from nltk.classify import MaxentClassifier
from nltk.classify import WekaClassifier
import random

def word_feats(words):
    return dict([(word, True) for word in words])
for line in data:
    print(line)

anders = [x for x in data if x[1] not in ['neg', 'pos', 'obj']]
negids = [[tknzr.tokenize(x[0]),x[1]] for x in data if x[1] == 'neg']
posids = [[tknzr.tokenize(x[0]),x[1]] for x in data if x[1] == 'pos']
objids = [[tknzr.tokenize(x[0]),x[1]] for x in data if x[1] == 'obj']
print(len(negids),len(posids),len(objids),len(data))

 
negfeats = [(word_feats(f[0]), 'neg') for f in negids]
posfeats = [(word_feats(f[0]), 'pos') for f in posids]
objfeats = [(word_feats(f[0]), 'obj') for f in objids]

##print(min([len(negfeats),len(posfeats),len(objfeats)])

leng = min([len(negfeats),len(posfeats),len(objfeats)])


negfeats = random.sample(negfeats,leng)
posfeats = random.sample(posfeats,leng)
objfeats = random.sample(objfeats,leng)

##for x in posfeats:
##    print(x)
##    eerr
## 
negcutoff = int(len(negfeats)*3/4)
poscutoff = int(len(posfeats)*3/4)
objcutoff = int(len(objfeats)*3/4)

print(len(posfeats), len(negfeats), len(data), len(objfeats))
trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff] + objfeats[:objcutoff]
testfeats = negfeats[negcutoff:] + posfeats[poscutoff:] + objfeats[objcutoff:]
##for x in trainfeats:
##    print(x)
##    err
print('train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats)))

##from sklearn.feature_extraction.text import CountVectorizer
##count_vect = CountVectorizer()
##X_train_counts = count_vect.fit_transform(trainfeats)
##X_train_counts.shape
##from sklearn.feature_extraction.text import TfidfTransformer
##tf_transformer = TfidfTransformer(use_idf=False).fit(trainfeats)
##X_train_tf = tf_transformer.transform(X_train_counts)


##clf = MultinomialNB().fit(trainfeats, twenty_train.target)
classifier = NaiveBayesClassifier.train(trainfeats)
print('accuracy:', nltk.classify.util.accuracy(classifier, testfeats))
classifier.show_most_informative_features()

text = 'Het is een super mooie dag'
mooi = classifier.prob_classify(word_feats(text)).prob('pos')
print(mooi)
mooi = classifier.prob_classify(word_feats(text)).prob('neg')
print(mooi)
mooi = classifier.prob_classify(word_feats(text)).prob('obj')
print(mooi)
import pickle


pickle.dump(classifier, open( "sentiment_analysis_final.p", "wb" ) )


