from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque()
    i = 0

    while q or i < len(truck_weights):
        answer += 1

        for j in range(len(q)):
            q[j][1] -= 1

        if q and q[0][1] == 0:
            q.popleft()

        if (i < len(truck_weights)
            and sum(t[0] for t in q) + truck_weights[i] <= weight):
            q.append([truck_weights[i], bridge_length])
            i += 1

    return answer