def dfs(left, ways, visited, cnt, result):
    moved = False
    
    for i, v in enumerate(ways):
        if not visited[i] and left >= v[0]:
            moved = True
            visited[i]=True
            dfs(left-v[1],ways, visited, cnt+1,result)
            visited[i]=False
        if not moved:
            result.append(cnt)
    return

def solution(k, dungeons):
    answer = -1
    result = []
    dfs(k,dungeons,[False]*len(dungeons),0,result)
    return max(result)