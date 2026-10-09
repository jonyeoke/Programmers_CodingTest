from collections import defaultdict, deque

def solution(n, wires):
    answer = []
    maps = defaultdict(list)
    
    for x, y in wires:
        maps[x].append(y)
        maps[y].append(x)
    
    
    
    for skip in wires:
        que = deque()
        visited=[False]*n
        count = 0
        
        que.append(1)
        visited[0]=True
        while que:
            now = que.popleft()
            for nxt in maps[now]:
                if visited[nxt-1]==True: continue
                if now in skip and nxt in skip: continue
                visited[nxt-1]=True
                que.append(nxt)
        for check in visited:
            if check: count+=1
        answer.append(abs(2*count-n))
    
    
    
    return min(answer)