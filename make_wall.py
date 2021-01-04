from collections import deque
import random

def make_wall(list):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    mx = len(list[0])
    my = len(list)
    # 컴포넌트 갯수 설정
    component = random.randint(10, 15)
    for i in range(component):
        # 1의 넓이 설정
        area = random.randint(10, 30)

        # 1이 아닌 한 지점 선택
        temp = list
        x, y
        while True:
            x = random.randint(0,mx)
            y = random.randint(0,my)
            if temp[x][y] == 0:
                break

        # 그 지점을 기준으로 설정한 넓이만큼 1로 변경
        temp[x][y] = 1
        for j in range(area):
            go = random.randint(0,3)
            nx = x+dx[go]
            ny = y+dy[go]
            if (temp[nx][ny]==1 or nx<0 or nx>=mx or ny<0 or ny>=my):
                j-=1
                continue
            temp[nx][ny]=1
            x = nx
            y = ny

        # 모든 지점을 탐색하기 위한 1이 아닌 지점 선택
        sx, sy
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
        search = temp
        search[sx][sy] = 1
        while queue:
            qx, qy = queue.popleft()
            for j in range(4):
                qnx = qx + dx[j]
                qny = qy + dy[j]

                # 범위 밖 and 갈 수 없는 곳
                if(search[qnx][qny] == 1 or qnx<0 or qnx>=mx or qny<0 or qny>=my) : continue

                queue.append(qnx, qny)
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
            list = temp
        else:
            i-=1

    return list
