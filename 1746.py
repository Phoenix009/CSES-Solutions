MOD = 10**9 + 7
n, m = map(int, input().split())
val = list(map(int, input().split()))

dp = [[0 for i in range(m+2)] for i in range(n)]
if val[0] == 0:
    for j in range(m+1): dp[0][j] = 1
dp[0][val[0]] = 1

for i in range(1, n):
    if val[i]:
        for j in [val[i]-1, val[i], val[i]+1]:
            dp[i][val[i]] += dp[i-1][j]%MOD if 1 <= j <= m else 0
    else:
        for j in range(1, m+1):
            for k in [j-1, j, j+1]:
                dp[i][j] += dp[i-1][k]%MOD if 1 <= k <= m else 0
            
print(sum(dp[-1][1:-1])%MOD)

