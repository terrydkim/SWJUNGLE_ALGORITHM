import sys,heapq

input = sys.stdin.readline

N = int(input())

lst=[]

for _ in range(N):
    X = int(input().strip())
    if not X == 0:
        heapq.heappush(lst, -X)
    else : 
        print(-heapq.heappop(lst) if lst else 0)
    