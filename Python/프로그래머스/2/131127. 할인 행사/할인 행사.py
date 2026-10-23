from collections import Counter

def solution(want, number, discount):
    answer = 0
    w = Counter()
    for i, now in enumerate(want):
        w[now]+=number[i]
    
    i = 0
    j = 9
    
    while j<len(discount):
        d = Counter(discount[i:j+1])
        if d==w: answer+=1
        j+=1
        i+=1
    
    return answer