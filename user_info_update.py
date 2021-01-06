def user_info_update(user_info, mob_info):
    mobDMG = mob_info[2]

    user_info[1] -= mobDMG #user_info[1] = userHP

    user_info[5] += mobDMG #user_info[5] = EXP

    if user_info[5] >= 100:
        user_info[4] += 1 #user_info[4] = Level
        user_info[5] %= 100
