def solution(array, commands):
    answer = []
    
    for i,j,k in commands:
        now = array[i-1:j]
        now = sorted(now)
        answer.append(now[k-1])
    return answer