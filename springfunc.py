import random
import copy
from collections import deque


def can_conq(map):
    col = len(map[0])
    row = len(map)
    check = [[False for c in range(col)] for r in range(row)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    block = 0
    result = False
    global cnt
    cnt = 0

    def dfs(y, x):
        global cnt
        cnt += 1
        check[y][x] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx < col and nx >= 0 and ny < row and ny >= 0 and check[ny][nx] == False and map[ny][nx] != 1):
                dfs(ny, nx)

    for i in range(row):
        for j in range(col):
            if map[i][j] == 1:
                block += 1

    flag = False
    for i in range(row):
        for j in range(col):
            if map[i][j] != 1 and check[i][j] == False:
                dfs(i, j)
                flag = True
                break
        if flag == True:
            break

    if col * row - block == cnt:
        result = True

    return result


def do_fight(x, y):
    v1 = x[1]/y[2]
    v2 = y[3]/x[2]

    if (v1 > v2):
        f_result = -1
    if (v1 == v2) :
        f_result = 0
    if (v1 < v2) :
        f_result = 1

    return f_result


def get_mob_loc(map):
    n = len(map)
    m = len(map[0])

    newlist = []
    for i in range(n):
        for j in range(m):
            if map[i][j] == 2:
                newlist.append([i, j])

    return (newlist)


def init_map(n, m):
    maplist = []
    for i in range(n):
        line = []
        for j in range(m):
            line.append(0)
        maplist.append(line)

    return maplist


def is_map_only_zero(mlist):
    count = 0
    all_zero = True
    for x in mlist:
        for y in x:
            if y > 0:
                count += 1
    if count > 0:
        all_zero = False
    else:
        all_zero = True
    return all_zero


def make_env(MAP):
    col = len(MAP[0])
    row = len(MAP)
    flag = False #탈출 판정
    dy = [-1, 1, 0, 0] #상하좌우
    dx = [0, 0, -1, 1]
    break_count=0 #if break_count == result_count => 2개수 다 채움
    result_count = int((col*row)/8) # 총 count개수

    while True:
        if(break_count==result_count):
            break
        ny = random.randrange(0, col)
        nx = random.randrange(0, row)
        if MAP[nx][ny]==0:
            MAP[nx][ny]=2
            break_count+=1

    while True:
        if flag: break
        y = random.randrange(0, col)
        x = random.randrange(0, row)
        if (MAP[x][y]==0):
            for i in range(4):
                ny = y+dy[i]
                nx = x+dx[i]
                if (ny>=0 and ny<col and nx>=0 and nx<row  and MAP[nx][ny]==0):
                    MAP[nx][ny]=3 #또는 Map[x][y] 기준점에 따라 다름( 출발 | 도착)
                    flag=True
                    break
    return MAP


def make_new_st_pos(a, b):
    list = []
    list.append(random.randint(0,a))
    list.append(random.randint(0,b))
    return list


def make_new_user_info():
    a = random.randint(100,251)
    b = random.randint(10,31)
    return a, b


def renew_mob_info(list):
    ans = []
    for i in range(len(list[0])):
        ans.append(list[0][i])
    return ans


def renew_user_info(MAP):
    return MAP[1]


def where_st_pos(map):
    for x in range(len(map)):
        for y in range(len(map[x])):
            if(map[x][y] == 3) :
                return [x, y]


