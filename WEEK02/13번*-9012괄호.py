import sys
input = sys.stdin.readline

N = int(input())


for _ in range(N):
    b = input().strip()
    lst = []

    c = True
    for i in b:
        if i == '(':
            lst.append(i)
        elif i == ')':
            if lst:
                lst.pop()
            else: 
                c = False
                break
    if not c or len(lst)!= 0:
        print('NO')
    else: print('YES')
    
    



