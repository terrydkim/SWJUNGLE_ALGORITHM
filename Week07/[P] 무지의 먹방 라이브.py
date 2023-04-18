import heapq

def solution(food_times, k):
    answer = -1
    h =[]
    food_len = len(food_times)
    for i in range(food_len):
        heapq.heappush(h,(food_times[i],i+1))
    
    prev_food = 0
    while h:
        # 첫번째(최소)에서 이전 음식 빼기 * 전체 음식 개수
        t = (h[0][0]-prev_food) * food_len
        if k >= t:
            k -= t
            food_len -= 1
            prev_food,_ = heapq.heappop(h)
        else:
            # 전체 음식 개수보다 클 수 있으니까 %
            idx = k % food_len
            h.sort(key = lambda x : x[1])
            answer = h[idx][1]
            break
    return answer