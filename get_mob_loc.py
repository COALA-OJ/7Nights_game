# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

List = [[1,0,0,2],[3,3,2,1],[2,2,0,1]]

n = len(List)
m = len(List[0])

newlist = []
for i in range(n):
    for j in range(m):
        if List[i][j] == 2:
            newlist.append([i, j])

print(newlist)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
