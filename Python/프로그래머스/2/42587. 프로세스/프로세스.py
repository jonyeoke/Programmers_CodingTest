from collections import deque
def solution(priorities, location):
    answer = 0
    
    q = deque()
    for i, now in enumerate(priorities):
        q.append((i,now))
    
    found = False
    while q:
        i, now = q.popleft()
        if q and now < max(q, key=lambda x:x[1])[1]:
            q.append((i,now))
            continue
        answer+=1
        if i == location:
            return answer
        
    return answer