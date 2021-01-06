from collections import deque
import random
import copy

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
        check1 = True;
        for searchx in range(mx):
            if check1 == False:
                break;
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