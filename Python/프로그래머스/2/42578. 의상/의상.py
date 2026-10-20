from collections import defaultdict

def solution(clothes):
    answer = 1
    dicts = defaultdict(list)
    
    for now in clothes:
        dicts[now[1]].append(now[0])
        
    for now in dicts:
        answer*=(len(dicts[now])+1)
    return answer-1
    