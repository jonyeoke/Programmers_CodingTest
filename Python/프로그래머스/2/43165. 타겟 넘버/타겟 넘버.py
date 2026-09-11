def target_recursive(n_idx, n_num, numbers, target):
    if n_idx == len(numbers):
        if n_num == target:
            return 1
        else: return 0
    
    
    return target_recursive(n_idx+1, n_num+numbers[n_idx], numbers, target) + target_recursive(n_idx+1, n_num-numbers[n_idx], numbers, target)
def solution(numbers, target):
    answer = target_recursive(0, 0, numbers, target)
    
    return answer