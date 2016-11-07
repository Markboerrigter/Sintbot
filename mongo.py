from pymongo import MongoClient
import datetime
from difflib import SequenceMatcher
# import sys
# sys.path.insert(0, sys.path[0]+'/kpss/kpss')
#
# # import file
import kpss
information = {'oldincoming': '15-30 euro', 'Stage': 'presentchoosing', 'startans': [], 'dolog': '', 'text': [('bot', u'Hallo, ik ben spot, de chatbot van spotta. Ik ga je vandaag helpen met het vinden van het juiste kado. Maar eerst gaan we elkaar wat beter leren kennen oke? :) '), ('user', 'Oke!'), ('bot', u'Weet je al welke surprise je bij het cadeau gaat maken?  '), ('user', 'Ja, leuk!'), ('bot', 'Ah, leuk!'), ('bot', 'Het grote boek van Sinterklaas kent alle kinderen, maar weet wat minder van de volwassenen. Ik wil wat vragen stellen om je beter te leren kennen!'), ('bot', ['\n{\n    "attachment":{\n      "type":"template",\n      "payload":{\n        "template_type":"generic",\n        "elements":[\n          {\n            "title": "Liever creatief of lekker lui?",\n            "image_url":"http://support.greenorange.com/sint/images/IG_vraag2_Maken_Internet.jpg",\n          }\n        ]\n      }\n    }\n  }\n', 'Maak jij een hele mooie originele surprise of een gedichtje van het internet? :)', ['Surprise', 'https://support.greenorange.com/sint/images/geel_suprise_maken.png'], ['Gedichtje', 'https://support.greenorange.com/sint/images/rood_gedicht_internet.png']]), ('user', 'Surprise'), ('bot', ['\n  {\n      "attachment":{\n        "type":"template",\n        "payload":{\n          "template_type":"generic",\n          "elements":[\n            {\n              "title": "Lees of schrijf jij liever een gedicht?",\n              "image_url":"http://support.greenorange.com/sint/images/IG_vraag1_Lezen_Schrijven.jpg",\n            }\n          ]\n        }\n      }\n    }\n', 'Lees jij liever je gedicht voor aan de groep, of schijf je liever een gedicht voor een ander? :)', ['Lezen', 'https://support.greenorange.com/sint/images/groen_gedicht_lezen.png'], ['Schrijven', 'https://support.greenorange.com/sint/images/blauw_gedicht_schrijven.jpg']]), ('user', 'Schrijven'), ('bot', ['\n{\n    "attachment":{\n      "type":"template",\n      "payload":{\n        "template_type":"generic",\n        "elements":[\n          {\n            "title": "Geef of krijg jij liever een kado?",\n            "image_url":"http://support.greenorange.com/sint/images/IG_vraag3_Geven_Ontvangen.jpg",\n          }\n        ]\n      }\n    }\n  }\n', 'Geef jij liever een kado, of krijg je liever iets? :)', ['Geven', 'https://support.greenorange.com/sint/images/blauw_kado_geven.png'], ['Krijgen', 'https://support.greenorange.com/sint/images/groen_kado_krijgen.png']]), ('user', 'Geven'), ('bot', u'Dus jouw familie gaat weer lange gedichten mogen voorlezen? Weet je al welk kadootje je daarbij gaat geven?'), ('user', 'Nee'), ('bot', u'Ik vroeg me af, hoe oud is de gelukkige dit jaar geworden? \U0001f389'), ('user', '8 jaar oud'), ('bot', "Ik vroeg me nog af, tot welke van onderstaande categorieen behoort het kind het best? \n1: Kleine ontdekkers\n2: Kleine papa's, mama's en dierenvriendjes\n3: Knutselaars\n4: Verhalenmakers en superhelden\n5: Knappe koppen en boekenwurmen\n6: Een andere categorie"), ('user', '3'), ('bot', u'Is het voor een jongen of een meisje? '), ('user', 'Een meisje'), ('bot', u'Voor sinterklaas zijn heel veel kadootjes in de aanbieding, hoe hoog is uw budget? \U0001f4b0\U0001f4b0'), ('user', '15-30 euro'), ('bot', 'Bedankt voor je informatie, ik ga is even op zoek naar kadootjes.')], 'try': 1, 'message-id': u'mid.1478529445681:70fefe9267', 'data': {'type': 'Knutselaars', 'Age': u'oud', 'budget': u'15-30', 'distinction': u'Nee', 'Gender': u'Een meisje'}, 'cat': 'Knutselaars', 'Startpos': False, 'starter': 'budget', 'presents': [[{u'description_extended': u'Schilder jij dit romantische schilderij met dolfijnen bij zonsondergang?\n\nHet was nog nooit zo makkelijk om een schilderij te maken als met schilderen op nummer van Ravensburger!\n\nDe cijfers in de vakjes geven aan welke kleur verf je moet gebruiken. Volg de instructies open maak dit romantische schilderij!\n\nInhoud\n\u2022 11 Kleuren acrylverf\n\u2022 Kwast\n\u2022 Glittereffect\n\u2022 Lijst\n\u2022 Schilderij op nummer\n\nEigenschappen\n\u2022 Afmetingen verpakking: 20x27x5 cm (LxBxH)\n\u2022 Met glittereffect en bijpassende lijst\n\u2022 Schilderpaneel op leeftijd (11+)\n\u2022 15 kleuren acrylverf op waterbasis\n\u2022 Serie: R', u'page_link': u'http://www.intertoys.nl/schilderen-op-nummer-dolfijnen-1', u'age': u'Vanaf 7 jaar', u'discount_price': u'', u'article_number': 1182534, u'brand': u'Ravensburger', u'title': u'Schilderen Op Nummer Dolfijnen', u'price': 17.99, u'gender': u'Beide', u'retailer': u'intertoys', u'page': 55, u'website_category': u'School & Boeken', u'description': u'Schilder jij dit romantische schilderij met dolfijnen bij zonsondergang?', u'stemming': [u'Schilderen Op Nummer Dolfijnen', u'Schilder jij dit romantische schilderij met dolfijnen bij zonsondergang?\n\nHet was nog nooit zo makkelijk om een schilderij te maken als met schilderen op nummer van Ravensburger!\n\nDe cijfers in de vakjes geven aan welke kleur verf je moet gebruiken. Volg de instructies open maak dit romantische schilderij!\n\nInhoud\n\u2022 11 Kleuren acrylverf\n\u2022 Kwast\n\u2022 Glittereffect\n\u2022 Lijst\n\u2022 Schilderij op nummer\n\nEigenschappen\n\u2022 Afmetingen verpakking: 20x27x5 cm (LxBxH)\n\u2022 Met glittereffect en bijpassende lijst\n\u2022 Schilderpaneel op leeftijd (11+)\n\u2022 15 kleuren acrylverf op waterbasis\n\u2022 Serie: R', u'schilder op nummer dolfijn schilder jij dit romantisch schild met dolfijn bij zonsondergang? het was nog nooit zo makkelijk om een schild te maak al met schilder op nummer van ravensburger! de cijfer in de vak geef aan welke kleur verf je moet bruik volg de instructie oop maak dit romantisch schilderij! inhoud \u2022 11 kleur acrylverf \u2022 kwast \u2022 glittereffect \u2022 lijst \u2022 schild op nummer einschap \u2022 afmeet verpakking: 20x27x5 cm (lxbxh) \u2022 met glittereffect en bijpas lijst \u2022 schilderpaneel op leeftijd (11+) \u2022 15 kleur acrylverf op waterbasis \u2022 serie: r'], u'folder_category': u'Knutselaars', u'img_link': u'http://static.intertoys.nl//BLKCAS/960x960/1182534.jpg'}, -2, u'http://static.intertoys.nl//BLKCAS/960x960/1182534.jpg'], [{u'description_extended': u"Bouw je ontwerp Qixel per Qixel op! Qixels zijn de blokjes die je aan elkaar hecht met water. Cre\xeber je eigen wereld met de thema-navulpakketten en kies uit drie fantastische nieuwe thema's!\nGa nu aan de slag met het thema ruimte.  \nInhoud:  \n500 x blokjes.\n1 x werkblad.\n4 x ontwerpsjablonen.\n1 x standaard.\n1 x displaystandaard.\n2 x accessoires.\n1 x tashanger met touwtje.\n1 x verstuiver.\n1 instructieboekje.\nAssortiment van 3: Ruimte, Zee, Dino.", u'page_link': u'http://www.intertoys.nl/qixels-themapakket-ruimte', u'age': u'Vanaf 4 jaar', u'discount_price': u'', u'article_number': 1389741, u'brand': u'Qixels', u'title': u'Qixels themapakket ruimte', u'price': 29.99, u'gender': u'Beide', u'retailer': u'intertoys', u'page': 54, u'website_category': u'School & Boeken', u'description': u'Qixels zijn de blokjes die je aan elkaar hecht met water. Cre\xeber je eigen wereld met de thema-navulpakketten. Ga aan de slag met het themapakket ruimte.', u'stemming': [u'Qixels themapakket ruimte', u"Bouw je ontwerp Qixel per Qixel op! Qixels zijn de blokjes die je aan elkaar hecht met water. Cre\xeber je eigen wereld met de thema-navulpakketten en kies uit drie fantastische nieuwe thema's!\nGa nu aan de slag met het thema ruimte.  \nInhoud:  \n500 x blokjes.\n1 x werkblad.\n4 x ontwerpsjablonen.\n1 x standaard.\n1 x displaystandaard.\n2 x accessoires.\n1 x tashanger met touwtje.\n1 x verstuiver.\n1 instructieboekje.\nAssortiment van 3: Ruimte, Zee, Dino.", u"qixel themapakket ruimt bouw je ontwerp qixel per qixel op! qixel zijn de blok die je aan elkaar hecht met water cre\xeber je eig wereld met de thema-navulpakket en kies uit drie fantastisch nieuwe thema's! ga nu aan de slag met het thema ruimt inhoud: 500 x blok 1 x werkblad 4 x ontwerpsjabloon 1 x standaard 1 x displaystandaard 2 x accessoir 1 x tashanger met touw 1 x verstuiver 1 instructieboek assortiment van 3: ruimte, zee, dino"], u'folder_category': u'Knutselaars', u'img_link': u'http://static.intertoys.nl//BLKCAS/960x960/1389741.jpg'}, -2, u'http://static.intertoys.nl//BLKCAS/960x960/1389741.jpg'], [{u'description_extended': u"Mandala-Designer van Ravensburger: gewoon zelf leuke Mandala's schilderen! Met maar \xe9\xe9n Ravensburger Mandala-Designer-sjabloon van Trolls kan je honderden verschillende mandala's ontwerpen. En met de bijgeleverde stiften kleur je ze vervolgens prachtig in. Gewoon de speciale sjablonen plaatsen en streep voor streep de omtrekken natekenen. Daarna kan de Mandala in verschillende kleuren ingekleurd worden. Zo maakt je stap voor stap een zelfgemaakte Mandala.", u'page_link': u'http://www.intertoys.nl/ravensburger-trolls-mandala-designer-2-in-1', u'age': u'Vanaf 6 jaar', u'discount_price': 14.99, u'article_number': 1391549, u'brand': u'Ravensburger', u'title': u'Ravensburger Trolls mandala designer 2-in-1', u'price': 17.99, u'gender': u'Beide', u'retailer': u'intertoys', u'page': 55, u'website_category': u'School & Boeken', u'description': u"Mandala-Designer van Ravensburger: gewoon zelf leuke Trolls mandala's schilderen!", u'stemming': [u'Ravensburger Trolls mandala designer 2-in-1', u"Mandala-Designer van Ravensburger: gewoon zelf leuke Mandala's schilderen! Met maar \xe9\xe9n Ravensburger Mandala-Designer-sjabloon van Trolls kan je honderden verschillende mandala's ontwerpen. En met de bijgeleverde stiften kleur je ze vervolgens prachtig in. Gewoon de speciale sjablonen plaatsen en streep voor streep de omtrekken natekenen. Daarna kan de Mandala in verschillende kleuren ingekleurd worden. Zo maakt je stap voor stap een zelfgemaakte Mandala.", u'ravensburger trol mandala designer 2-in-1 mandala-designer van ravensburger: woon zelf leuke mandala schilderen! met maar ravensburger mandala-designer-sjabloon van trol kan je honder verschil mandala ontwerp en met de bijlever stif kleur je ze vervolgen pracht in woon de special sjabloon plaats en streep voor streep de omtrek natekeen daarna kan de mandala in verschil kleur inkleur wor zo maak je stap voor stap een zelfmaak mandala'], u'folder_category': u'Knutselaars', u'img_link': u'http://static.intertoys.nl//BLKCAS/960x960/1391549.jpg'}, -2, u'http://static.intertoys.nl//BLKCAS/960x960/1391549.jpg']], 'secondRow': False, 'token': 'IJ7PMHQPAVNK6UU3C3BE3NOVXZ6MMPOJ', 'session': 'GreenOrange-session-2016-11-0714:37:26.343327', 'intype': True, 'secondchoice': False, 'log': {'feedback':'' , 'presents': '' , 'text': {'0': 'first conversation'}}, 'personality': ['Surprise', 'Schrijven', 'Geven'], 'oldmessage': 'Bedankt voor je informatie, ik ga is even op zoek naar kadootjes.', 'personQuestions': [0, 2, 1]}
# information = endodings('' ,information)
# print(information)

