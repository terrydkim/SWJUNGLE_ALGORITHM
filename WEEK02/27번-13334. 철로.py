import heapq ,sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    start, end = map(int, input().split())
    if start > end:  # 시작점이 더 큰 경우, 뒤집어서 저장
        start, end = end, start
    arr.append((start, end))

d = int(input())
arr.sort(key=lambda x: x[1])  # 끝나는 지점을 기준으로 정렬



heap = []
cnt = 0
for start, end in arr:
    if end - start <= d:  # 길이가 d 이하인 경우만 고려
        heapq.heappush(heap, start)
        while heap and heap[0] < end - d:
            heapq.heappop(heap)
        cnt = max(cnt, len(heap))

print(cnt)