from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 1
    q = deque()
    finished = []
    now = 1
    q.append((truck_weights[0],answer))
    
    while len(finished) < len(truck_weights) and q:
        answer+=1
        if answer-q[0][1]==bridge_length:
            finished.append(q.popleft())
        if now<len(truck_weights):
            if sum(x[0] for x in q)+truck_weights[now]<=weight:
                    q.append((truck_weights[now],answer))
                    now+=1
            
        
    
    return answer