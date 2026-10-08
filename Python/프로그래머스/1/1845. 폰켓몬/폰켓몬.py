def solution(nums):
    answer = 0
    
    seen = set()
    
    for n in nums:
        seen.add(n)
    
    return min(len(nums)/2, len(seen))