def solution(numbers, target):
    answer = dfs(numbers, target, 0)
    return answer

# idx가 depth 역할도 함
def dfs(numbers,target,idx):
    count = 0
    
    if idx == len(numbers):
        if sum(numbers) == target:
            return 1
        return 0
    else:
        count += dfs(numbers,target,idx+1) # + 일때
        numbers[idx] *= -1
        count += dfs(numbers,target,idx+1) # - 일때
        return count
        