#From_Baek

import requests
import json
#from Data import Data
from collections import OrderedDict, defaultdict


def getCode_info():
# 2. json타입을 dict으로 변경하는 방법
# => json.loads() - json input
    html = json.loads(requests.get("http://211.33.49.253:5000/spring/initiate_game").text)
    # print(html[0]["lang_type"])
    html = dict(html)
    # liste = [html[0]["code"] ,html[0]["lang_type"],html[0]["id"]]
    # m = Data()
    # for i in html:
    #     m = Data(
    #         i[0]['ID'], 
    #         i['Language_type'],
    #         i['Code'], 
    #     )
    #     list.append(m)
    #print(list)        
    return html["user_create_info"], html["mob_info"]

def getans_info(a):
# 2. json타입을 dict으로 변경하는 방법
# => json.loads() - json input
    #html = json.loads(requests.get("http://210.117.181.106:12331/tolim").text)
    print(a)
    list = [a[0]["code"] ,a[0]["id"]]
    # m = Data()
    # for i in html:
    #     m = Data(
    #         i[0]['ID'], 
    #         i['Language_type'],
    #         i['Code'], 
    #     )
    #     list.append(m)
    print(list)        
    return list

# if __name__=='__main__':
#     print(requests.post("http://210.117.181.106:12331/ip").text)
#     print(getCode_info())