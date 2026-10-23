def solution(nums):
    answer = 0
    s = list(set(nums))
    
    return min(len(nums)//2, len(s))