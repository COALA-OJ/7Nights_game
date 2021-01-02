
def get_mob_loc(map):
    n = len(map)
    m = len(map[0])

    newlist = []
    for i in range(n):
        for j in range(m):
            if map[i][j] == 2:
                newlist.append([i, j])

    return (newlist)


