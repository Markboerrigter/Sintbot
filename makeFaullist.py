
x =  ['homo','flikker','klootzak','hitler','nazi','zwartjoekel','bokito','hoer', 'neger', 'discriminatie', 'rascisme']

file1 = open('scheldwoorden.txt', 'r+').read()

for word in file1.splitlines():
     x.append(word)
print(x)

import pickle
import pprint

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
Tokens['Start']['New']['1'] = {"Get Started": 'ADLGAY3FVPMAEIKF5DEL3EYEIDIHROHQ'}
Tokens['Start']['New']['2'] = {"Get Started": 'NDVDNO7MLGK6EQK7FR574BBF2VQF6KPY'}
Tokens['Start']['New']['3'] = {"Get Started": 'DURGB5YYD4SLABPAMSPXZ4OJJHG5REZN'}
Tokens['Start']['New']['4'] = {"Get Started": 'GNPNF5VIYW7HAI34MLS3CREFJL7UZVFH'}
# Tokens['Start']['New']['5'] = {"Get Started": '6YY3HTLYKJG4HJOMEDPQ4BTUBA262SCY'}
# Tokens['Start']['longText'] = {"Get Started": 'YZDGTRUDQU7H2BPRCWFIEVU4KSL42IK4'}
Tokens['Start']['Old'] = {}
Tokens['Start']['Old']['recognized'] = {"Ja": 'IZ5AIDU7KEVIXG6RAWEOY4W6664XGX3R'}
Tokens['Start']['Old']['oldFashioned'] = {"Ja": 'Z4NCJN2J2CJGNBVW64WQULIWCUD54HMB'}
Tokens['Start']['Old']['longText'] = {"Ja": 'YZDGTRUDQU7H2BPRCWFIEVU4KSL42IK4'}
Tokens['Start']['Old']['sintQuestioning'] = {"Ja": 'DNYI3O6EHFJ376YACLJSDCB3U7H7MXDB'}
Tokens['Connection'] = {}
Tokens['Connection']['1'] = { "connection": 'BJNSOGRPKXSMDPF2ENNVKYTABVHR355K'}
Tokens['Connection']['2'] = { "connection": 'R627JM63JY4EONMAAQ2ANBWYT327TYJC'}
Tokens['Connection']['3'] = { "connection": 'BMJBF36VFTS4DUQ5FYWJQSELDORNS4UC'}
Tokens['Connection']['4'] = { "connection": 'OX5JHQ53LMRSC5Y7FENKP6NTELWU6JHH'}
Tokens['bridge'] = {}
Tokens['bridge']['1'] = {"bridge": 'J6XT5AGLGL5KIXE7IC4XUDNJOGEUF2Q5'}
Tokens['bridge']['2'] = {"bridge": 'H54363GTXNWOLPGX4NAAIC45SJG7J2VL'}
Tokens['bridge']['3'] = {"bridge": 'NBX3SDK2E24UDEIPIOTUNJFXVSMAJ5ZZ'}
Tokens['bridge']['4'] = {"bridge": '3BZNDNOBLRFPWZXR2LPUYHE6NHCGR45V'}
Tokens['bridge']['5'] = {"bridge": 'P5RQHZLDEIWAITYY5P4PILWYFHE4VCDL'}
Tokens['bridge']['6'] = {"bridge": 'ZNU3ZP7F5EXPX6CBLQUBUMWJTD57XT7V'}
Tokens['bridge']['7'] = {"bridge": '4LH3SMXRIW64PM63MIIS6LP2U2AWEXY5'}
Tokens['bridge']['8'] = {"bridge": 'QVOQXFPTO3YVO5RNS36KAZSVPUNQ2KF6'}
Tokens['bridge']['9'] = {"bridge": '7MHFOJP3ZEBOKBF4E7KPSCKF7ZEYPM6Q'}
Tokens['bridge']['10'] = {"bridge": 'JGI6SJ6AFVJVU6LJ32T634MGWRVMPEON'}
Tokens['bridge']['11'] = {"bridge": 'JU722A5QPP33LKMLEP5F7CJ2EH3DEZRY'}
Tokens['bridge']['12'] = {"bridge": 'O4BITSQVHFZAI64ITEMWCMV3CQULIQTJ'}
# Tokens['Personalities'] = {}
# Tokens['Start']['Personalities']['Extraversion'] = {'Get Started': 'XXZ45IGCPW35BP2BO2HGZ7F7MZMQWHYR'}
# Tokens['Start']['Personalities']['Agreeableness'] = {'Agreeableness': 'WQD3FULNTPZYX5LEKXPV4SQFBKIO4S3X'}
# Tokens['Start']['Personalities']['Openess'] = {'Openess': 'RF2EW7WPKNNBXOVOMPIHN6WKWPBKSWKK'}
# Tokens['Start']['Personalities']['Conciousness'] = {'Conciousness': 'DV53ZSWVLJXO25PV3TLSRTIYHQ2DZWSU'}
# Tokens['GiveIdea'] = {}
Tokens['GiveIdea'] = {"Ja":'GI53VC6SX2EPKWUHYOC2MSEIZMZORHFG'}
# Tokens['GiveIdea']['Nee'] = {"Nee":'4YK2BMAEKCDX2RVSRJLM22NALZL2TU33'}
Tokens['decisions'] = {}
Tokens['decisions']['age'] = {}
Tokens['decisions']['gender'] = {}
Tokens['decisions']['budget'] = {}
Tokens['decisions']['type'] = {}
Tokens['decisions']['age']['1'] =  {"Age":'BQDMM2HIB7YSAXICR7QFULGKXQWJHKXJ'}
Tokens['decisions']['age']['2'] =  {"Age":'5UTS7JO3NPTOHD52HAWKQOZBUNTFC53R'}
Tokens['decisions']['age']['3'] =  {"Age":'ZSH2KSPXJBWLDR6YJDG5EHRVXM26ZEUU'}
Tokens['decisions']['gender']['1'] =  {"Gender":'BBEESH7AOGULQK6L3TPYYRC4L4Y36LHH'}
Tokens['decisions']['gender']['2'] =  {"Gender":'UQVGOAZSC54YYVUGHURXHY5I4U6A2X3M'}
Tokens['decisions']['gender']['3'] =  {"Gender":'DJS7HA5DUXDLK42CVX7TUST472LZPOUB'}
Tokens['decisions']['budget']['1'] =  {"budget":'IJ7PMHQPAVNK6UU3C3BE3NOVXZ6MMPOJ'}
Tokens['decisions']['budget']['2'] =  {"budget":'TB4QZIZYN4AZQPHYMWDCNFVOR3MJRUGI'}
Tokens['decisions']['budget']['3'] =  {"budget":'PUL5AUPO3AV2ANCQ7J2S5L4YZEVNYBPN'}
Tokens['decisions']['type']['1'] =  {'type':'1'}
Tokens['decisions']['type']['2'] =  {'type':'1'}
Tokens['decisions']['type']['3'] =  {'type':'1'}
# Tokens['presentchoosing'] = {}
# Tokens['presentchoosing']['present'] = {}
# Tokens['presentchoosing']['present']['normal'] = {"Suggest":'5YVSD6XFV4I3Q457C56YRYLED5Q6E6ZK'}
# Tokens['presentchoosing']['present']['discount'] = {"Suggest Discount":'RNZHGD6QHWG6JOZF66W52XHU364H4B6Y'}
# Tokens['presentchoosing']['present']['loyal'] = {"Suggest loyal":'COHIUFQKSQMSGK6SNFLDR6D74CWZIJLZ'}
# Tokens['presentchoosing']['notFound'] = {}
# Tokens['presentchoosing']['notFound']['stop1'] = {"budget":'B6ZPCLQVJDDKKRNXQFF2HFWF2LZJ27KT'}
# Tokens['presentchoosing']['notFound']['stop2'] = {"budget":'I376WUKZF6BKKUP2I3LQ4CTGF5UBYAOM'}
# Tokens['presentchoosing']['notFound']['popular'] = {"budget":'BQ44V4L72VQKETN5DRE7NKPMDPVJ276C0'}
# Tokens['presentchoosing']['notFound']['keyword1'] = {"budget":'YPRANRJYCS4VPLXM3RZBOZA7V4R73TDY'}
# Tokens['presentchoosing']['notFound']['keyword2'] = {"budget":'5CJ4C7UWBRIVLERLIU5XEMUN3WDUUM3H'}
Tokens['feedback'] = {}
Tokens['feedback']['1'] = {"Feedback":'Z7V53U4LAVY3JWEU6B32ZYBXK4SK6OEJ'}
Tokens['feedback']['2'] = {"Feedback":'6ZUZHBITRTWR3PEJE26DZE6ZX3HHGGES'}
Tokens['feedback']['3'] = {"Feedback":'IJUVMKFS4HEGLIKP25ORZ5UCVVBJGW3Q'}

pickle.dump(Tokens, open('Tokens.p', 'wb'))
# x = {"object":"page","entry":[{"id":"1036938909752245","time":1477923783353,"messaging":[{"sender":{"id":"1036938909752245"},"recipient":{"id":"1100393156681613"},"timestamp":1477923783064,"message":{"is_echo":True,"app_id":1487927634556831,"mid":"mid.1477923783064:3a1a5dd402","seq":7222,"attachments":[{"title":"What do you prefer?","url":'',"type":"template","payload":{"template_type":"generic","sharable":False,"elements":[{"title":"What do you prefer?","image_url":"http:\/\/nl.stockfresh.com\/thumbs\/nickylarson974\/5847697_vakantie-werk-keuze-illustratie-Blauw-Rood.jpg","buttons":[{"type":"postback","title":"Boven","payload":"Boven1"},{"type":"postback","title":"Onder","payload":"Onder2"}]}]}}]}}]}]}
#
# pprint(x)
