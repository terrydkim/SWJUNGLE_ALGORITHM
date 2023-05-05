import sys
input = sys.stdin.readline

n = int(input())

location = list(map(int, input().split()))

prefix_sum = [0]*n

prefix_sum[0] = location[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + location[i]
print(prefix_sum)

# 벌 벌 꿀
honey = 0
for j in range(1,n-1):
    temp = 2 * prefix_sum[n-1] - (location[0]+location[i]) - prefix_sum[i-1]
    honey = max(honey,temp)

# 꿀 벌 벌
for k in range()

# 벌 꿀 벌
