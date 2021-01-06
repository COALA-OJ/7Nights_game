from random import randint

def random_making_mob():

    # 몬스터 HP, DMG 난수 생성
    mobHP = randint(50, 200)
    mobDMG = randint(5, 20)

    # 몬스터 정보 return
    mobINFO = [mobHP, mobDMG]
    return mobINFO
