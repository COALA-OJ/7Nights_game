# getmonster_dmg 함수 정의
def getmonster_dmg(monster_id):
    #mob dictionary에서 각 id의 list value중에서 공격력에 해당하는 2번째 인덱스를 mob_DMG의 값으로 취함
    mob_DMG=mob[monster_id][2]
    #mob_DMG로 return
    return mob_DMG