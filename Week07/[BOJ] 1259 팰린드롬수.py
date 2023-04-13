import sys
input = sys.stdin.readline

while (True):
    n = list(map(int,input().strip()))

    if n[0] == 0 :
        break
    cnt = 0
    for i in range(len(n)//2):
        if n[i] != n[-(i+1)]:
            print('no')
            cnt += 1
            break
    if cnt != 1:
        print('yes')