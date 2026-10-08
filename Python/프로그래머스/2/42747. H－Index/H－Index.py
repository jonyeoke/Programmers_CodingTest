def solution(citations):
    answer = 0
    
    sc = sorted(citations,reverse=True)
    
    now = 0
    
    while now<len(sc) and now+1<=sc[now]:
        now+=1
    return now