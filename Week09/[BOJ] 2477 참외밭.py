import sys
input = sys.stdin.readline

n= int(input())

lst = [list(map(int,input().split()))for i in range(6)]

width = []
length = []
for j in range(6):
    if lst[j][0] == 1 or lst[j][0] == 2:
        width.append(lst[j][1])
    elif lst[j][0] == 3 or lst[j][0] == 4:
        length.append(lst[j][1])

minus_list = []
for i in range(6):
    if lst[i][0] == lst[(i+2)%6][0]:
        minus_list.append(lst[(i+1)%6][1])

print((max(width)*max(length)-minus_list[0]*minus_list[1])*n)