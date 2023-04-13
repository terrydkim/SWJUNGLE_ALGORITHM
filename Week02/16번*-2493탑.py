import sys
input = sys.stdin.readline

a = int(input())

T = list(map(int, input().split()))

L=[]
point_tower = [0] * a

for i in range(a):
    while L:
        if L[-1][1] > T[i]:
            point_tower[i] = L[-1][0]
            break
        # 스택의 탑이 현재 탑보다 낮으면 팝
        L.pop()
    L.append((i+1,T[i]))

print(*point_tower)