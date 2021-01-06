#get_mosterid
def get_mosterid(x,y):
    # dict인 monster의 크기만큼 for문을 수행
    for key,value in monster.items():
        # for문을 돌다가 mob_info중 x좌표와 y좌표가 입력의 x,y와 같을 때 return
        if(value[0][0] == x and value[0][1] == y):
            return [[key, getmonster_hp(key),getmonster_dmg(key)],user_info]
