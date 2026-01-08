def solution(n):
    matrix = [[0] * i for i in range(1, n + 1)]
    
    dy = [1, 0, -1]
    dx = [0, 1, -1]
    
    x = y = now = 0
    size = n * (n + 1) // 2
    num = 1
    
    while num <= size:
        matrix[y][x] = num
        num += 1
        nx = x + dx[now]
        ny = y + dy[now]
        
        if 0 <= ny < n and 0 <= nx < len(matrix[ny]) and matrix[ny][nx] == 0:
            x, y = nx, ny
        else:
            now = (now + 1) % 3
            x += dx[now]
            y += dy[now]
            
    answer = []
    for row in matrix:
        answer.extend(row)
        
    return answer