answer = -1
cnt = 0
n = 0


def dfs(k, dungeons, cnt):
    global answer
    if cnt > answer:
        answer = cnt

    for i in range(n):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = 1
            dfs(k - dungeons[i][1], dungeons, cnt + 1)
            visited[i] = 0


def solution(k, dungeons):
    global n, visited
    n = len(dungeons)
    visited = [0] * n
    dfs(k, dungeons, 0)
    return answer