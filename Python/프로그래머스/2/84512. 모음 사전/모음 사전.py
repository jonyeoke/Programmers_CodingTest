def dfs(now, count, target, moeum):
    if now==target:
        return count, True
    if len(now)==5:
        return count, False
    for nxt in moeum:
        count, found = dfs(now+nxt, count+1, target, moeum)
        if found:
            return count, True
    
    return count, False

def solution(word):
    answer = 0
    moeum = ['A','E','I','O','U']
    answer, found = dfs('',0,word,moeum)
    if found: return answer
    return answer