def init_map(n, m):
     
    maplist = []
    for i in range(n):
        line = []
        for j in range(m):
            line.append(0)
        maplist.append(line)
            
    return maplist
