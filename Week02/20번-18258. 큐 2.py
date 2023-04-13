import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
que = deque([])

for _ in range(N):
    X = input().strip()

    if X == 'pop':
        print(que.popleft() if que else -1)
    elif X == 'front':
        print(que[0] if que else -1)
    elif X == 'back':
        print(que[-1] if que else -1)
    elif X == 'size':
        print(len(que))
    elif X == 'empty':
        print(0 if que else 1)

    else: 
        a,b = X.split()
        que.append(b)


