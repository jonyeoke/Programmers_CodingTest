from collections import defaultdict

def dfs(tckt, now, path, n):
    if len(path) == n + 1:
        return True

    for idx, [nxt, visited] in enumerate(tckt[now]):
        if not visited:
            path.append(nxt)
            tckt[now][idx][1] = True

            if dfs(tckt, nxt, path, n):
                return True

            tckt[now][idx][1] = False
            path.pop()



def solution(tickets):
    tckt = defaultdict(list)

    for now, nxt in tickets:
        tckt[now].append([nxt, False])

    for key in tckt:
        tckt[key].sort()

    path = ["ICN"]
    dfs(tckt, "ICN", path, len(tickets))

    return path