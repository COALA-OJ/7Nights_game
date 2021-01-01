def getmonster_hp(mob_id):
    mob_hp=mob[mob_id][1] #mob딕셔너리에서 mob_id와 같은 id의 값을 찾았습니다. 그리고,
    return mob_hp #mob_hp는 save_mob_info에서 mob 딕셔너리에 2번째 value에 저장되어있으므로 
    #[1]로 처리해서 구해주었습니다.