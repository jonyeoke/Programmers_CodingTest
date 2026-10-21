
def transform(now, target):
    if ord(target) <= ord('N'):
        return ord(target) - ord('A')
    else:
        return ord('Z') - ord(target) + 1


def solution(name):
    answer = 0
    now = 'A' * len(name)

    for target in name:
        answer += transform('A', target)

    move = len(name) - 1

    for i in range(len(name)):
        next_idx = i + 1

        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1

        move = min(move, 2 * i + len(name) - next_idx)

        move = min(move, i + 2 * (len(name) - next_idx))

    answer += move

    return answer
