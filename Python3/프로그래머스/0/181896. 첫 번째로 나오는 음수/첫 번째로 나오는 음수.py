def solution(num_list):
    answer = -1
    for i , now in enumerate(num_list):
        if now <0:
            answer = i
            break
    
    return answer