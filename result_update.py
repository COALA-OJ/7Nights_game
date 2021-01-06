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
