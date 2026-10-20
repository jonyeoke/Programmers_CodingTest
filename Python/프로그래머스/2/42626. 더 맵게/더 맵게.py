import heapq
def solution(scoville, K):
    answer = 0
    h=[]
    for now in scoville:
        heapq.heappush(h, now)
    
    while len(h)>=2 and h[0] < K:
        n1 = heapq.heappop(h)
        n2 = heapq.heappop(h)
        heapq.heappush(h, n1+n2*2)
        answer+=1
    if h[0] < K:
        return -1
    return answer