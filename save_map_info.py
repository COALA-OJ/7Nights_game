def save_map_info(mob_loc, user_create_info):

    for id in range(len(mob_loc)):
        mobINFO = random_making_mob()  # mobHP, mobDMG 불러오기
        mob.update({id: [mob_loc[id],mobINFO[0],mobINFO[1]]})  # mob추가 -> key : 0 ~ len-1

    user_info = user_create_info

    return True
