count=0
found=False

def recursive(target, now):
    global count, found
    if now == target:
        found = True
        return

    if len(now) >= 5:
        return

    aeiou = ['A', 'E', 'I', 'O', 'U']
    
    for char in aeiou:
        if found:
            return
        
        count += 1
        recursive(target, now + char)

def solution(word):
    global count, found
    recursive(word, '')
    
    return count