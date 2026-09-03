def solution(n, m, section):        
    count = 0
    painted = 0
    for now in section:
        if now > painted:
            count+=1
            painted = now+m-1
            if painted > n:
                painted = n
        
    return count