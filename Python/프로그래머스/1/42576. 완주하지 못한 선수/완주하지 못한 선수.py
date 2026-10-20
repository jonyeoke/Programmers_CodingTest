def solution(participant, completion):
    answer = ''
    sorted_p = sorted(participant)
    sorted_c = sorted(completion)
    for i, now in enumerate(sorted_c):
        if sorted_p[i] != now:
            return sorted_p[i]
    return sorted_p[-1]