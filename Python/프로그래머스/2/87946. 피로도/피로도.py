

def dfs(now, items,visited,count):
    best = count
    for i in range(len(items)):
        if not visited[i] and now>=items[i][0]:
            visited[i]=True
            best=max(best,dfs(now-items[i][1],items,visited,count+1))
            visited[i]=False
    return best

def solution(k, dungeons):
    answer = -1
    visited=[False]*len(dungeons)
    return dfs(k,dungeons,visited,0)