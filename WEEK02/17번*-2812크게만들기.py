import sys
input = sys.stdin.readline

N, K = map(int, input().split())
M = list(input())

num = []
cnt = 0
for i in range(N):
    while cnt < K and num and num[-1] < M[i]:
        num.pop()
        cnt += 1
    num.append(M[i])

print(''.join(num[:N-K]))
    
