import sys
from itertools import combinations
input = sys.stdin.readline

n , m = map(int,input().split())

house = []
chick = []

for i in range(n):
    a = list(map(int,input().split()))
    for j in range(n):
        if a[j] == 1:
            house.append((i,j))
        elif a[j] == 2:
            chick.append((i,j))
result = 1e9
# 치킨 집 M 개 조합
for k in combinations(chick, m):
    # 조합당 최단 거리
    temp = 0
    # 집 마다
    for home in house:
        # 치킨집 거리
        distance = 1e9 
        for v in range(m):
            distance = min(distance, abs(home[0]-k[v][0])+ abs(home[1]-k[v][1]))
        temp += distance
    result = min(result,temp)
            
print(result)