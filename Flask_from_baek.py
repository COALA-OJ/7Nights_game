#Flask_from_baek

from fuc import random_making_mob, save_map_info,  get_mosterid, get_item, getmonster_dmg, getmonster_hp, user_info_update, result_update, reset
from flask import render_template
import requests
from flask import jsonify
from flask import Flask
from From_Baek import *
import json
from flask import request
mob={}
user_info = []

 
app = Flask (__name__)
 
@app.route('/mob_info')
def index():
    w, k = getCode_info()
    save_map_info(k, w, mob)
    user_info = w
    print(mob, user_info)
    return "546"
    
@app.route('/flask/send_map_info', methods=['POST'])
def mob_request():
    param_dict = request.get_json()
    if param_dict == None:
        return "no param"
    mob = param_dict['mob_info']
    user_info = param_dict['user_create_info']
    print(mob, user_info)
    return 'True'
    #res = get_fight(curx, cury)
    #return res


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=6000)

# from flask import jsonify
# #/movie/<page>로 들어오면 movie.html 리턴해주고 list에 정보가 담겨 넘어감
# @app.route('/1')
# def movie():
#     res = requests.post("http://210.117.181.248:13579/3").text
#     return res

# @app.route('/4')
# def tokim():
#     return jsonify(getCode_info())
# 0.0.0.0은 누구나 들어 올 수 있고
# port는 9000번
# 디버그 모드 작용
## 중요한 점은 절대 여기서 실행하지 말고 cmd에서 실행 할 것!!
# if __name__=="__main__":
#     app.run(host='0.0.0.0', port=9000, debug=True)
