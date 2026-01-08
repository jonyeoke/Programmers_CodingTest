def rotate(x1,y1,x2,y2,mat):
    save = mat[x1][y1]
    min_value = int(1e15)
    
    for i in range(x1,x2):
        mat[i][y1] = mat[i+1][y1]
        min_value = min(min_value, mat[i+1][y1])
    for i in range(y1,y2):
        mat[x2][i] = mat[x2][i+1]
        min_value = min(min_value, mat[x2][i+1])
    for i in range(x2,x1,-1):
        mat[i][y2] = mat[i-1][y2]
        min_value = min(min_value, mat[i-1][y2])
    for i in range(y2,y1,-1):
        mat[x1][i] = mat[x1][i-1]
        min_value = min(min_value, mat[x1][i-1])
    mat[x1][y1+1]=save
    min_value = min(min_value,save)
    return min_value

def solution(rows, columns, queries):
    answer = []
    matrix = []
    
    matrix = [0] * rows 
    for i in range(rows):
        matrix[i] = [0] * columns
    for i in range(rows):
        for j in range(columns):
            matrix[i][j]=i*columns+j+1
    for x1, y1, x2, y2 in queries:
        answer.append(rotate(x1-1,y1-1,x2-1,y2-1,matrix))
    return answer