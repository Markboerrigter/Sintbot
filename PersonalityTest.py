mport json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV2


personality_insights = PersonalityInsightsV2(
    username='d056f981-77b1-4081-9a41-c151e9d473da',
    password='OvRAc4rDoAMG')

# with open(join(dirname(__file__),'Trump.txt'))as personality_text:
#     print(personality_text.read()[480:485])
#     print(json.dumps(personality_insights.profile(
#         text=personality_text.read()), indent=2))

def getPersonality(personality_text,name,source):
    personality_insights_json = {"contentItems": [
        {"id": "245160944223793152", "userid": name, "sourceid": source, "created": 1427720427,
         "updated": 1427720427, "contenttype": "text/plain", "charset": "UTF-8", "language": "en",
         "content": personality_text, "parentid": "", "reply": "false", "forward": "false"}]}
    return(personality_insights.profile(text=personality_insights_json))

# with open(join(dirname(__file__), '../resources/personality.es.txt') as personality_text:
#     print(json.dumps(personality_insights.profile(text=personality_text.read(), language='es'), indent=2))

