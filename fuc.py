from random import randint
mob={}
user_info=[]

#맵 생성

def random_making_mob():
    # 몬스터 HP, DMG 난수 생성
    mobHP = randint(50, 200)
    mobDMG = randint(5, 20)

    # 몬스터 정보 return
    mobINFO = [mobHP, mobDMG]
    return mobINFO

def save_map_info(mob_loc, user_create_info, mob):
    for id in range(len(mob_loc)):
        mobINFO = random_making_mob()  # mobHP, mobDMG 불러오기
        mob.update({id: [mob_loc[id],mobINFO[0],mobINFO[1]]})  # mob추가 -> key : 0 ~ len-1
    return True

def getmonster_hp(mob_id):
    mob_hp=mob[mob_id][1] #mob딕셔너리에서 mob_id와 같은 id의 값을 찾았습니다. 그리고,
    return mob_hp #mob_hp는 save_mob_info에서 mob 딕셔너리에 2번째 value에 저장되어있으므로
    #[1]로 처리해서 구해주었습니다.

def getmonster_dmg(monster_id):
    #mob dictionary에서 각 id의 list value중에서 공격력에 해당하는 2번째 인덱스를 mob_DMG의 값으로 취함
    mob_DMG=mob[monster_id][2]
    #mob_DMG로 return
    return mob_DMG

#get_mosterid
def get_mosterid(x,y):
    # dict인 monster의 크기만큼 for문을 수행
    for key,value in mob.items():
        # for문을 돌다가 mob_info중 x좌표와 y좌표가 입력의 x,y와 같을 때 return
        if(value[0][0] == x and value[0][1] == y):
            return [[key, getmonster_hp(key),getmonster_dmg(key)],user_info]



#싸울때



def user_info_update(user_info, mob_info):
    mobDMG = mob_info[2]

    user_info[1] -= mobDMG  # user_info[1] = userHP

    user_info[5] += mobDMG  # user_info[5] = EXP

    if user_info[5] >= 100:
        user_info[4] += 1  # user_info[4] = Level
        user_info[5] %= 100

import random #random.randrange를 사용하기 위해 random을 import
def get_item(): #함수 정의
    money = random.randrange(1,21) #1~20 사이 난수 return
    user_info[3] = user_info[3] + money #money를 userMoney에 더한다

def reset(user_info):

    user_info[3] = 0  # userMoney 초기화
    user_info[4] = 1  # Level 초기화
    user_info[5] = 0  # Exp 초기화

    # user_info = [[x,y], userHP, userDMG, userMoney, Level, Exp]

#result_update
def result_update(f_result, user_info, mob_info):
    if(f_result == 1): #f_result 가 1인 경우
        user_info_update(user_info, mob_info)
        get_item()
        return True
    elif(f_result == 0): #f_result 가 0인 경우
        return True
    else: #f_result 가 -1인 경우 (0과1이 아닌 경우)
        reset(user_info)
        return True