# def encodings(L,oldL):
#     for key, value in oldL.items():
#         key = key.encode('ascii', 'ignore')
#         if isinstance(value,str):
#             L[key] = value.encode('ascii', 'ignore')
#         else:
#             L[key] = encodings(value)
#     return L
# from bson.son import SON
# from bson.code import Code
client = MongoClient('mongodb://go:go1234@95.85.15.38:27017/toys')
db = client.toys

now = datetime.datetime.now()
d = now.isoformat()

# cursor = db.speelgoed.find()
#
# for document in cursor:
#     print(document)
tryout = {'foo': 'bar', 'baz': {'1': {'a': 'B'}}, '_id': 'AB123456789'}
def findConfig(x):
    try:
        catalogus = db.configs
        ans = list(catalogus.find({'number': x}))[0]
        for x in ans:
            if x != '_id' and x != 'number':
                return(ans[x])
    except Exception, e:
        return 'Not found any configuration'

def findUser(id):
    try:
        catalogus = db.users
        ans = list(catalogus.find({'sender': x}))[0]
        for x in ans:
            if x != '_id' and x != 'number':
                return(ans[x])
    except Exception, e:
        return None


def updateUser(id, newInformation):
    try:
        catalogus = db.users
        catalogus.update({'_id': str(id)},newInformation)
        return 'id: ' +str(id) + 'has been updated'
    except Exception, e:
        return 'Not found user',e

