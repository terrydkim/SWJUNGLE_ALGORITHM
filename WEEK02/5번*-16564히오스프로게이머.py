import sys
input = sys.stdin.readline

N, K = map(int, input().split())

X = [int(input().strip()) for _ in range(N)]

left, right = min(X), max(X) + K

while left <= right:
    goal = (left+right)//2
    need = sum([goal - level for level in X if goal - level > 0])
    
    if need <= K :
        left = goal + 1
        result = goal
    else : 
        right = goal - 1
print(result)

