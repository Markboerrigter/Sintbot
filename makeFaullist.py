
x =  ['homo','flikker','klootzak','hitler','nazi','zwartjoekel','bokito','hoer']

file1 = open('scheldwoorden.txt', 'r+').read()

for word in file1:
     x.append(word)

import pickle

pickle.dump(x, open('Faulword.p', 'wb'))

Starttext = {}
Starttext['begin'] = 'Hallo ik ben de hulp piet en ga je vandaag helpen met het zoeken van een kadotje.  Heb je al zin om Sinterklaas te vieren met je familie? :)'
Starttext['Ja'] = {}
Starttext['Ja']['begin'] = 'Natuurlijk haha! Ben jij dan ook altijd lekker aan het praten tijdens de viering?'
Starttext['Ja']['Ja'] = {}
Starttext['Ja']['Ja']['final'] = ['Altijd gezellig, weet je ook al welk cadeau je zoekt?', 'Extraversion']
Starttext['Ja']['Ja']['distinction'] = 'ans'
Starttext['Ja']['Nee'] = {}
Starttext['Ja']['Nee']['begin'] = 'Ben jij dan degene die altijd opruimt na het Sinterklaasfeestje?'
Starttext['Ja']['Nee']['Ja'] = {}
Starttext['Ja']['Nee']['Ja']['begin'] = 'Als je mijn kadootje niet leuk vindt, zou je het me dan eerlijk vertellen?'
Starttext['Ja']['Nee']['Ja']['Ja'] = {}
Starttext['Ja']['Nee']['Ja']['Ja']['begin'] = 'Dat is ook helemaal niet leuk natuurlijk. Ben jij wel goed in het maken van de meest orginele surprises?'
Starttext['Ja']['Nee']['Ja']['Ja']['Ja'] = {}
Starttext['Ja']['Nee']['Ja']['Ja']['Ja']['final'] = ['Ik ben benieuwd! Weet je ook al welk cadeautje je zoekt? :)', 'Openess']
Starttext['Ja']['Nee']['Ja']['Ja']['Nee'] = {}
Starttext['Ja']['Nee']['Ja']['Ja']['Nee']['begin'] = 'Niet de creative ziel van de familie? ;) Heb je je SInterklaas planning wel altijd helemaal op orde?'
Starttext['Ja']['Nee']['Ja']['Ja']['Nee']['Ja'] = {}
Starttext['Ja']['Nee']['Ja']['Ja']['Nee']['Ja']['final'] = ['Structuur is altijd fijn :). Weet je dan ook al welk kado je wil kopen?', 'Conciousness']
Starttext['Ja']['Nee']['Ja']['Nee'] = {}
Starttext['Ja']['Nee']['Ja']['Nee']['final'] = ['Je wil me echt geen pijn doen he! Weet je al welk kado je wil kopen?','Agreeableness']
Starttext['Ja']['Nee']['Nee'] = {}
Starttext['Ja']['Nee']['Nee']['begin'] = 'Dat is ook helemaal niet leuk natuurlijk. Ben jij wel goed in het maken van de meest orginele surprises?'
Starttext['Ja']['Nee']['Nee']['Ja'] = {}
Starttext['Ja']['Nee']['Nee']['Ja']['final'] = ['Ik ben benieuwd! Weet je ook al welk cadeautje je zoekt? :)', 'Openess']
Starttext['Ja']['Nee']['Nee']['Nee'] = {}
Starttext['Ja']['Nee']['Nee']['Nee']['begin'] = 'Niet de creative ziel van de familie? ;) Heb je je SInterklaas planning wel altijd helemaal op orde?'
Starttext['Ja']['Nee']['Nee']['Nee']['Ja'] = {}
Starttext['Ja']['Nee']['Nee']['Nee']['Ja']['final'] = ['Structuur is altijd fijn :). Weet je dan ook al welk kado je wil kopen?', 'Conciousness']
Starttext['Ja']['Nee']['Nee']['Nee']['Nee'] = {}
Starttext['Ja']['Nee']['Nee']['Nee']['Nee']['final'] = ['Je bent toch niet altijd te laat hoop ik? :) Weet je al wel welk kado je wil kopen?', 'default']


