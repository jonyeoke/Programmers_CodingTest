def solution(number, k):
    stack = []
    for x in number:
        while k > 0 and stack and stack[-1] < x:
            stack.pop()
            k -= 1
        stack.append(x)
    if k > 0:
        stack = stack[:-k]
    return ''.join(stack)