MOD = 10**9 + 7

n = int(input())

mat = [list(input()) for i in range(n)]
dp = [[0 for i in range(n)] for j in range(n)]


for i in range(n):
    for j in range(n):
        if (i, j) == (0, 0) and mat[i][j] == '.':
            dp[i][j] = 1
        if mat[i][j] == '.':
            if i-1 > -1: dp[i][j] += dp[i-1][j]
            if j-1 > -1: dp[i][j] += dp[i][j-1]
            dp[i][j] %= MOD

print(dp[-1][-1])




