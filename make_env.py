def make_env(MAP):
    col = len(MAP[0])
    row = len(MAP)
    flag = False #탈출 판정
    dy = [-1, 1, 0, 0] #상하좌우
    dx = [0, 0, -1, 1]
    break_count=0 #if break_count == result_count => 2개수 다 채움
    result_count = int((n*m)/8) # 총 count개수

    while True:
        if(break_count==result_count):
            break
        ny = random.randrange(0, col)
        nx = random.randrange(0, row)
        if MAP[ny][nx]==0:
            MAP[ny][nx]=2
            break_count+=1
                      
    for y in range(col):
        if flag: break
        for x in range(row):
            if flag: break
            if MAP[y][x]==0:
                for i in range(4):
                    ny = y+dy[i]
                    nx = x+dx[i]
                    if (ny>=0 and ny<col and nx>=0 and nx<row  and MAP[ny][nx]==0):
                        MAP[y][x]=3 #또는 Map[ny][nx] 기준점에 따라 다름( 출발 | 도착)
                        flag=True
                        break
    return MAP
