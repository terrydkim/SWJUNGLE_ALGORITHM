import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

for i in range(m):
    a ,b = map(int,input().split())

    if a == b :
        print('1')
        continue
    if not n//2 +1 >= abs(b-a):
        print('0')
        continue
    if b > a:
        if b-a <= n-b+1:
            print('1')
            continue
    if a > b :
        if a-b <= n-a+2:
            print('1')
            continue
    print('0')