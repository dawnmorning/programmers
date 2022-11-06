def solution(m, n, puddles):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for p in puddles:
        dp[p[1]][p[0]] == -1
    dp[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if dp[i][j] == 0:
                dp[i][j] = (max(dp[i-1][j],0) + max(dp[i][j-1],0))
    return dp[-1][-1]

print(solution(4,3,[[2,3]]))