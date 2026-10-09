from collections import defaultdict

def solution(clothes):
    answer = 1
    dict = defaultdict(list)
    
    for n,i in clothes:
        dict[i].append(n)
    
    
    for now in dict:
        answer*=(len(dict[now])+1)
    
    
    return answer-1