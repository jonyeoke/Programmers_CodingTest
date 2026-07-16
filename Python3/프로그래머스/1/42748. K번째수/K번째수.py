def solution(array, commands):
    answer = []
    for now in commands:
        i,j,k = now
        sublist = sorted(array[i-1:j])
        answer.append(sublist[k-1])
    return answer