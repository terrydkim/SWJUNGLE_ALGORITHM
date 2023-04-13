import sys, heapq
input = sys.stdin.readline
import math
N = int(input())

left = []
right = []

for _ in range(N):
    X = int(input().strip())
    if len(left) == len(right):
        heapq.heappush(left, -X)
    else: heapq.heappush(right, X)

    if left and right and left and -left[0] > right[0]:
        left_insert = -heapq.heappop(right)
        right_insert = -heapq.heappop(left)

        heapq.heappush(left, left_insert)
        heapq.heappush(right, right_insert)
    print(-left[0])