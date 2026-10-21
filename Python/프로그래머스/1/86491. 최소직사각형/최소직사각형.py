def solution(sizes):
    answer = 0
    
    v = []
    h = []
    
    for i, j in sizes:
        if i<j:
            v.append(j)
            h.append(i)
        else:
            v.append(i)
            h.append(j)
    return max(v) * max(h)
    return answer