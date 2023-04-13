import sys
from itertools import combinations
input = sys.stdin.readline

N, C = map(int, input().split())
x = sorted([int(input().strip()) for _ in range(N)])


# print(x)

start = 1
end = x[-1]-x[0]

while start <= end:
    mid = (start+end) // 2
    # 첫 집에 공유기 설치
    count = 1
    prev_home = x[0]
    # 공유기 사이의 간격을 검색
    for i in range(1,N):
        if x[i]-prev_home >= mid:
            count += 1
            prev_home = x[i]
    if count >= C:
        start = mid +1
        ans = mid
    else: 
        end = mid - 1

print(ans)





# start = 1
# end = x[-1]-x[0]

# while start <= end:
#     mid = (start+end)//2
#     count = 1
#     prev_home = x[0]

#     for i in range(1, N):
#         if x[i]-prev_home >= mid:
#             count += 1
#             prev_home = x[i]
#     if count >= C:
#         start = mid + 1
#         answer = mid
#     else:
#         end = mid - 1

# print(answer)
