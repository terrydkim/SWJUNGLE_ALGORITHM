def solution(nums):
    answer = 0
    dicts = {}
    for i in nums:
        if i in dicts:
            dicts[i] += 1
        else:
            dicts[i] = 1

    if len(nums) // 2 < len(dicts):
        return len(nums) // 2
    return len(dicts)



print(solution([3,3,3,2,2,2]))