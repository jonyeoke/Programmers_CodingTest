from collections import deque

def solution(maps):
    answer = 0
    q = deque()
    
    n = len(maps) # 행
    m = len(maps[0]) # 열
    # 시작점 0,0
    target = (n-1, m-1) # 도착점 n-1, m-1
    
    q.append((0,0,1))
    
    dnxt = ((0,1),(0,-1),(1,0),(-1,0))
    
    while q:
        nn, nm, cnt = q.popleft()
        if nn == n-1 and nm == m-1:
            return cnt
        for dn,dm in dnxt:
            nxtn = nn+dn
            nxtm = nm+dm
            
            if nxtn>=0 and nxtn<n and nxtm>=0 and nxtm<m:
                if maps[nxtn][nxtm] == 1:
                    maps[nxtn][nxtm]=0
                    q.append((nxtn, nxtm, cnt+1))
                    
    
    return -1