from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    
    for i, now in enumerate(priorities):
        q.append((i,now))
    
    count = 0
    while q:
        maxone = max(x[1] for x in list(q))
        n, p = q.popleft()
        if p < maxone:
            q.append((n,p))
        else:
            count+=1
            if n==location:
                return count
    
    return answer