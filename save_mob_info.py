def save_mob_info(mob_loc):

    for id in range(len(mob_loc)):
        mobINFO = random_making_mob()  # mobHP, mobDMG 불러오기
        mob.update({id: [mob_loc[id],mobINFO[0],mobINFO[1]]})  # mob추가 -> key : 0 ~ len-1

    return
