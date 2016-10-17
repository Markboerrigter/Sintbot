def allValues(dictionary):
    ans = []
    for k,v in dictionary.items():
        if isinstance(v,dict):
            ans.extend(allValues(v))
        else:
            ans.append(v)
    return ans

Tokens = {}
Tokens['Start'] = {}
Tokens['Start']['New'] = {}
Tokens['Start']['New']['Introduce'] = 'D7JHYWLOPGPFHJRCHPWC7DBCBEK2G7RZ'
Tokens['Start']['New']['Sinterklaas'] = 'TT4U2XJYSY6EZBUKIBGAJPHDNWDZVGVL'
Tokens['Start']['New']['Story'] = 'JW4QZSHW2GXLJKZEGPH6ZFOOP6PBYTKL'
Tokens['Start']['New']['Open'] = 'POPSPV3EUB7L3W56K4FOU7ZIMFMFKDRP'
Tokens['Start']['New']['loose'] = '6YY3HTLYKJG4HJOMEDPQ4BTUBA262SCY'
Tokens['Start']['longText'] = 'YZDGTRUDQU7H2BPRCWFIEVU4KSL42IK4'
Tokens['Start']['Old'] = {}
Tokens['Start']['Old']['recognized'] = 'IZ5AIDU7KEVIXG6RAWEOY4W6664XGX3R'
Tokens['Start']['Old']['oldFashioned'] = 'Z4NCJN2J2CJGNBVW64WQULIWCUD54HMB'
Tokens['Start']['Old']['longText'] = 'YZDGTRUDQU7H2BPRCWFIEVU4KSL42IK4'
Tokens['Start']['Old']['sintQuestioning'] = 'DNYI3O6EHFJ376YACLJSDCB3U7H7MXDB'
Tokens['decisions'] = {}
Tokens['decisions']['age'] = {}
Tokens['decisions']['gender'] = {}
Tokens['decisions']['budget'] = {}
Tokens['decisions']['age']['findage1'] = 'BQDMM2HIB7YSAXICR7QFULGKXQWJHKXJ'
Tokens['decisions']['age']['findage2'] = '5UTS7JO3NPTOHD52HAWKQOZBUNTFC53R'
Tokens['decisions']['gender']['findgender1'] = 'BBEESH7AOGULQK6L3TPYYRC4L4Y36LHH'
Tokens['decisions']['gender']['findgender2'] = 'UQVGOAZSC54YYVUGHURXHY5I4U6A2X3M'
Tokens['decisions']['budget']['findbudget1'] = 'IJ7PMHQPAVNK6UU3C3BE3NOVXZ6MMPOJ'
Tokens['decisions']['budget']['findbudget2'] = 'TB4QZIZYN4AZQPHYMWDCNFVOR3MJRUGI'
Tokens['presentchoosing'] = {}
Tokens['presentchoosing']['present'] = {}
Tokens['presentchoosing']['present']['normal'] = '5YVSD6XFV4I3Q457C56YRYLED5Q6E6ZK'
Tokens['presentchoosing']['present']['discount'] = 'RNZHGD6QHWG6JOZF66W52XHU364H4B6Y'
Tokens['presentchoosing']['present']['loyal'] = 'COHIUFQKSQMSGK6SNFLDR6D74CWZIJLZ'
Tokens['presentchoosing']['notFound'] = {}
Tokens['presentchoosing']['notFound']['stop1'] = 'B6ZPCLQVJDDKKRNXQFF2HFWF2LZJ27KT'
Tokens['presentchoosing']['notFound']['stop2'] = 'I376WUKZF6BKKUP2I3LQ4CTGF5UBYAOM'
Tokens['presentchoosing']['notFound']['popular'] = 'BQ44V4L72VQKETN5DRE7NKPMDPVJ276C'
Tokens['presentchoosing']['notFound']['keyword1'] = 'YPRANRJYCS4VPLXM3RZBOZA7V4R73TDY'
Tokens['presentchoosing']['notFound']['keyword2'] = '5CJ4C7UWBRIVLERLIU5XEMUN3WDUUM3H'
Tokens['feedback'] = {}
Tokens['feedback']['feedback1'] = 'Z7V53U4LAVY3JWEU6B32ZYBXK4SK6OEJ'
Tokens['feedback']['feedback2'] = '6ZUZHBITRTWR3PEJE26DZE6ZX3HHGGES'


print(len(allValues(Tokens)))
