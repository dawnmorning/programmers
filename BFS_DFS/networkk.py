def solution(n, computers):
    def DFS(i):
        visited[i] = 1
        for a in range(n):
            if computers[i][a] and not visited[a]:
                DFS(a)
    answer = 0
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer+=1
    return answer

print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	))
