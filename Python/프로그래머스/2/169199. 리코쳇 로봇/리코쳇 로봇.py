from collections import deque

def slide(grid, row, col, d_row, d_col):
    while True:
        next_row, next_col = row+d_row, col+d_col
        if next_row < 0 or next_col < 0 or next_row >= len(grid) or next_col>=len(grid[0]) or grid[next_row][next_col]=='D': break
        row,col=next_row, next_col
    return row,col

def solution(board):
    answer = 0
    found = False
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cur_row, cur_col = 0,0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=='R': 
                cur_row, cur_col = i,j
                found = True
                break
        if found:
            break
    visited = [[False]*len(board[0]) for _ in range(len(board))]
    
    queue = deque([(cur_row, cur_col, 0)])

    while queue:
        row, col, dist = queue.popleft()
        if board[row][col] == 'G':
            return dist
        for d_row, d_col in directions:
            next_row, next_col = slide(board, row, col, d_row, d_col)
            if not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                queue.append((next_row, next_col, dist+1))

    return -1