from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    
    unq = list(set("".join(words)))
    
    visited =[False]*len(words)
    
    q.append((begin,answer))
    while q:
        now, count = q.popleft()
        if now == target:
            return count
        for i in range(len(now)):
            for c in unq:
                newone = now[:i]+c+now[i+1:]
                for j, mm in enumerate(words):
                    if not visited[j] and mm==newone:
                        visited[j]=True
                        q.append((newone,count+1))
        
        
    return 0