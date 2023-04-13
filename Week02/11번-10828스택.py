import sys
input = sys.stdin.readline

N = int(input())

lst = []
for i in range(N):
    b = input().split()
    if b[0] == 'push':
        lst.append(b[1])
    elif b[0] == 'pop':
        try:
            x = lst.pop()
            print(x)
        except:
            print(-1)
    elif b[0] == 'size':
        print(len(lst))
    elif b[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else : print(0)
    else : 
        try:
            print(lst[-1])
        except:
            print(-1)

            
# 참고하기 빈 리스트를 체크하는 법
# import sys
# N=int(input())
# stk=[]
# for _ in range(N):
#     cmd=sys.stdin.readline().split()
#     if cmd[0] == 'push': stk.append(int(cmd[1]))
#     elif cmd[0] == 'pop': print(stk.pop() if stk else -1)
#     elif cmd[0] == 'size': print(len(stk))
#     elif cmd[0] == 'empty': print(1 if not stk else 0)
#     elif cmd[0] == 'top': print(stk[-1] if stk else -1)

