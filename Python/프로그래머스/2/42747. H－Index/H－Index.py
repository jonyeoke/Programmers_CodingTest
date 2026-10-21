def solution(citations):
    answer = 0
    
    c = sorted(citations, reverse=True)
    
    for i, now in enumerate(c):
        if i+1 > now:
            return i
    return len(c)