MOD = 10**9 + 7
n, cap = map(int, input().split())
vals = list(map(int, input().split()))
dp = [[0 for j in range(cap+1)] for i in range(n)]

for i in range(n): dp[i][0] = 1

for i in range(n):
    for j in range(1, cap+1):
        if i-1 > -1: dp[i][j] += dp[i-1][j]
        if j-vals[i] > -1: dp[i][j] += dp[i][j-vals[i]]
        dp[i][j] %= MOD

print(dp[-1][-1])

