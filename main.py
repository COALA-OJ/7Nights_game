import requests, json, sys
import requests
import json
from react import *
import time
#global usermap
def initiate_game():
    res = json.loads(requests.get("http://211.33.49.253:5000/spring/initiate_game").text)
    #print(res['user_create_info'])
    """
    초기 맵 상태, 초기 유저 위치 확인인
    # """
    with open('map_file3', 'w', encoding='utf-8') as file:
        for i in res['map']:
            file.write(" ".join([str(_) for _ in i]))
            file.write('\n')

    with open('user_pos', 'w', encoding='utf-8') as file:
        for i in res['user_create_info']:
            file.write(str(i)+"\n")
    # usermap = ''
    # for i in res['map']:
    #     usermap+=" ".join([str(_) for _ in i])
    #     usermap+='\n'

# @app.route('/react/meet_monster')
def send_event(event, pos_x,pos_y):
    data = {'w_event':'','user_pos_x':'', 'user_pos_y' : ''}
    data['w_event'] = event
    data['user_pos_x'] =  pos_x
    data['user_pos_y'] =  pos_y
    start = time.time()
    res = requests.get('http://211.33.49.253:5000/spring/meet_monster', params=data, timeout=5)
    end = time.time()
    print(f"time : {end-start}")
    return res

if __name__=='__main__':
    initiate_game()
    g = UserState()
    while g.start:
        g.new()
