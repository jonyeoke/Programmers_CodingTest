def solution(sizes):
    answer = 0
    
    s = []
    
    for now in sizes:
        if now[0] > now[1]:
            s.append((now[0],now[1]))
        else:
            s.append((now[1],now[0]))
    mh = max(v[0] for v in s)
    mv = max(v[1] for v in s)
    return mh*mv