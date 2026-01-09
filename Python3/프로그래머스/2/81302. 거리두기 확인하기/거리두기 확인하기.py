from collections import deque

def check(world):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    to_check = [(i,j) for i in range(5) for j in range (5) if world[i][j]=='P']
    
    for r,c in to_check:
        q = deque([(r, c, 0)])
        visited = [[False] * 5 for _ in range(5)]
        visited[r][c] = True
        
        while q:
            y, x, dist = q.popleft()
            if (dist==1 or dist==2) and world[y][x]=='P':
                return 0
            if dist>=2: continue
            
            for i in range(4):
                nr = y+dy[i]
                nc = x+dx[i]
                if 0<=nr<5 and 0<=nc<5:
                    if world[nr][nc]!='X' and visited[nr][nc]!=True:
                        if world[nr][nc] =='P':
                            return 0
                        
                        else: 
                            visited[nr][nc]=True
                            q.append((nr, nc, dist + 1))
    return 1
                
                
def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
                
    return answer