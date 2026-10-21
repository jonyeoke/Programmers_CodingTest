def dfs(now, moeum, count, target):
    if target == now:
        return count, True
    if len(now) == 5:
        return count, False
    for m in moeum:
        count += 1
        count, found = dfs(now + m, moeum, count, target)
        if found:
            return count, True
    return count, False

def solution(word):
    answer = 0
    moeum = ['A','E','I','O','U']

    answer, _ = dfs('', moeum, 0, word)
    return answer