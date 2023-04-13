import sys
input = sys.stdin.readline
from collections import deque

lst = deque([])
N = int(input())
for i in range(1,N+1):
    lst.append(i)

while len(lst) > 1:
    x = lst.popleft()
    b = lst.popleft()
    lst.append(b) 
print(lst[0])


