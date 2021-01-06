import random


def create_item(maplist, curx, cury):
    
    wallcount=0
    nummax = [0,0]
    map_max=max(maplist)
    nummax[0]=len(maplist)
    nummax[1]=len(map_max)
    nummax[0]-=1
    nummax[1]-=1
    """for i in map_max:
        for j in range(1, 3):
            nummax[j-1]=i"""
    
    if curx==0 and cury==0: #curx cury가 모두 0일 때 right_top
        itemlist = []
        ranlist = [0,1]
        
        visited = [[True, False],
                   [False, False]]
     
        for i in range(0,2):
            for j in range(0,2):
                if maplist[curx+i][cury+j]==1:
                    visited[i][j] = True
                    wallcount-=1
        wtemp = 4+wallcount
        rannum = random.randrange(1,wtemp)
                    
        tempitemlist = [[curx, cury],[curx, cury+1],
                    [curx+1, cury],[curx+1, cury+1]]
        
    
        
        for i in range(1, rannum+1):
            ranx = random.choice(ranlist)
            rany = random.choice(ranlist)
            if visited[ranx][rany]==True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlist)
                    rany = random.choice(ranlist)
            visited[ranx][rany]=True
         
          
        visited[0][0]=False
         
        itemlist = []
        itemcount=0
         
        for i in range(0,2):
            for j in range(0,2):
                itemlist.append([])
                if visited[i][j]==True and maplist[curx+i][cury+j]==0:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount+=1
        itemlist.sort(reverse=True)
        
       
        
    elif curx==0 and cury==nummax[1]: #curx, cury가 우측 상단일 때 left_top
    
        itemlist = []
        ranlist = [0,1]
        
        
        visited = [[False, True],
                   [False, False]]
        
        for i in range(0,2):
            for j in range(-1,1):
                if maplist[curx+i][cury+j]==1:
                    visited[i][j+1] = True
                    wallcount-=1
        wtemp = 4+wallcount
        rannum = random.randrange(1,wtemp)
        
        
        tempitemlist = [[curx, cury-1],[curx, cury],
                    [curx+1, cury-1],[curx+1, cury]]
        
    
        
        for i in range(1, rannum+1):
            ranx = random.choice(ranlist)
            rany = random.choice(ranlist)
            if visited[ranx][rany]==True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlist)
                    rany = random.choice(ranlist)
            visited[ranx][rany]=True
         
          
        visited[0][1]=False
         

         
        itemlist = []
        itemcount=0
         
        for i in range(0,2):
            for j in range(-1,1):
                itemlist.append([])
                if visited[i][j+1]==True and maplist[curx+i][cury+j]==0:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount+=1
        itemlist.sort(reverse=True)
        
   
        
    elif curx==nummax[0] and cury==0: #curx, cury가 왼쪽 하단일 때 right_bottom
        
        itemlist = []
        ranlist = [0,1]
        
        
        visited = [[False, False],
                   [True, False]]
        
        for i in range(-1,1):
            for j in range(0,2):
                if maplist[curx+i][cury+j]==1:
                    visited[i+1][j] = True
                    wallcount-=1
        wtemp = 4+wallcount
        rannum = random.randrange(1,wtemp)
                    
        tempitemlist = [[curx-1, cury],[curx-1, cury+1],
                        [curx, cury],[curx, cury+1]]
    
        
        for i in range(1, rannum+1):
            ranx = random.choice(ranlist)
            rany = random.choice(ranlist)
            if visited[ranx][rany]==True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlist)
                    rany = random.choice(ranlist)
            visited[ranx][rany]=True
         
          
        visited[1][0]=False
         
        
        itemlist = []
        itemcount=0
         
        for i in range(-1,1):
            for j in range(0,2):
                itemlist.append([])
                if visited[i+1][j]==True and maplist[curx+i][cury+j]==0:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount+=1
        itemlist.sort(reverse=True)
        
    
        
    elif curx==nummax[0] and cury==nummax[1]: #curx, cury가 오른쪽 하단일 때 left_bottom
    
        itemlist = []
        ranlist = [0,1]
        
        
        visited = [[False, False],
                   [False, True]]
        
        for i in range(-1,1):
            for j in range(-1,1):
                if maplist[curx+i][cury+j]==1:
                    visited[i+1][j+1] = True
                    wallcount-=1
        wtemp = 4+wallcount
        rannum = random.randrange(1,wtemp)  
        
        
        tempitemlist = [[curx-1, cury-1],[curx-1, cury],
                        [curx, cury-1],[curx, cury]]
        
    
        
        for i in range(1, rannum+1):
            ranx = random.choice(ranlist)
            rany = random.choice(ranlist)
            if visited[ranx][rany]==True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlist)
                    rany = random.choice(ranlist)
            visited[ranx][rany]=True
         
          
        visited[1][1]=False
         
        
         
       
        itemlist = []
        itemcount=0
         
        
        for i in range(-1,1):
            for j in range(-1,1):
                itemlist.append([])
                if visited[i+1][j+1]==True and maplist[curx+i][cury+j]==0:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount+=1
        itemlist.sort(reverse=True)
        
    
        
    elif cury==0: #cury가 0일 때
        itemlist = []
        ranlistx = [0,1,2]
        ranlisty = [0,1]
       
          
          
        visited = [[False, False],
                   [True, False],
                   [False, False]]
        
        
        for i in range(-1,2):
            for j in range(0,2):
                if maplist[curx+i][cury+j]==1:
                    visited[i+1][j] = True
                    wallcount-=1
        wtemp = 6+wallcount
        rannum = random.randrange(1,wtemp)
            
        tempitemlist = [[curx-1, cury],[curx-1, cury+1],
                        [curx, cury],[curx, cury+1],
                        [curx+1, cury],[curx+1, cury+1]]
        
        
        for i in range(1, rannum+1):
            ranx = random.choice(ranlistx)
            rany = random.choice(ranlisty)
            if visited[ranx][rany]==True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlistx)
                    rany = random.choice(ranlisty)
            visited[ranx][rany]=True
         
          
        visited[1][0]=False
         

        itemlist = []
        itemcount=0
         
        for i in range(-1,2):
            for j in range(0,2):
                itemlist.append([])
                if visited[i+1][j]==True and maplist[curx+i][cury+j]==0:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount+=1
        itemlist.sort(reverse=True)
        
    elif curx==0: #curx가 0일 때
        itemlist = []
        ranlistx = [0,1]
        ranlisty = [0,1,2]
        
          
          
        visited = [[False, True, False],
                   [False, False, False]]
        
        for i in range(0,2):
            for j in range(-1,2):
                if maplist[curx+i][cury+j]==1:
                    visited[i][j+1] = True
                    wallcount-=1
        wtemp = 6+wallcount
        rannum = random.randrange(1,wtemp)
        
        
        tempitemlist = [[curx, cury-1],[curx, cury],[curx, cury+1],
                        [curx+1, cury-1],[curx+1, cury],[curx+1, cury+1]]
        
        
        for i in range(1, rannum+1):
            ranx = random.choice(ranlistx)
            rany = random.choice(ranlisty)
            if visited[ranx][rany]==True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlistx)
                    rany = random.choice(ranlisty)
            visited[ranx][rany]=True
         
          
        visited[0][1]=False
         
      
        itemlist = []
        itemcount=0
         
        for i in range(0,2):
            for j in range(-1,2):
                itemlist.append([])
                if visited[i][j+1]==True and maplist[curx+i][cury+j]==0:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount+=1
        itemlist.sort(reverse=True)
        
    elif cury==nummax[1]: #cury가 mapy의 max값일 때

        itemlist = []
        ranlistx = [0,1,2]
        ranlisty = [0,1]
        
          
          
        visited = [[False, False],
                   [False, True],
                   [False, False]]
        
        for i in range(-1,2):
            for j in range(-1,1):
                if maplist[curx+i][cury+j]==1:
                    visited[i+1][j+1] = True
                    wallcount-=1
        wtemp = 6+wallcount
        rannum = random.randrange(1,wtemp)
        
        tempitemlist = [[curx-1, cury-1],[curx-1, cury],
                        [curx, cury-1],[curx, cury],
                        [curx+1, cury-1],[curx+1, cury],]
        
        
        for i in range(1, rannum+1):
            ranx = random.choice(ranlistx)
            rany = random.choice(ranlisty)
            if visited[ranx][rany]==True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlistx)
                    rany = random.choice(ranlisty)
            visited[ranx][rany]=True
         
          
        visited[1][1
                   ]=False
         
  
        itemlist = []
        itemcount=0
         
        for i in range(-1,2):
            for j in range(-1,1):
                itemlist.append([])
                if visited[i+1][j+1]==True and maplist[curx+i][cury+j]==0:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount+=1
        itemlist.sort(reverse=True)
        
    elif curx==nummax[0]: #curx가 mapx의 max값일 때

        itemlist = []
        ranlistx = [0,1]
        ranlisty = [0,1,2]
        
          
          
        visited = [[False, False, False],
                   [False, True, False]]
        
        for i in range(-1,1):
            for j in range(-1,2):
                if maplist[curx+i][cury+j]==1:
                    visited[i+1][j+1] = True
                    wallcount-=1
        wtemp = 6+wallcount
        rannum = random.randrange(1,wtemp)
        
        tempitemlist = [[curx-1, cury-1],[curx-1, cury],[curx-1, cury+1],
                        [curx, cury-1],[curx, cury],[curx, cury+1]]
        
        for i in range(1, rannum+1):
            ranx = random.choice(ranlistx)
            rany = random.choice(ranlisty)
            if visited[ranx][rany]==True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlistx)
                    rany = random.choice(ranlisty)
            visited[ranx][rany]=True
         
          
        visited[1][1]=False
         

        itemlist = []
        itemcount=0
         
        for i in range(-1,1):
            for j in range(-1,2):
                itemlist.append([])
                if visited[i+1][j+1]==True and maplist[curx+i][cury+j]==0:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount+=1
        itemlist.sort(reverse=True)
        
    else: #모두 0, max값이 아닐 때
        itemlist = []
        ranlist = [0,1,2]
        rannum = random.randrange(1,9)
          
          
        visited = [[False, False, False],
                   [False, True, False],
                   [False, False, False]]
        
        for i in range(-1,2):
            for j in range(-1,2):
                if maplist[curx+i][cury+j]==1:
                    visited[i+1][j+1] = True
                    wallcount-=1
        wtemp = 9+wallcount
        rannum = random.randrange(1,wtemp)
        
        
        tempitemlist = [[curx-1, cury-1],[curx-1, cury],[curx-1, cury+1],
                    [curx, cury-1],[curx, cury],[curx, cury+1],
                    [curx+1, cury-1],[curx+1, cury],[curx+1, cury+1]]
        
        
        for i in range(1, rannum+1):
            ranx = random.choice(ranlist)
            rany = random.choice(ranlist)
            if visited[ranx][rany]==True:
                while visited[ranx][rany]:
                    ranx = random.choice(ranlist)
                    rany = random.choice(ranlist)
            visited[ranx][rany]=True
         
          
        visited[1][1]=False
         

        itemlist = []
        itemcount=0
         
        for i in range(-1,2):
            for j in range(-1,2):
                itemlist.append([])
                if visited[i+1][j+1]==True and maplist[curx+i][cury+j]==0:
                    itemlist[itemcount].append(tempitemlist[itemcount][0])
                    itemlist[itemcount].append(tempitemlist[itemcount][1])
                itemcount+=1
    itemlist.sort(reverse=True)
    
    
    
    return itemlist[:rannum]

