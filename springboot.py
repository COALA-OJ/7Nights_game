import requests, json, sys
import springfunc as sf
from flask import Flask
from flask import request

app = Flask(__name__)

#@app.route('/spring/meet_monster')
def mob_request():
    param_dict = request.args.to_dict()
    if len(param_dict) == 0:
        return "no param"
    curx = request.args['user_pos_x']
    cury = request.args['user_pos_y']
    # res = get_fight(curx, cury)
    # return res


def send_map_info(mob_info, user_create_info, maplist):
    data = {}
    data1 = {}
    data['mob_info'] = mob_info
    data['user_create_info'] = user_create_info
    data['map'] = maplist
    # res = requests.get("http://127.0.0.1:5000/spring/initiate_game", data=json.dumps(data)).text
    data1['mob_info'] = mob_info
    HP, DMG = sf.make_new_user_info()
    user_info = []
    user_info.append(user_create_info)
    user_info.append(HP)
    user_info.append(DMG)
    user_info.append(0)
    user_info.append(1)
    user_info.append(0)
    data1['user_create_info'] = user_create_info
    header = {'Content-Type':'application/json'}
    while True:
        resf = requests.post("http://210.117.181.103:6000/flask/send_map_info", headers=header, data=json.dumps(data1)).text
        if resf == "True" : break
        break
    return json.dumps(data)
    # if res == "True" : return True
    # else : return False


@app.route('/spring/initiate_game')
def create_map():
    while True:
        map = sf.init_map(100, 100) # 전부 0으로 1000 x 1000 2차원 list 생성
        if sf.is_map_only_zero(map) :
            break
    map = sf.make_wall(map) # 개당 크기가 10 ~ 30인 컴포넌트를 10 ~ 15개 생성
    map = sf.make_env(map)
    st_pos = sf.where_st_pos(map)
    mob_info = sf.get_mob_loc(map)
    user_create_info = st_pos
    res = send_map_info(mob_info, user_create_info, map)
    return res

# def get_fight(curx, cury):
#     fight_data = requests.get("http://210.117.181.103:5000/flask/get_monsterid", data=[locx, locy]).text
#     mob_info = sf.renew_mob_info(fight_data)
#     user_info = sf.renew_user_info(fight_data)
#     f_result = sf.do_fight(mob_info, user_info)
#     data = {}
#     data['f_result'] = f_result
#     data['user_info'] = user_info
#     data['mob_info'] = user_info
#     res = requests.get("http://210.117.181.103:5000/flask/res_fight", data=data).text
#
#     if f_result == 1:
#        sf.create_item(curx, cury)
#
#     return res
#



app.run(host='0.0.0.0', port=5000, debug=True)
