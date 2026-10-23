def solution(citations):
    answer = 0
    c = sorted(citations, reverse=True)
    if len(c)==1: return 0
    i=0
    while i<len(c) and c[i] >= i+1:
        i+=1
        
    return i