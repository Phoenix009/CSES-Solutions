

n, x = map(int, input().split())
coins = list(map(int, input().split()))
dp = [1]
for i in range(1, x+1):
    dp.append(0)
    for j in coins:
        if i-j > -1: dp[i] += dp[i-j]

print(dp[-1])

