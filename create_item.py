import random


def create_item(maplist, curx, cury):
    
    
    nummax = [0,0]
    map_max=max(maplist)
    for i in map_max:
        for j in range(1, 3):
            nummax[j-1]=i
    
    if curx==0 and cury==0: #curx cury가 모두 0일 때
        itemlist = []
        ranlist = [0,1]
        rannum = random.randrange(1,4)
        print(rannum)#떨어진아이템수
        
        visited = [[True, False],
                   [False, False]]
     
        tempitemlist = [[curx, cury],[curx+1, cury],
                        [curx, cury+1],[curx+1, cury+1]]
        
    
        
        for i in range(1, rannum+1):
            ranx = random.choice(ranlist)
            rany = random.choice(ranlist)
            if visited[ranx][rany]==True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlist)
                    rany = random.choice(ranlist)
            visited[ranx][rany]=True
         
          
        visited[0][0]=False
         
        print(visited)
         
        itemlist = []
        itemcount=0
         
        print(tempitemlist)
        for i in range(0,2):
            for j in range(0,2):
                itemlist.append([])
                if visited[i][j]==True:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount+=1
        itemlist.sort(reverse=True)
        
    elif curx==0 and cury==nummax[1]: #curx, cury가 우측 상단일 때
    
        itemlist = []
        ranlist = [0,1]
        rannum = random.randrange(1,4)
        print(rannum)#떨어진아이템수
        
        visited = [[True, False],
                   [False, False]]
        
        tempitemlist = [[curx, cury],[curx+1, cury],
                        [curx, cury+1],[curx+1, cury+1]]
        
    
        
        for i in range(1, rannum+1):
            ranx = random.choice(ranlist)
            rany = random.choice(ranlist)
            if visited[ranx][rany]==True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlist)
                    rany = random.choice(ranlist)
            visited[ranx][rany]=True
         
          
        visited[0][0]=False
         
        print(visited)
         
        itemlist = []
        itemcount=0
         
        print(tempitemlist)
        for i in range(0,2):
            for j in range(0,2):
                itemlist.append([])
                if visited[i][j]==True:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount+=1
        itemlist.sort(reverse=True)
        
    elif curx==nummax[0] and cury==0: #curx, cury가 왼쪽 하단일 때
        
        itemlist = []
        ranlist = [0,1]
        rannum = random.randrange(1,4)
        print(rannum)#떨어진아이템수
        
        visited = [[False, False],
                   [True, False]]
        
        tempitemlist = [[curx, cury-1],[curx+1, cury-1],
                        [curx, cury],[curx+1, cury]]
    
        
        for i in range(1, rannum+1):
            ranx = random.choice(ranlist)
            rany = random.choice(ranlist)
            if visited[ranx][rany]==True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlist)
                    rany = random.choice(ranlist)
            visited[ranx][rany]=True
         
          
        visited[0][0]=False
         
        print(visited)
        
        itemlist = []
        itemcount=0
         
        print(tempitemlist)
        for i in range(0,2):
            for j in range(0,2):
                itemlist.append([])
                if visited[i][j]==True:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount+=1
        itemlist.sort(reverse=True)
        
    elif curx==0: #curx가 0일 때
        itemlist = []
        ranlistx = [0,1,2]
        ranlisty = [0,1]
        rannum = random.randrange(1,6)
        print(rannum)#떨어진아이템수
          
          
        visited = [[False, False],
                   [True, False],
                   [False, False]]
        
        tempitemlist = [[curx, cury-1],[curx+1, cury-1],
                        [curx, cury],[curx+1, cury],
                        [curx, cury+1],[curx+1, cury+1]]
        
        
        for i in range(1, rannum+1):
            ranx = random.choice(ranlistx)
            rany = random.choice(ranlisty)
            if visited[ranx][rany]==True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlistx)
                    rany = random.choice(ranlisty)
            visited[ranx][rany]=True
         
          
        visited[1][0]=False
         
        print(visited)

        itemlist = []
        itemcount=0
         
        print(tempitemlist)
        for i in range(0,3):
            for j in range(0,2):
                itemlist.append([])
                if visited[i][j]==True:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount+=1
        itemlist.sort(reverse=True)
        
    elif cury==0: #cury가 0일 때
        itemlist = []
        ranlistx = [0,1]
        ranlisty = [0,1,2]
        rannum = random.randrange(1,6)
        print(rannum)#떨어진아이템수
          
          
        visited = [[False, True, False],
                   [False, False, False]]
        
        tempitemlist = [[curx-1, cury],[curx, cury],[curx+1, cury],
                        [curx-1, cury+1],[curx, cury+1],[curx+1, cury+1]]
        
        
        for i in range(1, rannum+1):
            ranx = random.choice(ranlistx)
            rany = random.choice(ranlisty)
            if visited[ranx][rany]==True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlistx)
                    rany = random.choice(ranlisty)
            visited[ranx][rany]=True
         
          
        visited[0][1]=False
         
        print(visited)
      
        itemlist = []
        itemcount=0
         
        print(tempitemlist)
        for i in range(0,2):
            for j in range(0,3):
                itemlist.append([])
                if visited[i][j]==True:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount+=1
        itemlist.sort(reverse=True)
        
    elif curx==nummax[0]: #curx가 mapx의 max값일 때

        itemlist = []
        ranlistx = [0,1,2]
        ranlisty = [0,1]
        rannum = random.randrange(1,6)
        print(rannum)#떨어진아이템수
          
          
        visited = [[False, False],
                   [False, True],
                   [False, False]]
        
        tempitemlist = [[curx-1, cury-1],[curx, cury-1],
                        [curx-1, cury],[curx, cury],
                        [curx-1, cury+1],[curx, cury+1]]
        
        
        for i in range(1, rannum+1):
            ranx = random.choice(ranlistx)
            rany = random.choice(ranlisty)
            if visited[ranx][rany]==True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlistx)
                    rany = random.choice(ranlisty)
            visited[ranx][rany]=True
         
          
        visited[1][0]=False
         
        print(visited)
  
        itemlist = []
        itemcount=0
         
        print(tempitemlist)
        for i in range(0,3):
            for j in range(0,2):
                itemlist.append([])
                if visited[i][j]==True:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount+=1
        itemlist.sort(reverse=True)
        
    elif cury==nummax[1]: #cury가 mapy의 max값일 때

        itemlist = []
        ranlistx = [0,1,2]
        ranlisty = [0,1]
        rannum = random.randrange(1,6)
        print(rannum)#떨어진아이템수
          
          
        visited = [[False, False, False],
                   [False, True, False]]
        
        tempitemlist = [[curx-1, cury-1],[curx, cury-1],[curx+1, cury-1],
                        [curx-1, cury],[curx, cury],[curx+1, cury]]
        
        
        for i in range(1, rannum+1):
            ranx = random.choice(ranlistx)
            rany = random.choice(ranlisty)
            if visited[ranx][rany]==True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlistx)
                    rany = random.choice(ranlisty)
            visited[ranx][rany]=True
         
          
        visited[1][0]=False
         
        print(visited)

        itemlist = []
        itemcount=0
         
        print(tempitemlist)
        for i in range(0,3):
            for j in range(0,2):
                itemlist.append([])
                if visited[i][j]==True:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount+=1
        itemlist.sort(reverse=True)
        
    else: #모두 0, max값이 아닐 때
        itemlist = []
        ranlist = [0,1,2]
        rannum = random.randrange(1,9)
        print(rannum)#떨어진아이템수
          
          
        visited = [[False, False, False],
          [False, True, False],
          [False, False, False]]
        
        tempitemlist = [[curx-1, cury-1],[curx, cury-1],[curx+1, cury-1],
                        [curx-1, cury],[curx, cury],[curx+1, cury],
                        [curx-1, cury+1],[curx, cury+1],[curx+1, cury+1]]
        
        
        for i in range(1, rannum+1):
            ranx = random.choice(ranlist)
            rany = random.choice(ranlist)
            if visited[ranx][rany]==True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlist)
                    rany = random.choice(ranlist)
            visited[ranx][rany]=True
         
          
        visited[1][1]=False
         
        print(visited)

        itemlist = []
        itemcount=0
         
        print(tempitemlist)
        for i in range(0,3):
            for j in range(0,3):
                itemlist.append([])
                if visited[i][j]==True:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount+=1
        itemlist.sort(reverse=True)
    
    
    return itemlist[:rannum]


x = 0
y = 0
print(create_item(x,y))
