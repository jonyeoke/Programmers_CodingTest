def dfs(visited, computers, now):
    visited[now]=True
    for i, nxt in enumerate(computers[now]):
        if nxt==1 and not visited[i]:
            dfs(visited, computers, i)
        

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for now in range(n):
        if visited[now]==False:
            answer+=1
            dfs(visited, computers, now)
    return answer