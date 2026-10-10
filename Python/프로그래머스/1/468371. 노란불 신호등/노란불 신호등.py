def solution(signals):
    t = 1

    while True:
        all_yellow = True

        for g, y, r in signals:
            cycle = g + y + r
            time = (t - 1) % cycle

            if not (g <= time < g + y):
                all_yellow = False
                break

        if all_yellow:
            return t

        t += 1

        if t > __import__('math').lcm(*[sum(s) for s in signals]):
            return -1