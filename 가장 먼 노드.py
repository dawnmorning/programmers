from collections import deque


def solution(n, edge):
    answer = 0
    visited = [0] * (n + 1)
    q = deque([1])
    arr = [[] for i in range(n + 1)]
    for e in edge:
        arr[e[0]].append(e[1])
        arr[e[1]].append(e[0])
    # q.append(1)
    visited[1] = 1
    while q:
        now = q.popleft()
        for i in arr[now]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[now] + 1

    for v in visited:
        if max(visited) == v:
            answer += 1
    return answer