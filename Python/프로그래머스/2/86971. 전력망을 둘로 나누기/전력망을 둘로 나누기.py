from collections import defaultdict

def dfs(maps, visited, skipx, skipy, now):
    visited[now]=True
    count = 1
    for nxt in maps[now]:
        if not visited[nxt]:
            if not now in (skipx,skipy) or not nxt in (skipx,skipy):
                count += dfs(maps, visited, skipx, skipy, nxt)
    return count


def solution(n, wires):
    answer = 999
    maps = defaultdict(list)
    for x, y in wires:
        maps[x].append(y)
        maps[y].append(x)
    
    for i, toskip in enumerate(wires):
        skipx = toskip[0]
        skipy = toskip[1]
        visited = [False]*(n+1)
        answer = min(answer, abs(2*dfs(maps, visited, skipx,skipy, 1)-n))
        
    return answer