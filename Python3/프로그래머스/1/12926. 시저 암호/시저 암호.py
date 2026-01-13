def solution(s, n):
    answer = ''
    save = []

    for now in s:
        if (65<=ord(now)<=90) or (97<=ord(now)<=122):
            std= ord('A') if (65<=ord(now)<=90) else ord('a')
            now=ord(now)
            now = ((now-std+n)%26)+std
            save.append(chr(now))
        else:
            save.append(now)
            continue
    return ''.join(save)