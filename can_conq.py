def can_conq(map):
    col = len(map[0])
    row = len(map)
    check = [[False for c in range(col)] for r in range(row)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    block = 0
    result = False
    global cnt
    cnt = 0
    
    def dfs(y,x):
        global cnt
        cnt += 1
        check[y][x] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(nx<col and nx>=0 and ny<row and ny>=0  and check[ny][nx]==False and map[ny][nx]!=1):
                dfs(ny,nx)

    for i in range(row):
        for j in range(col):
            if map[i][j] == 1:
                block += 1

    flag = False
    for i in range(row):
        for j in range(col):
            if map[i][j] != 1 and check[i][j] == False : 
                dfs(i,j)
                flag = True
                break
        if flag == True:
            break

    if col*row-block == cnt:
        result = True
    
    return result
