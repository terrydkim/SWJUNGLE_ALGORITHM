import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

lst = list(range(1,n+1))
lst = deque(lst)

result = []
while lst:
    for i in range(k-1):
        x = lst.append(lst.popleft())
    result.append(lst.popleft())

print(f'<{", ".join(map(str,result))}>')
