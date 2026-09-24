from collections import *

def solution(n, roads, sources, destination):
    answer = []
    que = deque()
    dist = [-1] * (n+1)
    
    adj=[[] for _ in range(n+1)]
    for n1, n2 in roads:
        adj[n1].append(n2)
        adj[n2].append(n1)
    dist[destination]=0
    
    que.append((destination, dist[destination]))
    
    while que:
        now, ndist = que.popleft()
        for nxt in adj[now]:
            if dist[nxt]==-1:
                dist[nxt]=ndist+1
                que.append((nxt, dist[nxt]))
    for src in sources:
        answer.append(dist[src])
    return answer