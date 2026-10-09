def dfs(count, now, moeum, target,found):
    count+=1
    if now==target:
        return count, True
    if not found:
        if len(now)==5:
            return count, found
        for c in moeum:
            if found: break
            count,found = dfs(count, now+c, moeum, target, found)
    return count, found
        

def solution(word):
    answer = 0
    moeum=('A','E','I','O','U')
    
    count=0
    for m in moeum:
        answer, found = dfs(answer,m,moeum,word,False)
        if found: return answer
    
    return answer