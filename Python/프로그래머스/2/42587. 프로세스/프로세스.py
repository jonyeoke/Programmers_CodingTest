from collections import deque

def solution(priorities, location):
    answer = 0
    
    que = deque()
    
    for i in range(0,len(priorities)):
        que.append((i, priorities[i]))
        
    while que:
        cur = que.popleft()
        if que and cur[1] < max(que, key=lambda x: x[1])[1]:
            que.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
        
    
    
    return answer