from collections import defaultdict

def solution(clothes):
    answer = 1
    d = defaultdict(list)
    
    for c, k in clothes:
        d[k].append(c)
    
    for now in d:
        answer *= (len(d[now])+1)
    
    answer -= 1
    return answer