def create_item(maplist, curx, cury):
    wallcount = 0
    nummax = [0, 0]
    map_max = max(maplist)
    nummax[0] = len(maplist)
    nummax[1] = len(map_max)
    nummax[0] -= 1
    nummax[1] -= 1
    """for i in map_max:
        for j in range(1, 3):
            nummax[j-1]=i"""

    if curx == 0 and cury == 0:  # curx cury가 모두 0일 때 right_top
        itemlist = []
        ranlist = [0, 1]

        visited = [[True, False],
                   [False, False]]

        for i in range(0, 2):
            for j in range(0, 2):
                if maplist[curx + i][cury + j] == 1:
                    visited[i][j] = True
                    wallcount -= 1
        wtemp = 4 + wallcount
        rannum = random.randrange(1, wtemp)

        tempitemlist = [[curx, cury], [curx, cury + 1],
                        [curx + 1, cury], [curx + 1, cury + 1]]

        for i in range(1, rannum + 1):
            ranx = random.choice(ranlist)
            rany = random.choice(ranlist)
            if visited[ranx][rany] == True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlist)
                    rany = random.choice(ranlist)
            visited[ranx][rany] = True

        visited[0][0] = False

        itemlist = []
        itemcount = 0

        for i in range(0, 2):
            for j in range(0, 2):
                itemlist.append([])
                if visited[i][j] == True and maplist[curx + i][cury + j] == 0:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount += 1
        itemlist.sort(reverse=True)



    elif curx == 0 and cury == nummax[1]:  # curx, cury가 우측 상단일 때 left_top

        itemlist = []
        ranlist = [0, 1]

        visited = [[False, True],
                   [False, False]]

        for i in range(0, 2):
            for j in range(-1, 1):
                if maplist[curx + i][cury + j] == 1:
                    visited[i][j + 1] = True
                    wallcount -= 1
        wtemp = 4 + wallcount
        rannum = random.randrange(1, wtemp)

        tempitemlist = [[curx, cury - 1], [curx, cury],
                        [curx + 1, cury - 1], [curx + 1, cury]]

        for i in range(1, rannum + 1):
            ranx = random.choice(ranlist)
            rany = random.choice(ranlist)
            if visited[ranx][rany] == True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlist)
                    rany = random.choice(ranlist)
            visited[ranx][rany] = True

        visited[0][1] = False

        itemlist = []
        itemcount = 0

        for i in range(0, 2):
            for j in range(-1, 1):
                itemlist.append([])
                if visited[i][j + 1] == True and maplist[curx + i][cury + j] == 0:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount += 1
        itemlist.sort(reverse=True)



    elif curx == nummax[0] and cury == 0:  # curx, cury가 왼쪽 하단일 때 right_bottom

        itemlist = []
        ranlist = [0, 1]

        visited = [[False, False],
                   [True, False]]

        for i in range(-1, 1):
            for j in range(0, 2):
                if maplist[curx + i][cury + j] == 1:
                    visited[i + 1][j] = True
                    wallcount -= 1
        wtemp = 4 + wallcount
        rannum = random.randrange(1, wtemp)

        tempitemlist = [[curx - 1, cury], [curx - 1, cury + 1],
                        [curx, cury], [curx, cury + 1]]

        for i in range(1, rannum + 1):
            ranx = random.choice(ranlist)
            rany = random.choice(ranlist)
            if visited[ranx][rany] == True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlist)
                    rany = random.choice(ranlist)
            visited[ranx][rany] = True

        visited[1][0] = False

        itemlist = []
        itemcount = 0

        for i in range(-1, 1):
            for j in range(0, 2):
                itemlist.append([])
                if visited[i + 1][j] == True and maplist[curx + i][cury + j] == 0:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount += 1
        itemlist.sort(reverse=True)



    elif curx == nummax[0] and cury == nummax[1]:  # curx, cury가 오른쪽 하단일 때 left_bottom

        itemlist = []
        ranlist = [0, 1]

        visited = [[False, False],
                   [False, True]]

        for i in range(-1, 1):
            for j in range(-1, 1):
                if maplist[curx + i][cury + j] == 1:
                    visited[i + 1][j + 1] = True
                    wallcount -= 1
        wtemp = 4 + wallcount
        rannum = random.randrange(1, wtemp)

        tempitemlist = [[curx - 1, cury - 1], [curx - 1, cury],
                        [curx, cury - 1], [curx, cury]]

        for i in range(1, rannum + 1):
            ranx = random.choice(ranlist)
            rany = random.choice(ranlist)
            if visited[ranx][rany] == True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlist)
                    rany = random.choice(ranlist)
            visited[ranx][rany] = True

        visited[1][1] = False

        itemlist = []
        itemcount = 0

        for i in range(-1, 1):
            for j in range(-1, 1):
                itemlist.append([])
                if visited[i + 1][j + 1] == True and maplist[curx + i][cury + j] == 0:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount += 1
        itemlist.sort(reverse=True)



    elif cury == 0:  # cury가 0일 때
        itemlist = []
        ranlistx = [0, 1, 2]
        ranlisty = [0, 1]

        visited = [[False, False],
                   [True, False],
                   [False, False]]

        for i in range(-1, 2):
            for j in range(0, 2):
                if maplist[curx + i][cury + j] == 1:
                    visited[i + 1][j] = True
                    wallcount -= 1
        wtemp = 6 + wallcount
        rannum = random.randrange(1, wtemp)

        tempitemlist = [[curx - 1, cury], [curx - 1, cury + 1],
                        [curx, cury], [curx, cury + 1],
                        [curx + 1, cury], [curx + 1, cury + 1]]

        for i in range(1, rannum + 1):
            ranx = random.choice(ranlistx)
            rany = random.choice(ranlisty)
            if visited[ranx][rany] == True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlistx)
                    rany = random.choice(ranlisty)
            visited[ranx][rany] = True

        visited[1][0] = False

        itemlist = []
        itemcount = 0

        for i in range(-1, 2):
            for j in range(0, 2):
                itemlist.append([])
                if visited[i + 1][j] == True and maplist[curx + i][cury + j] == 0:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount += 1
        itemlist.sort(reverse=True)

    elif curx == 0:  # curx가 0일 때
        itemlist = []
        ranlistx = [0, 1]
        ranlisty = [0, 1, 2]

        visited = [[False, True, False],
                   [False, False, False]]

        for i in range(0, 2):
            for j in range(-1, 2):
                if maplist[curx + i][cury + j] == 1:
                    visited[i][j + 1] = True
                    wallcount -= 1
        wtemp = 6 + wallcount
        rannum = random.randrange(1, wtemp)

        tempitemlist = [[curx, cury - 1], [curx, cury], [curx, cury + 1],
                        [curx + 1, cury - 1], [curx + 1, cury], [curx + 1, cury + 1]]

        for i in range(1, rannum + 1):
            ranx = random.choice(ranlistx)
            rany = random.choice(ranlisty)
            if visited[ranx][rany] == True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlistx)
                    rany = random.choice(ranlisty)
            visited[ranx][rany] = True

        visited[0][1] = False

        itemlist = []
        itemcount = 0

        for i in range(0, 2):
            for j in range(-1, 2):
                itemlist.append([])
                if visited[i][j + 1] == True and maplist[curx + i][cury + j] == 0:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount += 1
        itemlist.sort(reverse=True)

    elif cury == nummax[1]:  # cury가 mapy의 max값일 때

        itemlist = []
        ranlistx = [0, 1, 2]
        ranlisty = [0, 1]

        visited = [[False, False],
                   [False, True],
                   [False, False]]

        for i in range(-1, 2):
            for j in range(-1, 1):
                if maplist[curx + i][cury + j] == 1:
                    visited[i + 1][j + 1] = True
                    wallcount -= 1
        wtemp = 6 + wallcount
        rannum = random.randrange(1, wtemp)

        tempitemlist = [[curx - 1, cury - 1], [curx - 1, cury],
                        [curx, cury - 1], [curx, cury],
                        [curx + 1, cury - 1], [curx + 1, cury], ]

        for i in range(1, rannum + 1):
            ranx = random.choice(ranlistx)
            rany = random.choice(ranlisty)
            if visited[ranx][rany] == True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlistx)
                    rany = random.choice(ranlisty)
            visited[ranx][rany] = True

        visited[1][1
        ] = False

        itemlist = []
        itemcount = 0

        for i in range(-1, 2):
            for j in range(-1, 1):
                itemlist.append([])
                if visited[i + 1][j + 1] == True and maplist[curx + i][cury + j] == 0:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount += 1
        itemlist.sort(reverse=True)

    elif curx == nummax[0]:  # curx가 mapx의 max값일 때

        itemlist = []
        ranlistx = [0, 1]
        ranlisty = [0, 1, 2]

        visited = [[False, False, False],
                   [False, True, False]]

        for i in range(-1, 1):
            for j in range(-1, 2):
                if maplist[curx + i][cury + j] == 1:
                    visited[i + 1][j + 1] = True
                    wallcount -= 1
        wtemp = 6 + wallcount
        rannum = random.randrange(1, wtemp)

        tempitemlist = [[curx - 1, cury - 1], [curx - 1, cury], [curx - 1, cury + 1],
                        [curx, cury - 1], [curx, cury], [curx, cury + 1]]

        for i in range(1, rannum + 1):
            ranx = random.choice(ranlistx)
            rany = random.choice(ranlisty)
            if visited[ranx][rany] == True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlistx)
                    rany = random.choice(ranlisty)
            visited[ranx][rany] = True

        visited[1][1] = False

        itemlist = []
        itemcount = 0

        for i in range(-1, 1):
            for j in range(-1, 2):
                itemlist.append([])
                if visited[i + 1][j + 1] == True and maplist[curx + i][cury + j] == 0:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount += 1
        itemlist.sort(reverse=True)

    else:  # 모두 0, max값이 아닐 때
        itemlist = []
        ranlist = [0, 1, 2]
        rannum = random.randrange(1, 9)

        visited = [[False, False, False],
                   [False, True, False],
                   [False, False, False]]

        for i in range(-1, 2):
            for j in range(-1, 2):
                if maplist[curx + i][cury + j] == 1:
                    visited[i + 1][j + 1] = True
                    wallcount -= 1
        wtemp = 9 + wallcount
        rannum = random.randrange(1, wtemp)

        tempitemlist = [[curx - 1, cury - 1], [curx - 1, cury], [curx - 1, cury + 1],
                        [curx, cury - 1], [curx, cury], [curx, cury + 1],
                        [curx + 1, cury - 1], [curx + 1, cury], [curx + 1, cury + 1]]

        for i in range(1, rannum + 1):
            ranx = random.choice(ranlist)
            rany = random.choice(ranlist)
            if visited[ranx][rany] == True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlist)
                    rany = random.choice(ranlist)
            visited[ranx][rany] = True

        visited[1][1] = False

        itemlist = []
        itemcount = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                itemlist.append([])
                if visited[i + 1][j + 1] == True and maplist[curx + i][cury + j] == 0:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount += 1
    itemlist.sort(reverse=True)
    return itemlist[:rannum]


