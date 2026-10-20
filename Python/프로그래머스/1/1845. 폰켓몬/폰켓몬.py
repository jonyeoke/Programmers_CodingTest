from collections import Counter
def solution(nums):
    answer = 0
    n = Counter(nums)
    return min(len(n),(len(nums)/2))
    return answer