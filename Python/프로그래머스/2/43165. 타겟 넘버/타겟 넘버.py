def dfs(now, step, numbers, target):
    if step==len(numbers)+1:
        if now == target:
            return 1
        else: return 0
    
    minus = dfs(now-numbers[step-1], step+1, numbers, target)
    plus = dfs(now+numbers[step-1], step+1,numbers, target)
    return minus + plus

def solution(numbers, target):
    answer = 0
    
    return dfs(0,1,numbers,target)
    return answer