def make_wall(list):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    choice = [4,5]
    mx = len(list)
    my = len(list[0])
    # 컴포넌트 갯수 설정
    component = random.randint(10, 15)
    for i in range(component):
        print(i)
        # 1의 넓이 설정
        area = random.randint(0, 1)

        # 1이 아닌 한 지점 선택
        temp = copy.deepcopy(list)
        x=0
        y=0
        while True:
            x = random.randint(0, mx-1)
            y = random.randint(0, my-1)
            if temp[x][y] == 0:
                break

        # 그 지점을 기준으로 4x4 or 5x5 넓이만큼 1로 변경
        temp[x][y] = 1
        for j in range(choice[area]):
            for k in range(choice[area]):

                nx = x+j
                ny = y+k
                if (x < 0 or nx >= mx or ny < 0 or ny >= my):
                    continue
                temp[nx][ny]=1
                x = nx
                y = ny

        # 모든 지점을 탐색하기 위한 1이 아닌 지점 선택
        sx=0; sy=0
        check1 = True
        for searchx in range(mx):
            if check1 == False:
                break
            for searchy in range(my):
                if temp[searchx][searchy] == 0:
                    sx = searchx; sy = searchy
                    check1 = False
                    break

        # 모든 지점 탐색
        queue = deque()
        queue.append((sx,sy))
        search = copy.deepcopy(temp)
        search[sx][sy] = 1
        while queue:
            qx, qy = queue.popleft()
            for j in range(4):
                qnx = qx + dx[j]
                qny = qy + dy[j]

                # 범위 밖 and 갈 수 없는 곳
                if(qnx>=0 and qnx<mx and qny>=0 and qny<my and search[qnx][qny]==0):
                    queue.append([qnx, qny])
                    search[qnx][qny] = 1

        # 전부 탐색을 성공했는지 아닌지
        check2 = True
        for ii in range(mx):
            if check2 == False:
                break
            for jj in range(my):
                if search[ii][jj]==0:
                    check2 = False
                    break
        if check2 == True:
            list = copy.deepcopy(temp)
        else:
            i-=1
    return list