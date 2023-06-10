from collections import deque


def solution(board):
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
    n,m = len(board), len(board[0])
    q = deque()
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                visited[i][j] = 1
                q.append((i,j))
    while q:
        a, b = q.popleft()
        if board[a][b] == "G":
            return visited[a][b] - 1
        for k in range(4):
            nr, nc = a,b
            while True:
                nr, nc = nr+dr[k], nc+dc[k]
                if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == "D":
                    nr -= dr[k]
                    nc -= dc[k]
                    break
                if nr < 0 or nr >= n or nc < 0  or nc >= m:
                    nr -= dr[k]
                    nc -= dc[k]
                    break
            if not visited[nr][nc]:
                visited[nr][nc] = visited[a][b] + 1
                q.append((nr,nc))
    return -1