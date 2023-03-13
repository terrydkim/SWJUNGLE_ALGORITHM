import sys
input = sys.stdin.readline

N = int(input())
M = [int(input().strip()) for _ in range(N)]

result = 0
cnt = 0

for i in reversed(M) :
    x = M.pop()
    if result < x:
        result = x
        cnt+=1
print(cnt)