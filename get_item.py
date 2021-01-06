import random #random.randrange를 사용하기 위해 random을 import
def get_item(): #함수 정의
    money = random.randrange(1,21) #1~20 사이 난수 return
    user_info[3] = user_info[3] + money #money를 userMoney에 더한다