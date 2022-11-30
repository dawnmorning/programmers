from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    # visited = [[0] for _ in range(m) for _ in range(n)]
    # visited[0][0] = 1
    # q = deque([(0,0)])
    q = deque()
    q.append((0,0))
    
    # cnt = 0
    while q:
        r, c = q.popleft()
        dr = [-1,1,0,0]
        dc = [0,0,-1,1] 
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] == 1:
                    maps[nr][nc] = maps[r][c] + 1
                    q.append((nr,nc))
    if maps[n-1][m-1] > 1:
        return maps[n-1][m-1]
    else:
        return -1