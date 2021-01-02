import requests, json, sys
from settings import *

'''
GET 방식으로 보내기
'''
def initiate_game():
    res = requests.get("http://127.0.0.1:5000/spring/initiate_game%22").text
    if res=="True": return True
    else: return False

'''
POST 방식으로 보내기
'''
# headers = {'Content-Type': 'application/json'}
# data = {
#     'id': 'lee',
#     'lang_type': 'cpp',
# }
# res = requests.post('http://210.117.181.248:13577/3', headers=headers, data=json.dumps(data)).text

if __name__ == 'main':
    can_start = initiate_game()
    if can_start==False:
        sys.exit()
    # 계속 진행