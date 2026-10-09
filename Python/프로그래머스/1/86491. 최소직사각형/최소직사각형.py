def solution(sizes):
    answer = 0
    
    for now in sizes:
        now.sort()
        
    max_row = max([x[0] for x in sizes])
    max_col = max([x[1] for x in sizes])
    answer = max_row*max_col
    return answer