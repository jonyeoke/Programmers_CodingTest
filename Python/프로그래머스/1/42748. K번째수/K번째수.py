def solution(array, commands):
    answer = []
    for now in commands:
        i = now[0]
        j = now[1]
        k = now[2]
        new = array[i-1:j]
        new = sorted(new)
        answer.append(new[k-1])
    return answer