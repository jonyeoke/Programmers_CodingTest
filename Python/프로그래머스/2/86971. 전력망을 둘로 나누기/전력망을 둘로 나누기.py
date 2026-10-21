from collections import deque, defaultdict



def solution(n, wires):
    answer = []
    maps = defaultdict(list)
    
    for x, y in wires:
        maps[x].append(y)
        maps[y].append(x)
    
    for idx, skip in enumerate(wires):
        # idx = pass할 index, (a,b): pass할 edge이자 각 시작점
        que = deque()
        visited=[False]*n
        count = 0
        
        que.append(1)
        visited[0]=True
        
        while que:
            now = que.popleft()
            for nxt in maps[now]:
                if not visited[nxt-1] and now not in skip and nxt not in skip:
                    visited[nxt-1]=True
                    que.append(nxt)
        for check in visited:
            if check: count+=1
        answer.append(abs(2*count-n))
                    
        
    return min(answer)