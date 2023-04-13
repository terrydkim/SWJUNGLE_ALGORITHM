import sys
input = sys.stdin.readline

N = int(input())

lst = []
for _ in range(N):
    b = int(input())
    
    lst.append(b) if not b == 0 else lst.pop()

print(sum(lst))