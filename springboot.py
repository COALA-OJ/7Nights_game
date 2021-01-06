import requests, json, sys
import springfunc as sf
from flask import Flask
from flask import request
import copy

app = Flask(__name__)

@app.route('/spring/meet_monster', methods=['POST'])
def mob_request():
    param_dict = request.get_json()
    if param_dict == None:
        return "no param"
    curx = param_dict['user_pos_x']
    cury = param_dict['user_pos_y']
    res = get_fight(curx, cury)
    data = {}
    data["item_loc"] = res
    print(data)
    return json.dumps(data)

def send_map_info(mob_info, user_create_info, maplist):
    data = {}
    data1 = {}
    data['mob_info'] = mob_info
    data['user_create_info'] = user_create_info
    data['map'] = maplist
    data1['mob_info'] = mob_info
    HP, DMG = sf.make_new_user_info()
    user_info = []
    user_info.append(user_create_info)
    user_info.append(HP)
    user_info.append(DMG)
    user_info.append(0)
    user_info.append(1)
    user_info.append(0)
    data1['user_create_info'] = user_info
    header = {'Content-Type': 'application/json'}
    # print(data1)
    # resf = requests.post("http://210.117.181.103:9998/flask/send_map_info", headers=header, data=json.dumps(data1))
    return json.dumps(data)


@app.route('/spring/initiate_game')
def create_map():
    while True:
        map = sf.init_map(100, 100) # 전부 0으로 1000 x 1000 2차원 list 생성
        if sf.is_map_only_zero(map) :
            break
    map = sf.make_wall(map)
    map = sf.make_env(map)
    global maplist
    maplist = copy.deepcopy(map)
    st_pos = sf.where_st_pos(map)
    mob_info = sf.get_mob_loc(map)
    user_create_info = st_pos
    res = send_map_info(mob_info, user_create_info, map)
    return res

def get_fight(curx, cury):
    header = {'Content-Type': 'application/json'}
    # fight_data = requests.post("http://210.117.181.103:5000/flask/get_monsterid", headers=header, data=json.dumps([locx, locy]))
    # mob_info = sf.renew_mob_info(fight_data)
    mob_info = [1, 100, 10]
    # user_info = sf.renew_user_info(fight_data)
    user_info = [[curx, cury], 200, 10, 0, 1, 0]
    f_result = sf.do_fight(mob_info, user_info)
    data = {}
    data['f_result'] = f_result
    data['user_info'] = user_info
    data['mob_info'] = mob_info
    # res = requests.get("http://210.117.181.103:5000/flask/res_fight", headers=header, data=json.dumps(data)).text
    item_loc = sf.create_item(maplist, curx, cury)
    # if f_result == 1:
    #    sf.create_item(curx, cury)
    return item_loc




app.run(host='0.0.0.0', port=5000, debug=True)
