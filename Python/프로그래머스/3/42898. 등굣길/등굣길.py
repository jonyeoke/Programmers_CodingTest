def solution(m, n, puddles):
    answer = 0
    
    grid = [[0]*(m+1) for _ in range(0, n+1)]
    
    grid[1][1] = 1
    
    for px, py in puddles:
        grid[py][px] = -1
        
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if (r == 1 and c == 1) or grid[r][c] == -1:
                continue
            if grid[r-1][c] == -1:
                top = 0
            else: top = grid[r-1][c]
            if grid[r][c-1] == -1:
                left = 0
            else: left = grid[r][c-1]
            grid[r][c] = (top+left) % 1_000_000_007
    
    return grid[n][m]