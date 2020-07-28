MOD = 10**9 + 7

n = int(input())

mat = [list(input()) for i in range(n)]
dp = [[0 for i in range(n+1)] for j in range(n+1)]


for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 and j == 1:
            if mat[i-1][j-1] != '*':
                dp[i][j] = 1
        else:
            if mat[i-1][j-1] != '*':
                if i-2 > -1 and mat[i-2][j-1] != '*':
                    dp[i][j] += dp[i-1][j]
                if j-2 > -1 and mat[i-1][j-2] != '*':
                    dp[i][j] += dp[i][j-1]

        dp[i][j] %= MOD

print(dp[-1][-1])