Starttext['Nee'] = {}
Starttext['Nee']['begin'] = 'Ben jij dan degene die altijd opruimt na het Sinterklaasfeestje?'
Starttext['Nee']['Ja'] = {}
Starttext['Nee']['Ja']['begin'] = 'Als je mijn kadootje niet leuk vindt, zou je het me dan eerlijk vertellen?'
Starttext['Nee']['Ja']['Ja'] = {}
Starttext['Nee']['Ja']['Ja']['begin'] = 'Dat is ook helemaal niet leuk natuurlijk. Ben jij wel goed in het maken van de meest orginele surprises?'
Starttext['Nee']['Ja']['Ja']['Ja'] = {}
Starttext['Nee']['Ja']['Ja']['Ja']['final'] = ['Ik ben benieuwd! Weet je ook al welk cadeautje je zoekt? :)', 'Openess']
Starttext['Nee']['Ja']['Ja']['Nee'] = {}
Starttext['Nee']['Ja']['Ja']['Nee']['begin'] = 'Niet de creative ziel van de familie? ;) Heb je je SInterklaas planning wel altijd helemaal op orde?'
Starttext['Nee']['Ja']['Ja']['Nee']['Ja'] = {}
Starttext['Nee']['Ja']['Ja']['Nee']['Ja']['final'] = ['Structuur is altijd fijn :). Weet je dan ook al welk kado je wil kopen?', 'Conciousness']
Starttext['Nee']['Ja']['Nee'] = {}
Starttext['Nee']['Ja']['Nee']['final'] = ['Je wil me echt geen pijn doen he! Weet je al welk kado je wil kopen?','Agreeableness']
Starttext['Nee']['Nee'] = {}
Starttext['Nee']['Nee']['begin'] = 'Dat is ook helemaal niet leuk natuurlijk. Ben jij wel goed in het maken van de meest orginele surprises?'
Starttext['Nee']['Nee']['Ja'] = {}
Starttext['Nee']['Nee']['Ja']['final'] = ['Ik ben benieuwd! Weet je ook al welk cadeautje je zoekt? :)', 'Openess']
Starttext['Nee']['Nee']['Nee'] = {}
Starttext['Nee']['Nee']['Nee']['begin'] = 'Niet de creative ziel van de familie? ;) Heb je je SInterklaas planning wel altijd helemaal op orde?'
Starttext['Nee']['Nee']['Nee']['Ja'] = {}
Starttext['Nee']['Nee']['Nee']['Ja']['final'] = ['Structuur is altijd fijn :). Weet je dan ook al welk kado je wil kopen?', 'Conciousness']
Starttext['Nee']['Nee']['Nee']['Nee'] = {}
Starttext['Nee']['Nee']['Nee']['Nee']['final'] = ['Je bent toch niet altijd te laat hoop ik? :) Weet je al wel welk kado je wil kopen?', 'default']

pickle.dump(Starttext, open('Starttext.p', 'wb'))

