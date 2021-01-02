def where_st_pos(map):
    for x in range(len(map)):
        for y in range(len(map[x])):
            if(map[x][y] == 3) :
                return [x, y]