import sys

Map = list() #맵
flag = False #탈출 판정
dy = [-1, 1, 0, 0] #상하좌우
dx = [0, 0, -1, 1]
break_count=0 #if break_count == result_count => 2개수 다 채움
reuslt_count=0 # (n*m)/8 => 2 최대 개수

n, m = map(int, sys.stdin.readline().split())
result_count = int((n*m)/8) # 총 count개수

for _ in range(n):
    Map.append(list(map(int, sys.stdin.readline().split())))   

for y in range(n):
    if flag: break
    for x in range(m):
        if flag: break
        if Map[y][x]==0:
            for i in range(4):
                ny = y+dy[i]
                nx = x+dx[i]
                if (ny>=0 and ny<n and nx>=0 and nx<m  and Map[ny][nx]==0):
                    Map[y][x]=3 #또는 Map[ny][nx] 기준점에 따라 다름( 출발 | 도착)
                    flag=True
                    break

flag=False
for y in range(n):
    if flag: break
    for x in range(m):
        if Map[y][x]==0:
            Map[y][x]=2
            break_count+=1
            if (break_count>=result_count): #총 count개수 채우면 탈출
                flag=True
                break

for row in Map:
    print(row)
