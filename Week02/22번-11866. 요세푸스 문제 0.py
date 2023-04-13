import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())

lst = deque([])
result = []

for i in range(1,N+1):
    lst.append(i)
        
while lst :
    for k in range(K-1):
        lst.append(lst.popleft())
    result.append(lst.popleft())

print("<", end='')
print(", ".join(map(str,result)), end='')
print(">")