def insertUser(id, newInformation):
    try:
        newInformation['_id'] = str(id)
        catalogus = db.users
        print(type(newInformation))
        catalogus.insert(newInformation)
        return 'id: ' +str(id) + 'has been updated'
    except Exception, e:
        return 'Not found user because ',e

# print(updateUser(1042410335857237, information))

# add data regarding usage of user in channel
# define the payload now the example of a complete watson personality is being stored
#
# @app.route('/user/add/positive/<artnr>/<pamount>')
def addPositive(artnr, pamount):
    try:
        catalogus = db.speelgoed
        catalogus.update_one(
            {'article_number':int(artnr)},
            {'$set': {'updated': d}, '$inc': {'positive_amount':int(pamount)}}
        )
        return 'Added ' + pamount + ' positive point(s) to article :' + artnr
    except Exception, e:
        return 'Not found an article'

# add data regarding usage of user in channel
# define the payload now the example of a complete watson personality is being stored
#
# @app.route('/user/add/positive/<artnr>')
# note this function works with one negative point extracted each time used
def addDislike(artnr):
    try:
        catalogus = db.speelgoed
        catalogus.update_one(
            {'article_number':int(artnr)},
            {'$set': {'updated': d}, '$inc': {'dislike_amount':1}}
        )
        return 'Extracted 1 dislike point to article :' + artnr
    except Exception, e:
        return 'Not found an article'

# add data regarding usage of user in channel
# define the payload now the example of a complete watson personality is being stored
#
# @app.route('/user/add/score/<ref>')
def addUserScore(ref, pers, text, prod, feedback):
    try:
        user = db.users
        user.insert({
        'facebook_id': ref, # facebook id gebruiken
        'personality': pers,
        'qa': text,
        'products': prod,
        'feedback': feedback
        })
        return 'Added ' + ref
    except Exception, e:
        return 'Not found an user'

# # finding one unique toy by article number [title, brand, price, age, gender, page]
# @app.route('/article/number/<artnr>')
def findArticle(artnr):
    try:
        catalogus = db.speelgoed
        toy = catalogus.find_one({'article_number':int(artnr)})
        # return str(toy['price'])
        return 'The article you found: ' + toy['title'] + ', ' + toy['brand'] + ', ' + str(toy['price']) + ', ' + toy['age'] + ', ' + toy['gender'] +', ' + str(toy['page']) + '<br>'
    except Exception, e:
        return 'Not found an article'


# getting all articles based on title (regex part of string not case sensitive)
# @app.route('/articles/title/<the_query>')
def findArticlesTitle(the_query):
    try:
        catalogus = db.speelgoed
        results = catalogus.find(
        {'title': {'$regex': '.*'+the_query+'.*','$options' : 'i'}}
        )
        return list(results)
    except Exception, e:
        return 'Not found'

# getting all articles based on title and description_extended (regex part of string not case sensitive)
# @app.route('/articles/<the_query>')
def findArticlesTitleAndDescription(the_query):
    try:
        catalogus = db.speelgoed
        data = list(catalogus.find({'$or': [{'title': {'$regex': '.*'+the_query+'.*','$options' : 'i'}},{'description_extended': {'$regex': '.*'+the_query+'.*','$options' : 'i'}} ]}))
        return data
    except Exception, e:
        return 'Not found'

# getting all articles [title, brand, price, age, gender, page]
# @app.route('/articles')
def findAllArticles():
    try:
        catalogus = db.speelgoed
        results = catalogus.find()
        return(list(results))
        # output = ''
        # for r in results:
        #     output += r['title'] + ', ' + r['brand'] + ', ' + str(r['price']) + ', ' + r['age'] + ', ' + r['gender'] +', ' + str(r['page']) + '<br>'
        # return output
    except Exception, e:
        return 'Not found'

# getting all articles that are aprox. price (plus and minus 15%)
# @app.route('/articles/price/<the_price>')
def findByPrice(the_price):
    try:
        the_price_low = float(the_price) - float(the_price)/6.6
        the_price_high = float(the_price)/6.6 + float(the_price)
        catalogus = db.speelgoed
        results = catalogus.find({'$and': [{'price': {'$lt':the_price_high}},{'price': {'$gt':the_price_low}} ]})
        ordered = results.sort('price')
        output = ''
        for r in ordered:
            output += r['title'] + ' - '+ str(r['price']) + '<br>'
        # return str(the_price_low) + ' and ' + str(the_price_high)
        return output
    except Exception, e:
        return 'Not found'

# getting all articles under 50 euro
# @app.route('/articles/under')
def findUndervalue():
    try:
        catalogus = db.speelgoed
        results = catalogus.find({'$and': [{'price': {'$lt':50}},{'price': {'$gt':0}} ]})
        ordered = results.sort('price')
        output = ''
        for r in ordered:
            output += r['title'] + ' - '+ str(r['price']) + '<br>'
        return output
    except Exception, e:
        return 'Not found'

# getting all articles above 50 euro
# @app.route('/articles/above')
def findAbovevalue():
    try:
        catalogus = db.speelgoed
        results = catalogus.find({'price': {'$gt':50}})
        ordered = results.sort('price')
        output = ''
        for r in ordered:
            output += r['title'] + ' - '+ str(r['price']) + '<br>'
        return output
    except Exception, e:
        return 'Not found'

# getting all articles within price range
# @app.route('/articles/price/range/<start>/<end>')
def findFromRange(start, end):
    try:
        aa = float(start)
        bb = float(end)
        catalogus = db.speelgoed
        results = list(catalogus.find({'$and': [{'price': {'$lt':bb}},{'price': {'$gt':aa}} ]}))
        return results
    except Exception, e:
        return 'Not found'

# getting all articles based on gender (Jongen / Meisje / Beide)
# @app.route('/articles/gender/<sex>')
def findArticlesGender(sex):
    try:
        catalogus = db.speelgoed
        results = list(catalogus.find({'gender': sex}))
        # ordered = results.sort('price')
        # output = ''
        # for r in ordered:
        #     output += r['title'] + ' - '+ str(r['price']) + '<br>'
        return results
    except Exception, e:
        return 'Not found'

# getting all articles based on brand (regex part of string not case sensitive)
# @app.route('/articles/brand/<the_brand>')
def findArticlesBrand(the_brand):
    try:
        catalogus = db.speelgoed
        results = catalogus.find({'brand': {'$regex': '.*'+the_brand+'.*','$options' : 'i'}})
        ordered = results.sort('price')
        output = ''
        for r in ordered:
            output += r['title'] + ' - '+ str(r['price']) + '<br>'
        return output
    except Exception, e:
        return 'Not found'

def findArticlesCategory(category):
    try:
        catalogus = db.speelgoed
        results = list(catalogus.find({'folder_category': category}))
        return results
    except Exception, e:
        return 'Not found'

def findArticlesStemming(the_query):
    try:
        catalogus = db.speelgoed
        data = list(catalogus.find({'stemming.2': {'$regex': '.*'+the_query+'.*','$options' : 'i'}}))
        return data
    except Exception, e:
        return 'Not found'

