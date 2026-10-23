from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    q = deque()
    
    for i, now in enumerate(progresses):
        q.append((now,math.ceil((100-now)/speeds[i])))
    while q:
        _, days = q.popleft()
        cnt = 1
        while len(q)>=1 and days>=q[0][1]:
            q.popleft()
            cnt+=1
        answer.append(cnt)
    
    return answer