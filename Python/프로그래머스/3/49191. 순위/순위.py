from collections import defaultdict, deque

def bfs(grph, rgrph, start,n):
    que = deque()
    que.append(start)
    visited = [False]*(n+1)
    visited[0]=True
    visited[start]=True
    while que:
        now = que.popleft()
        visited[now]=True
        for next in grph[now]:
            if not visited[next]:
                que.append(next)
    rque = deque()
    rque.append(start)
    while rque:
        now = rque.popleft()
        visited[now]=True
        for next in rgrph[now]:
            if not visited[next]:
                rque.append(next)
    if False in visited: 
        return False
    else:
        return True

def solution(n, results):
    answer = 0
    graph = defaultdict(list)
    r_graph=defaultdict(list)
    for x, y in results:
        graph[x].append(y)
        r_graph[y].append(x)
    
    for i in range(1, n+1):
        isTrue = bfs(graph,r_graph,i,n)
        if isTrue:
            answer+=1
        
    return answer