def solution(A,B):
    answer = 0

    sorted_a = sorted(A)
    sorted_b = sorted(B, reverse=True)
    
    for i in range(0, len(A)):
        answer+=sorted_a[i]*sorted_b[i]
    
    return answer