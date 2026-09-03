def solution(s):
    if len(s) == 1:
        return 1
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        res = ""
        cnt = 1
        now = s[:i]
        for j in range(i, len(s), i):
            if now == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    res += now
                else:
                    res += str(cnt) + now
                now = s[j:j+i]
                cnt = 1
        if cnt == 1:
            res += now
        else:
            res += str(cnt) + now
        answer = min(answer, len(res))
        
    return answer