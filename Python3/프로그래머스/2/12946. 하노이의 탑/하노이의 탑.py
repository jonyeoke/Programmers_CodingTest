def recursive(n, start, mid, end, answer):
    if n==1:
        return answer.append([start,end])
    recursive(n-1,start,end,mid,answer)
    answer.append([start,end])
    recursive(n-1,mid,start,end,answer)


def solution(n):
    answer = []
    recursive(n,1,2,3,answer)
    return answer