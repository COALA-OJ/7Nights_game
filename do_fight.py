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