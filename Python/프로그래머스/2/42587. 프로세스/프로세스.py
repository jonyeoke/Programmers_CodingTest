def solution(priorities, location):
    answer = 0
    que = []
    
    for i, pri in enumerate(priorities):
        que.append((i,pri))
    
    while que:
        idx, now = que.pop(0)
        if any(n[1] > now for n in que):
            que.append((idx,now))
        else:
            answer+=1
            if idx == location:
                return answer
    
    return answer