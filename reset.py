def reset(user_info):

    user_info[3] = 0  # userMoney 초기화
    user_info[4] = 1  # Level 초기화
    user_info[5] = 0  # Exp 초기화

    # user_info = [[x,y], userHP, userDMG, userMoney, Level, Exp]