# finding one unique toy by article number [title, brand, price, age, gender, page]
# @app.route('/articles/by/age/year/<jaar>')
def findByAge(jaar):
    try:
        # append this madness dictionary regarding age
        query = [{'age': 'alle leeftijden'}]
        if jaar == '0':
            query.append({'age': 'Vanaf 0 maanden'})
            query.append({'age': '0 jaar tot 1 jaar'})
            query.append({'age': '0 jaar tot 2 jaar'})
            query.append({'age': '0 jaar tot 3 jaar'})
            query.append({'age': '0 maanden tot 3 jaar'})
            query.append({'age': '0 maanden tot 4 jaar'})
            query.append({'age': '0 maanden tot 5 jaar'})
            query.append({'age': '3 maanden tot 1 jaar'})
            query.append({'age': 'Tot 12 maanden'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '1':
            query.append({'age': '1 jaar tot 3 jaar'})
            query.append({'age': '1 jaar tot 4 jaar'})
            query.append({'age': '1 jaar tot 5 jaar'})
            query.append({'age': '1 jaar tot 6 jaar'})
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': '1,5 jaar tot 3 jaar'})
            query.append({'age': '1,5 jaar tot 4 jaar'})
            query.append({'age': '1,5 jaar tot 5 jaar'})
            query.append({'age': '1,5 jaar tot 8 jaar'})
            query.append({'age': '1,5 jaar tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '2':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': '1 jaar tot 3 jaar'})
            query.append({'age': '1 jaar tot 4 jaar'})
            query.append({'age': '1 jaar tot 5 jaar'})
            query.append({'age': '1 jaar tot 6 jaar'})
            query.append({'age': '2 jaar tot 3 jaar'})
            query.append({'age': '2 jaar tot 4 jaar'})
            query.append({'age': '2 jaar tot 5 jaar'})
            query.append({'age': '2 jaar tot 6 jaar'})
            query.append({'age': '2 jaar tot 8 jaar'})
            query.append({'age': '2,5 jaar tot 4 jaar'})
            query.append({'age': '2,5 jaar tot 5 jaar'})
            query.append({'age': '2,5 jaar tot 6 jaar'})
            query.append({'age': '6 maanden tot 3 jaar'})
            query.append({'age': '6 maanden tot 4 jaar'})
            query.append({'age': '10 maanden tot 3 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '3':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': '1 jaar tot 4 jaar'})
            query.append({'age': '1 jaar tot 5 jaar'})
            query.append({'age': '1 jaar tot 6 jaar'})
            query.append({'age': '2 jaar tot 4 jaar'})
            query.append({'age': '2 jaar tot 5 jaar'})
            query.append({'age': '2 jaar tot 6 jaar'})
            query.append({'age': '2 jaar tot 8 jaar'})
            query.append({'age': '2,5 jaar tot 4 jaar'})
            query.append({'age': '2,5 jaar tot 5 jaar'})
            query.append({'age': '2,5 jaar tot 6 jaar'})
            query.append({'age': '3 jaar tot 4 jaar'})
            query.append({'age': '3 jaar tot 5 jaar'})
            query.append({'age': '3 jaar tot 6 jaar'})
            query.append({'age': '3 jaar tot 8 jaar'})
            query.append({'age': '3 jaar tot 10 jaar'})
            query.append({'age': '3 jaar tot 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': 'Vanaf 3 tot 8 jaar'})
            query.append({'age': 'Vanaf 3 tot 11 jaar'})
            query.append({'age': 'Vanaf 3 tot 12 jaar'})
            query.append({'age': 'Vanaf 3 tot 99 jaar'})
            query.append({'age': '6 maanden tot 4 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '4':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': '1 jaar tot 5 jaar'})
            query.append({'age': '1 jaar tot 6 jaar'})
            query.append({'age': '2 jaar tot 5 jaar'})
            query.append({'age': '2 jaar tot 6 jaar'})
            query.append({'age': '2 jaar tot 8 jaar'})
            query.append({'age': '2,5 jaar tot 5 jaar'})
            query.append({'age': '2,5 jaar tot 6 jaar'})
            query.append({'age': '3 jaar tot 5 jaar'})
            query.append({'age': '3 jaar tot 6 jaar'})
            query.append({'age': '3 jaar tot 8 jaar'})
            query.append({'age': '3 jaar tot 10 jaar'})
            query.append({'age': '3 jaar tot 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '4 jaar tot 6 jaar'})
            query.append({'age': '4 jaar tot 8 jaar'})
            query.append({'age': '4 jaar tot 10 jaar'})
            query.append({'age': '4 jaar tot 11 jaar'})
            query.append({'age': '4 jaar tot 12 jaar'})
            query.append({'age': 'Vanaf 4 tot 7 jaar'})
            query.append({'age': 'Vanaf 4 tot 10 jaar'})
            query.append({'age': 'Vanaf 4 tot 11 jaar'})
            query.append({'age': 'Vanaf 4 tot 12 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '5':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': '1 jaar tot 6 jaar'})
            query.append({'age': '2 jaar tot 6 jaar'})
            query.append({'age': '2 jaar tot 8 jaar'})
            query.append({'age': '2,5 jaar tot 6 jaar'})
            query.append({'age': '3 jaar tot 6 jaar'})
            query.append({'age': '3 jaar tot 8 jaar'})
            query.append({'age': '3 jaar tot 10 jaar'})
            query.append({'age': '3 jaar tot 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '4 jaar tot 6 jaar'})
            query.append({'age': '4 jaar tot 8 jaar'})
            query.append({'age': '4 jaar tot 10 jaar'})
            query.append({'age': '4 jaar tot 11 jaar'})
            query.append({'age': '4 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 8 jaar'})
            query.append({'age': '5 jaar tot 10 jaar'})
            query.append({'age': '5 jaar tot 11 jaar'})
            query.append({'age': '5 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': '6 jaar tot 8 jaar'})
            query.append({'age': '6 jaar tot 10 jaar'})
            query.append({'age': '6 jaar tot 12 jaar'})
            query.append({'age': 'Vanaf 4 tot 7 jaar'})
            query.append({'age': 'Vanaf 4 tot 10 jaar'})
            query.append({'age': 'Vanaf 4 tot 12 jaar'})
            query.append({'age': 'Vanaf 5 tot 10 jaar'})
            query.append({'age': 'Vanaf 5 tot 11 jaar'})
            query.append({'age': 'Vanaf 5 tot 12 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '6':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': '2 jaar tot 8 jaar'})
            query.append({'age': '3 jaar tot 8 jaar'})
            query.append({'age': '3 jaar tot 10 jaar'})
            query.append({'age': '3 jaar tot 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '4 jaar tot 8 jaar'})
            query.append({'age': '4 jaar tot 10 jaar'})
            query.append({'age': '4 jaar tot 11 jaar'})
            query.append({'age': '4 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 8 jaar'})
            query.append({'age': '5 jaar tot 10 jaar'})
            query.append({'age': '5 jaar tot 11 jaar'})
            query.append({'age': '5 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': 'Vanaf 4 tot 7 jaar'})
            query.append({'age': 'Vanaf 4 tot 10 jaar'})
            query.append({'age': 'Vanaf 4 tot 12 jaar'})
            query.append({'age': 'Vanaf 5 tot 10 jaar'})
            query.append({'age': 'Vanaf 5 tot 11 jaar'})
            query.append({'age': 'Vanaf 5 tot 12 jaar'})
            query.append({'age': 'Vanaf 6 tot 14 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '7':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': '2 jaar tot 8 jaar'})
            query.append({'age': '3 jaar tot 8 jaar'})
            query.append({'age': '3 jaar tot 10 jaar'})
            query.append({'age': '3 jaar tot 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '4 jaar tot 8 jaar'})
            query.append({'age': '4 jaar tot 10 jaar'})
            query.append({'age': '4 jaar tot 11 jaar'})
            query.append({'age': '4 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 8 jaar'})
            query.append({'age': '5 jaar tot 10 jaar'})
            query.append({'age': '5 jaar tot 11 jaar'})
            query.append({'age': '5 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': 'Vanaf 4 tot 10 jaar'})
            query.append({'age': 'Vanaf 4 tot 12 jaar'})
            query.append({'age': 'Vanaf 5 tot 10 jaar'})
            query.append({'age': 'Vanaf 5 tot 11 jaar'})
            query.append({'age': 'Vanaf 5 tot 12 jaar'})
            query.append({'age': 'Vanaf 6 tot 14 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': 'vanaf 7 tot 12 jaar'})
            query.append({'age': 'vanaf 7 tot 14 jaar'})
            query.append({'age': 'Vanaf 7 tot 12 jaar'})
            query.append({'age': 'Vanaf 7 tot 14 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '8':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': '3 jaar tot 10 jaar'})
            query.append({'age': '3 jaar tot 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '4 jaar tot 10 jaar'})
            query.append({'age': '4 jaar tot 11 jaar'})
            query.append({'age': '4 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 10 jaar'})
            query.append({'age': '5 jaar tot 11 jaar'})
            query.append({'age': '5 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': 'Vanaf 4 tot 10 jaar'})
            query.append({'age': 'Vanaf 4 tot 12 jaar'})
            query.append({'age': 'Vanaf 5 tot 10 jaar'})
            query.append({'age': 'Vanaf 5 tot 11 jaar'})
            query.append({'age': 'Vanaf 5 tot 12 jaar'})
            query.append({'age': 'Vanaf 6 tot 14 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': 'vanaf 7 tot 12 jaar'})
            query.append({'age': 'vanaf 7 tot 14 jaar'})
            query.append({'age': 'Vanaf 7 tot 12 jaar'})
            query.append({'age': 'Vanaf 7 tot 14 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '9':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': '3 jaar tot 10 jaar'})
            query.append({'age': '3 jaar tot 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '4 jaar tot 10 jaar'})
            query.append({'age': '4 jaar tot 11 jaar'})
            query.append({'age': '4 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 10 jaar'})
            query.append({'age': '5 jaar tot 11 jaar'})
            query.append({'age': '5 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': 'Vanaf 4 tot 10 jaar'})
            query.append({'age': 'Vanaf 4 tot 12 jaar'})
            query.append({'age': 'Vanaf 5 tot 10 jaar'})
            query.append({'age': 'Vanaf 5 tot 11 jaar'})
            query.append({'age': 'Vanaf 5 tot 12 jaar'})
            query.append({'age': 'Vanaf 6 tot 14 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': 'vanaf 7 tot 12 jaar'})
            query.append({'age': 'vanaf 7 tot 14 jaar'})
            query.append({'age': 'Vanaf 7 tot 12 jaar'})
            query.append({'age': 'Vanaf 7 tot 14 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '10':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': 'vanaf 10 jaar'})
            query.append({'age': 'Vanaf 10 jaar'})
            query.append({'age': '3 jaar tot 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '4 jaar tot 11 jaar'})
            query.append({'age': '4 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 11 jaar'})
            query.append({'age': '5 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': 'Vanaf 4 tot 12 jaar'})
            query.append({'age': 'Vanaf 5 tot 11 jaar'})
            query.append({'age': 'Vanaf 5 tot 12 jaar'})
            query.append({'age': 'Vanaf 6 tot 14 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': 'vanaf 7 tot 12 jaar'})
            query.append({'age': 'vanaf 7 tot 14 jaar'})
            query.append({'age': 'Vanaf 7 tot 12 jaar'})
            query.append({'age': 'Vanaf 7 tot 14 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '11':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': 'vanaf 10 jaar'})
            query.append({'age': 'Vanaf 10 jaar'})
            query.append({'age': '3 jaar tot 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '4 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': 'Vanaf 4 tot 12 jaar'})
            query.append({'age': 'Vanaf 5 tot 12 jaar'})
            query.append({'age': 'Vanaf 6 tot 14 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': 'vanaf 7 tot 12 jaar'})
            query.append({'age': 'vanaf 7 tot 14 jaar'})
            query.append({'age': 'Vanaf 7 tot 12 jaar'})
            query.append({'age': 'Vanaf 7 tot 14 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
            query.append({'age': ''})
        elif jaar == '12':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': 'vanaf 10 jaar'})
            query.append({'age': 'Vanaf 10 jaar'})
            query.append({'age': 'vanaf 12 jaar'})
            query.append({'age': 'Vanaf 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': 'Vanaf 6 tot 14 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': 'vanaf 7 tot 14 jaar'})
            query.append({'age': 'Vanaf 7 tot 14 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
            query.append({'age': ''})
        elif jaar == '13':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': 'vanaf 10 jaar'})
            query.append({'age': 'Vanaf 10 jaar'})
            query.append({'age': 'vanaf 12 jaar'})
            query.append({'age': 'Vanaf 12 jaar'})
            query.append({'age': 'vanaf 13 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': 'Vanaf 6 tot 14 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': 'vanaf 7 tot 14 jaar'})
            query.append({'age': 'Vanaf 7 tot 14 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
            query.append({'age': ''})
        elif jaar == '14':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': 'vanaf 10 jaar'})
            query.append({'age': 'Vanaf 10 jaar'})
            query.append({'age': 'vanaf 12 jaar'})
            query.append({'age': 'Vanaf 12 jaar'})
            query.append({'age': 'vanaf 13 jaar'})
            query.append({'age': 'vanaf 14 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
            query.append({'age': ''})
        elif jaar == '15':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': 'vanaf 10 jaar'})
            query.append({'age': 'Vanaf 10 jaar'})
            query.append({'age': 'vanaf 12 jaar'})
            query.append({'age': 'Vanaf 12 jaar'})
            query.append({'age': 'vanaf 13 jaar'})
            query.append({'age': 'vanaf 14 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
            query.append({'age': ''})
        elif jaar == '16':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': 'vanaf 10 jaar'})
            query.append({'age': 'Vanaf 10 jaar'})
            query.append({'age': 'vanaf 12 jaar'})
            query.append({'age': 'Vanaf 12 jaar'})
            query.append({'age': 'vanaf 13 jaar'})
            query.append({'age': 'vanaf 14 jaar'})
            query.append({'age': 'vanaf 16 jaar'})
            query.append({'age': 'Vanaf 16 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
            query.append({'age': ''})
        elif jaar == '17':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': 'vanaf 10 jaar'})
            query.append({'age': 'Vanaf 10 jaar'})
            query.append({'age': 'vanaf 12 jaar'})
            query.append({'age': 'Vanaf 12 jaar'})
            query.append({'age': 'vanaf 13 jaar'})
            query.append({'age': 'vanaf 14 jaar'})
            query.append({'age': 'vanaf 16 jaar'})
            query.append({'age': 'Vanaf 16 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
            query.append({'age': ''})
        else:
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': 'vanaf 10 jaar'})
            query.append({'age': 'Vanaf 10 jaar'})
            query.append({'age': 'vanaf 12 jaar'})
            query.append({'age': 'Vanaf 12 jaar'})
            query.append({'age': 'vanaf 13 jaar'})
            query.append({'age': 'vanaf 14 jaar'})
            query.append({'age': 'vanaf 16 jaar'})
            query.append({'age': 'Vanaf 16 jaar'})
            query.append({'age': 'vanaf 18 jaar'})
            query.append({'age': 'Vanaf 18 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
            query.append({'age': ''})

        catalogus = db.speelgoed
        # get query dict working
        results = catalogus.find({'$or': query})
        return(list(results))
        # ordered = results.sort('price')
        # output = ''
        # for r in ordered:
        #     output += r['title'] + ' | '+ r['age'] + ' | ' + str(r['price']) +'<br>'
        # return output
    except Exception, e:
        return 'Not found an article'


def findRightProduct(geslacht, budget, age, category, idea,n):
    # print((geslacht, budget, age, category, idea,n))
    idea = idea.lower()
    idea = idea.replace('een ', '').replace('de ', '' ).replace('het ', '')
    ideaStem = ' '.join([kpss.stem(word) for word in idea.split()])
    geslachtQuery = findArticlesGender(geslacht)
    budgetQuery = findFromRange(budget[0],budget[1])
    ageQuery = findByAge(age)
    if idea == '':
        ideaStem = 'jaa'
        ideaQuery = []
        titleQuery = []
        stemQuery = []
    else:
        ideaQuery = findArticlesTitleAndDescription(idea)
        stemQuery = findArticlesStemming(ideaStem)
        titleQuery = findArticlesTitle(idea)
    categoryQuery = findArticlesCategory(category)
    allProducts = geslachtQuery + budgetQuery + ageQuery + ideaQuery + stemQuery + titleQuery + categoryQuery
    #     print(x)
    uniqueProducts = dict((v['_id'],v) for v in allProducts).values()
    uniqueProducts = [[x,0] for x in uniqueProducts]
    # print(len(uniqueProducts))
    finalScore = []
    for x in uniqueProducts:
        a = 0
        if x[0] in titleQuery:
            a+=5
        else:
            a-=5
        if x[0] in ideaQuery:
            a+=2
        else:
            a-=2
        if x[0] in stemQuery:
            a+=2
        else:
            a-=2
        if x[0] in categoryQuery:
            a+=3
        else:
            a-=3
        if x[0] in ageQuery:
            a+=4
        else:
            a-=4
        if x[0] in budgetQuery:
            a+=4
        else:
            a-=4
        if x[0] in geslachtQuery:
            a+=4
        else:
            a-=4
        finalScore.append([x[0],a])
    finalScore = sorted(finalScore, key=lambda x: x[1])
    high = finalScore[-1][1]
    # print(len([x for x in finalScore if x[1] == high]))
    # print(finalScore[-n:])
    return finalScore[-n:]

def printprod(L):
    for x in L:
        print(x[0]['title'], x[1])
# printprod(findRightProduct('Jongen', [30,45], '14', 'Gadget- en gamekings', 'Een drone',3))
#
# # finding one unique toy by article number [title, brand, price, age, gender, page, img_link]
# @app.route('/articles/<geslacht>/<budget>/<bedrag>/age/<jaar>')
def findByTrinity(geslacht,budget,bedrag,jaar):
    try:
        # append this madness dictionary regarding age
        query = [{'age': 'alle leeftijden'}]
        if jaar == '0':
            query.append({'age': 'Vanaf 0 maanden'})
            query.append({'age': '0 jaar tot 1 jaar'})
            query.append({'age': '0 jaar tot 2 jaar'})
            query.append({'age': '0 jaar tot 3 jaar'})
            query.append({'age': '0 maanden tot 3 jaar'})
            query.append({'age': '0 maanden tot 4 jaar'})
            query.append({'age': '0 maanden tot 5 jaar'})
            query.append({'age': '3 maanden tot 1 jaar'})
            query.append({'age': 'Tot 12 maanden'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '1':
            query.append({'age': '1 jaar tot 3 jaar'})
            query.append({'age': '1 jaar tot 4 jaar'})
            query.append({'age': '1 jaar tot 5 jaar'})
            query.append({'age': '1 jaar tot 6 jaar'})
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': '1,5 jaar tot 3 jaar'})
            query.append({'age': '1,5 jaar tot 4 jaar'})
            query.append({'age': '1,5 jaar tot 5 jaar'})
            query.append({'age': '1,5 jaar tot 8 jaar'})
            query.append({'age': '1,5 jaar tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '2':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': '1 jaar tot 3 jaar'})
            query.append({'age': '1 jaar tot 4 jaar'})
            query.append({'age': '1 jaar tot 5 jaar'})
            query.append({'age': '1 jaar tot 6 jaar'})
            query.append({'age': '2 jaar tot 3 jaar'})
            query.append({'age': '2 jaar tot 4 jaar'})
            query.append({'age': '2 jaar tot 5 jaar'})
            query.append({'age': '2 jaar tot 6 jaar'})
            query.append({'age': '2 jaar tot 8 jaar'})
            query.append({'age': '2,5 jaar tot 4 jaar'})
            query.append({'age': '2,5 jaar tot 5 jaar'})
            query.append({'age': '2,5 jaar tot 6 jaar'})
            query.append({'age': '6 maanden tot 3 jaar'})
            query.append({'age': '6 maanden tot 4 jaar'})
            query.append({'age': '10 maanden tot 3 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '3':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': '1 jaar tot 4 jaar'})
            query.append({'age': '1 jaar tot 5 jaar'})
            query.append({'age': '1 jaar tot 6 jaar'})
            query.append({'age': '2 jaar tot 4 jaar'})
            query.append({'age': '2 jaar tot 5 jaar'})
            query.append({'age': '2 jaar tot 6 jaar'})
            query.append({'age': '2 jaar tot 8 jaar'})
            query.append({'age': '2,5 jaar tot 4 jaar'})
            query.append({'age': '2,5 jaar tot 5 jaar'})
            query.append({'age': '2,5 jaar tot 6 jaar'})
            query.append({'age': '3 jaar tot 4 jaar'})
            query.append({'age': '3 jaar tot 5 jaar'})
            query.append({'age': '3 jaar tot 6 jaar'})
            query.append({'age': '3 jaar tot 8 jaar'})
            query.append({'age': '3 jaar tot 10 jaar'})
            query.append({'age': '3 jaar tot 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': 'Vanaf 3 tot 8 jaar'})
            query.append({'age': 'Vanaf 3 tot 11 jaar'})
            query.append({'age': 'Vanaf 3 tot 12 jaar'})
            query.append({'age': 'Vanaf 3 tot 99 jaar'})
            query.append({'age': '6 maanden tot 4 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '4':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': '1 jaar tot 5 jaar'})
            query.append({'age': '1 jaar tot 6 jaar'})
            query.append({'age': '2 jaar tot 5 jaar'})
            query.append({'age': '2 jaar tot 6 jaar'})
            query.append({'age': '2 jaar tot 8 jaar'})
            query.append({'age': '2,5 jaar tot 5 jaar'})
            query.append({'age': '2,5 jaar tot 6 jaar'})
            query.append({'age': '3 jaar tot 5 jaar'})
            query.append({'age': '3 jaar tot 6 jaar'})
            query.append({'age': '3 jaar tot 8 jaar'})
            query.append({'age': '3 jaar tot 10 jaar'})
            query.append({'age': '3 jaar tot 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '4 jaar tot 6 jaar'})
            query.append({'age': '4 jaar tot 8 jaar'})
            query.append({'age': '4 jaar tot 10 jaar'})
            query.append({'age': '4 jaar tot 11 jaar'})
            query.append({'age': '4 jaar tot 12 jaar'})
            query.append({'age': 'Vanaf 4 tot 7 jaar'})
            query.append({'age': 'Vanaf 4 tot 10 jaar'})
            query.append({'age': 'Vanaf 4 tot 11 jaar'})
            query.append({'age': 'Vanaf 4 tot 12 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '5':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': '1 jaar tot 6 jaar'})
            query.append({'age': '2 jaar tot 6 jaar'})
            query.append({'age': '2 jaar tot 8 jaar'})
            query.append({'age': '2,5 jaar tot 6 jaar'})
            query.append({'age': '3 jaar tot 6 jaar'})
            query.append({'age': '3 jaar tot 8 jaar'})
            query.append({'age': '3 jaar tot 10 jaar'})
            query.append({'age': '3 jaar tot 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '4 jaar tot 6 jaar'})
            query.append({'age': '4 jaar tot 8 jaar'})
            query.append({'age': '4 jaar tot 10 jaar'})
            query.append({'age': '4 jaar tot 11 jaar'})
            query.append({'age': '4 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 8 jaar'})
            query.append({'age': '5 jaar tot 10 jaar'})
            query.append({'age': '5 jaar tot 11 jaar'})
            query.append({'age': '5 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': '6 jaar tot 8 jaar'})
            query.append({'age': '6 jaar tot 10 jaar'})
            query.append({'age': '6 jaar tot 12 jaar'})
            query.append({'age': 'Vanaf 4 tot 7 jaar'})
            query.append({'age': 'Vanaf 4 tot 10 jaar'})
            query.append({'age': 'Vanaf 4 tot 12 jaar'})
            query.append({'age': 'Vanaf 5 tot 10 jaar'})
            query.append({'age': 'Vanaf 5 tot 11 jaar'})
            query.append({'age': 'Vanaf 5 tot 12 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '6':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': '2 jaar tot 8 jaar'})
            query.append({'age': '3 jaar tot 8 jaar'})
            query.append({'age': '3 jaar tot 10 jaar'})
            query.append({'age': '3 jaar tot 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '4 jaar tot 8 jaar'})
            query.append({'age': '4 jaar tot 10 jaar'})
            query.append({'age': '4 jaar tot 11 jaar'})
            query.append({'age': '4 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 8 jaar'})
            query.append({'age': '5 jaar tot 10 jaar'})
            query.append({'age': '5 jaar tot 11 jaar'})
            query.append({'age': '5 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': 'Vanaf 4 tot 7 jaar'})
            query.append({'age': 'Vanaf 4 tot 10 jaar'})
            query.append({'age': 'Vanaf 4 tot 12 jaar'})
            query.append({'age': 'Vanaf 5 tot 10 jaar'})
            query.append({'age': 'Vanaf 5 tot 11 jaar'})
            query.append({'age': 'Vanaf 5 tot 12 jaar'})
            query.append({'age': 'Vanaf 6 tot 14 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '7':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': '2 jaar tot 8 jaar'})
            query.append({'age': '3 jaar tot 8 jaar'})
            query.append({'age': '3 jaar tot 10 jaar'})
            query.append({'age': '3 jaar tot 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '4 jaar tot 8 jaar'})
            query.append({'age': '4 jaar tot 10 jaar'})
            query.append({'age': '4 jaar tot 11 jaar'})
            query.append({'age': '4 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 8 jaar'})
            query.append({'age': '5 jaar tot 10 jaar'})
            query.append({'age': '5 jaar tot 11 jaar'})
            query.append({'age': '5 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': 'Vanaf 4 tot 10 jaar'})
            query.append({'age': 'Vanaf 4 tot 12 jaar'})
            query.append({'age': 'Vanaf 5 tot 10 jaar'})
            query.append({'age': 'Vanaf 5 tot 11 jaar'})
            query.append({'age': 'Vanaf 5 tot 12 jaar'})
            query.append({'age': 'Vanaf 6 tot 14 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': 'vanaf 7 tot 12 jaar'})
            query.append({'age': 'vanaf 7 tot 14 jaar'})
            query.append({'age': 'Vanaf 7 tot 12 jaar'})
            query.append({'age': 'Vanaf 7 tot 14 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '8':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': '3 jaar tot 10 jaar'})
            query.append({'age': '3 jaar tot 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '4 jaar tot 10 jaar'})
            query.append({'age': '4 jaar tot 11 jaar'})
            query.append({'age': '4 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 10 jaar'})
            query.append({'age': '5 jaar tot 11 jaar'})
            query.append({'age': '5 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': 'Vanaf 4 tot 10 jaar'})
            query.append({'age': 'Vanaf 4 tot 12 jaar'})
            query.append({'age': 'Vanaf 5 tot 10 jaar'})
            query.append({'age': 'Vanaf 5 tot 11 jaar'})
            query.append({'age': 'Vanaf 5 tot 12 jaar'})
            query.append({'age': 'Vanaf 6 tot 14 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': 'vanaf 7 tot 12 jaar'})
            query.append({'age': 'vanaf 7 tot 14 jaar'})
            query.append({'age': 'Vanaf 7 tot 12 jaar'})
            query.append({'age': 'Vanaf 7 tot 14 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '9':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': '3 jaar tot 10 jaar'})
            query.append({'age': '3 jaar tot 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '4 jaar tot 10 jaar'})
            query.append({'age': '4 jaar tot 11 jaar'})
            query.append({'age': '4 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 10 jaar'})
            query.append({'age': '5 jaar tot 11 jaar'})
            query.append({'age': '5 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': 'Vanaf 4 tot 10 jaar'})
            query.append({'age': 'Vanaf 4 tot 12 jaar'})
            query.append({'age': 'Vanaf 5 tot 10 jaar'})
            query.append({'age': 'Vanaf 5 tot 11 jaar'})
            query.append({'age': 'Vanaf 5 tot 12 jaar'})
            query.append({'age': 'Vanaf 6 tot 14 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': 'vanaf 7 tot 12 jaar'})
            query.append({'age': 'vanaf 7 tot 14 jaar'})
            query.append({'age': 'Vanaf 7 tot 12 jaar'})
            query.append({'age': 'Vanaf 7 tot 14 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '10':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': 'vanaf 10 jaar'})
            query.append({'age': 'Vanaf 10 jaar'})
            query.append({'age': '3 jaar tot 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '4 jaar tot 11 jaar'})
            query.append({'age': '4 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 11 jaar'})
            query.append({'age': '5 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': 'Vanaf 4 tot 12 jaar'})
            query.append({'age': 'Vanaf 5 tot 11 jaar'})
            query.append({'age': 'Vanaf 5 tot 12 jaar'})
            query.append({'age': 'Vanaf 6 tot 14 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': 'vanaf 7 tot 12 jaar'})
            query.append({'age': 'vanaf 7 tot 14 jaar'})
            query.append({'age': 'Vanaf 7 tot 12 jaar'})
            query.append({'age': 'Vanaf 7 tot 14 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
        elif jaar == '11':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': 'vanaf 10 jaar'})
            query.append({'age': 'Vanaf 10 jaar'})
            query.append({'age': '3 jaar tot 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '4 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 12 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': 'Vanaf 4 tot 12 jaar'})
            query.append({'age': 'Vanaf 5 tot 12 jaar'})
            query.append({'age': 'Vanaf 6 tot 14 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': 'vanaf 7 tot 12 jaar'})
            query.append({'age': 'vanaf 7 tot 14 jaar'})
            query.append({'age': 'Vanaf 7 tot 12 jaar'})
            query.append({'age': 'Vanaf 7 tot 14 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
            query.append({'age': ''})
        elif jaar == '12':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': 'vanaf 10 jaar'})
            query.append({'age': 'Vanaf 10 jaar'})
            query.append({'age': 'vanaf 12 jaar'})
            query.append({'age': 'Vanaf 12 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': 'Vanaf 6 tot 14 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': 'vanaf 7 tot 14 jaar'})
            query.append({'age': 'Vanaf 7 tot 14 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
            query.append({'age': ''})
        elif jaar == '13':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': 'vanaf 10 jaar'})
            query.append({'age': 'Vanaf 10 jaar'})
            query.append({'age': 'vanaf 12 jaar'})
            query.append({'age': 'Vanaf 12 jaar'})
            query.append({'age': 'vanaf 13 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': 'Vanaf 6 tot 14 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': 'vanaf 7 tot 14 jaar'})
            query.append({'age': 'Vanaf 7 tot 14 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
            query.append({'age': ''})
        elif jaar == '14':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': 'vanaf 10 jaar'})
            query.append({'age': 'Vanaf 10 jaar'})
            query.append({'age': 'vanaf 12 jaar'})
            query.append({'age': 'Vanaf 12 jaar'})
            query.append({'age': 'vanaf 13 jaar'})
            query.append({'age': 'vanaf 14 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': '5 jaar tot 15 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
            query.append({'age': ''})
        elif jaar == '15':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': 'vanaf 10 jaar'})
            query.append({'age': 'Vanaf 10 jaar'})
            query.append({'age': 'vanaf 12 jaar'})
            query.append({'age': 'Vanaf 12 jaar'})
            query.append({'age': 'vanaf 13 jaar'})
            query.append({'age': 'vanaf 14 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
            query.append({'age': ''})
        elif jaar == '16':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': 'vanaf 10 jaar'})
            query.append({'age': 'Vanaf 10 jaar'})
            query.append({'age': 'vanaf 12 jaar'})
            query.append({'age': 'Vanaf 12 jaar'})
            query.append({'age': 'vanaf 13 jaar'})
            query.append({'age': 'vanaf 14 jaar'})
            query.append({'age': 'vanaf 16 jaar'})
            query.append({'age': 'Vanaf 16 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
            query.append({'age': ''})
        elif jaar == '17':
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': 'vanaf 10 jaar'})
            query.append({'age': 'Vanaf 10 jaar'})
            query.append({'age': 'vanaf 12 jaar'})
            query.append({'age': 'Vanaf 12 jaar'})
            query.append({'age': 'vanaf 13 jaar'})
            query.append({'age': 'vanaf 14 jaar'})
            query.append({'age': 'vanaf 16 jaar'})
            query.append({'age': 'Vanaf 16 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
            query.append({'age': ''})
        else:
            query.append({'age': 'vanaf 1 jaar'})
            query.append({'age': 'vanaf 1,5 jaar'})
            query.append({'age': 'vanaf 2 jaar'})
            query.append({'age': 'Vanaf 1 jaar'})
            query.append({'age': 'Vanaf 1,5 jaar'})
            query.append({'age': 'Vanaf 2 jaar'})
            query.append({'age': 'vanaf 3 jaar'})
            query.append({'age': 'Vanaf 3 jaar'})
            query.append({'age': 'vanaf 4 jaar'})
            query.append({'age': 'Vanaf 4 jaar'})
            query.append({'age': 'vanaf 5 jaar'})
            query.append({'age': 'Vanaf 5 jaar'})
            query.append({'age': 'vanaf 6 jaar'})
            query.append({'age': 'Vanaf 6 jaar'})
            query.append({'age': 'vanaf 7 jaar'})
            query.append({'age': 'Vanaf 7 jaar'})
            query.append({'age': 'vanaf 8 jaar'})
            query.append({'age': 'Vanaf 8 jaar'})
            query.append({'age': 'vanaf 9 jaar'})
            query.append({'age': 'Vanaf 9 jaar'})
            query.append({'age': 'vanaf 10 jaar'})
            query.append({'age': 'Vanaf 10 jaar'})
            query.append({'age': 'vanaf 12 jaar'})
            query.append({'age': 'Vanaf 12 jaar'})
            query.append({'age': 'vanaf 13 jaar'})
            query.append({'age': 'vanaf 14 jaar'})
            query.append({'age': 'vanaf 16 jaar'})
            query.append({'age': 'Vanaf 16 jaar'})
            query.append({'age': 'vanaf 18 jaar'})
            query.append({'age': 'Vanaf 18 jaar'})
            query.append({'age': '3 jaar tot 99 jaar'})
            query.append({'age': 'Vanaf 6 tot 99 jaar'})
            query.append({'age': '10 maanden tot 99 jaar'})
            query.append({'age': 'vanaf 9 tot 99 jaar'})
            query.append({'age': 'Vanaf 9 maanden'})
            query.append({'age': 'Vanaf 10 maanden'})
            query.append({'age': ''})

        query2 = ''
        if geslacht == 'jongen':
            query2 = 'Jongen'
        elif geslacht == 'meisje':
            query2 = 'Meisje'
        else:
            query2 = 'Beide'

        query3 = ''
        if budget == 'minder':
            query3 = '$lte'
        else:
            query3 = '$gte'

        catalogus = db.speelgoed
        # results = catalogus.find({ '$or': query, 'gender': query2, 'price': {query3: int(bedrag)} })
        # ordered = results.sort('price')
        #
        # output = ''
        # for r in ordered:
        #     output += r['title'] + ', ' + r['brand'] + ', ' + str(r['price']) + ', ' + r['age'] + ', ' + r['gender'] + ', ' + str(r['page']) + ', <a href="' + r['img_link'] + '">' + r['img_link'] + '</a><br>'
        # return output

        data = list(catalogus.find({ '$or': query, 'gender': query2, 'price': {query3: int(bedrag)} }))
        return data

    except Exception, e:
        return 'Not found an article'

"""

done> get product
done> get products
done> get product(s) by price
done> get products under and above cut
done> get product(s) by pricerange
done> get product(s) by gender
done> get product(s) by brand
done> get product(s) by age
get product(s) by category
done> get product(s) by age+pricerange+gender
get user data
get product(s) by keywords
get populartiy
get dislike
"""
#
# if __name__ == '__main__':
#     # app.run(debug=True)
#     app.run(host='0.0.0.0', debug=True)