Tokens = {}
Tokens['Start'] = {}
Tokens['Start']['New'] = {}
Tokens['Start']['New']['Introduce'] = {"Ja": 'D7JHYWLOPGPFHJRCHPWC7DBCBEK2G7RZ'}
Tokens['Start']['New']['Sinterklaas'] = {"Ja": 'TT4U2XJYSY6EZBUKIBGAJPHDNWDZVGVL'}
Tokens['Start']['New']['Story'] = {"Ja": 'JW4QZSHW2GXLJKZEGPH6ZFOOP6PBYTKL'}
Tokens['Start']['New']['Open'] = {"Ja": 'POPSPV3EUB7L3W56K4FOU7ZIMFMFKDRP'}
Tokens['Start']['New']['loose'] = {"Ja": '6YY3HTLYKJG4HJOMEDPQ4BTUBA262SCY'}
Tokens['Start']['longText'] = {"Ja": 'YZDGTRUDQU7H2BPRCWFIEVU4KSL42IK4'}
Tokens['Start']['Old'] = {}
Tokens['Start']['Old']['recognized'] = {"Ja": 'IZ5AIDU7KEVIXG6RAWEOY4W6664XGX3R'}
Tokens['Start']['Old']['oldFashioned'] = {"Ja": 'Z4NCJN2J2CJGNBVW64WQULIWCUD54HMB'}
Tokens['Start']['Old']['longText'] = {"Ja": 'YZDGTRUDQU7H2BPRCWFIEVU4KSL42IK4'}
Tokens['Start']['Old']['sintQuestioning'] = {"Ja": 'DNYI3O6EHFJ376YACLJSDCB3U7H7MXDB'}
# Tokens['Start']['Personalities'] = {}
# Tokens['Start']['Personalities']['Extraversion'] = {'Get Started': 'XXZ45IGCPW35BP2BO2HGZ7F7MZMQWHYR'}
# Tokens['Start']['Personalities']['Agreeableness'] = {'Agreeableness': 'WQD3FULNTPZYX5LEKXPV4SQFBKIO4S3X'}
# Tokens['Start']['Personalities']['Openess'] = {'Openess': 'RF2EW7WPKNNBXOVOMPIHN6WKWPBKSWKK'}
# Tokens['Start']['Personalities']['Conciousness'] = {'Conciousness': 'DV53ZSWVLJXO25PV3TLSRTIYHQ2DZWSU'}
Tokens['GiveIdea'] = {}
Tokens['GiveIdea']['Ja'] = {"Ja":'GI53VC6SX2EPKWUHYOC2MSEIZMZORHFG'}
Tokens['GiveIdea']['Nee'] = {"Nee":'4YK2BMAEKCDX2RVSRJLM22NALZL2TU33'}
Tokens['decisions'] = {}
Tokens['decisions']['age'] = {}
Tokens['decisions']['gender'] = {}
Tokens['decisions']['budget'] = {}
Tokens['decisions']['age']['findage1'] =  {"Age":'BQDMM2HIB7YSAXICR7QFULGKXQWJHKXJ'}
Tokens['decisions']['age']['findage2'] =  {"Age":'5UTS7JO3NPTOHD52HAWKQOZBUNTFC53R'}
Tokens['decisions']['gender']['findgender1'] =  {"Gender":'BBEESH7AOGULQK6L3TPYYRC4L4Y36LHH'}
Tokens['decisions']['gender']['findgender2'] =  {"Gender":'UQVGOAZSC54YYVUGHURXHY5I4U6A2X3M'}
Tokens['decisions']['budget']['findbudget1'] =  {"budget":'IJ7PMHQPAVNK6UU3C3BE3NOVXZ6MMPOJ'}
Tokens['decisions']['budget']['findbudget2'] =  {"budget":'TB4QZIZYN4AZQPHYMWDCNFVOR3MJRUGI'}
Tokens['presentchoosing'] = {}
Tokens['presentchoosing']['present'] = {}
Tokens['presentchoosing']['present']['normal'] = {"Suggest":'5YVSD6XFV4I3Q457C56YRYLED5Q6E6ZK'}
Tokens['presentchoosing']['present']['discount'] = {"Suggest Discount":'RNZHGD6QHWG6JOZF66W52XHU364H4B6Y'}
Tokens['presentchoosing']['present']['loyal'] = {"Suggest loyal":'COHIUFQKSQMSGK6SNFLDR6D74CWZIJLZ'}
# Tokens['presentchoosing']['notFound'] = {}
# Tokens['presentchoosing']['notFound']['stop1'] = {"budget":'B6ZPCLQVJDDKKRNXQFF2HFWF2LZJ27KT'}
# Tokens['presentchoosing']['notFound']['stop2'] = {"budget":'I376WUKZF6BKKUP2I3LQ4CTGF5UBYAOM'}
# Tokens['presentchoosing']['notFound']['popular'] = {"budget":'BQ44V4L72VQKETN5DRE7NKPMDPVJ276C0'}
# Tokens['presentchoosing']['notFound']['keyword1'] = {"budget":'YPRANRJYCS4VPLXM3RZBOZA7V4R73TDY'}
# Tokens['presentchoosing']['notFound']['keyword2'] = {"budget":'5CJ4C7UWBRIVLERLIU5XEMUN3WDUUM3H'}
Tokens['feedback'] = {}
Tokens['feedback']['feedback1'] = {"Feedback":'Z7V53U4LAVY3JWEU6B32ZYBXK4SK6OEJ'}
Tokens['feedback']['feedback2'] = {"Feedback":'6ZUZHBITRTWR3PEJE26DZE6ZX3HHGGES'}

pickle.dump(Tokens, open('Tokens.p', 'wb'))
