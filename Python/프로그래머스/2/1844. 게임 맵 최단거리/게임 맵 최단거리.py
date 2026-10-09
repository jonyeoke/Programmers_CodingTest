from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False]* m for _ in range(n)]
    
    que = deque()
    count = 1
    que.append((0,0,count))
    
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    visited[0][0]=True
    while que:
        tn,tm,count = que.popleft()
        if tn==n-1 and tm==m-1: return count
        for nn,nm in dir:
            if nn+tn>=0 and nm+tm>=0 and nn+tn<n and nm+tm<m and not visited[nn+tn][nm+tm]:
                if maps[nn+tn][nm+tm] != 0:
                    visited[nn+tn][nm+tm]=True
                    que.append((nn+tn,nm+tm,count+1))
                    
    
    return -1