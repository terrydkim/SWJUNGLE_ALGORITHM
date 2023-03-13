import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
# print(M,N,L)
X = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

X.sort()
# print(X)

cnt = 0


for a,b in A:
    hunting_range = L-b
    left = 0
    right = M - 1
    # 이 코드 없으면 시간초과남
    if b > L : 
        continue
    while left <= right:
        mid = (left+right)//2
        if abs(a-X[mid]) <= hunting_range:
            cnt += 1
            break
        elif a > X[mid]:
            left = mid + 1
        elif a < X[mid]:
            right = mid - 1
        
        
print(cnt)