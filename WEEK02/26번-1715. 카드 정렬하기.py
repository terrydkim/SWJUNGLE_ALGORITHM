import sys, heapq
input = sys.stdin.readline

N = int(input())

lst = []
for _ in range(N):
    x = int(input().strip())
    heapq.heappush(lst, x)

result = 0
while len(lst) > 1: 
    tmp = heapq.heappop(lst) +heapq.heappop(lst)

    result += tmp

    heapq.heappush(lst, tmp)

  
print(result)