from collections import deque, defaultdict

def solution(n, edge):
    answer = []
    q = deque()
    d = defaultdict(list)
    for now, nxt in edge:
        d[now].append(nxt)
        d[nxt].append(now)
    visited = [False] * n
    
    count = 0
    
    q.append((1,count))
    visited[0]=True
    while q:
        now, cnt = q.popleft()
        for nxt in d[now]:
            if not visited[nxt-1]:
                visited[nxt-1]=True
                q.append((nxt, cnt+1))
                answer.append((nxt,cnt+1))
    answer = sorted(answer, key=lambda x:x[1],reverse=True)
    
    returned = 0
    for now in answer:
        if now[1] == answer[0][1]:
            returned+=1
    return returned