from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    
    q = deque()
    for i, now in enumerate(progresses):
        q.append(math.ceil((100-now)/speeds[i]))
    
    while q:
        now = q.popleft()
        count = 1
        while q and now>=q[0]:
            q.popleft()
            count+=1
        answer.append(count)
    
    return answer