def solution(answers):
    answer = [0,0,0]
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    i=0
    j=0
    k=0
    for now in answers:
        if now == s1[i]:
            answer[0]+=1
        if now == s2[j]:
            answer[1]+=1
        if now == s3[k]:
            answer[2]+=1
        i = (i+1)%len(s1)
        j = (j+1)%len(s2)
        k = (k+1)%len(s3)
    maxone = max(v for v in answer)
    res = []
    for idx, now in enumerate(answer):
        if now == maxone:
            res.append(idx+1)
    return res