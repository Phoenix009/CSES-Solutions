n, cap = list(map(int, input().split()))
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

dp = [[0 for i in range(cap+1)] for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, cap+1):
        dp[i][j] = dp[i-1][j]
        if j-weights[i-1] > -1:
            dp[i][j] = max(dp[i][j], dp[i-1][j-weights[i-1]] + values[i-1])

print(dp[-1][-1])


