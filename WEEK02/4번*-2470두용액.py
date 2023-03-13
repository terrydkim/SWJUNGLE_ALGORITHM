import sys
input = sys.stdin.readline

N = int(input())
L = sorted(list(map(int, input().split())))
result = []

left = 0
right = N-1

ans = float('inf')
# 투 포인터는 등호를 넣으면 같은 용액이 됨
while left < right:
    l = L[left]
    r = L[right]

    total = abs(l+r)
    if total < ans:
        ans = total
        result = [l, r]

    if l+r < 0:
        left += 1
    else:
        right -= 1
print(result[0], result[1])
