MOD = 10**9 + 7

n = int(input())
dp = [0, 1, 2, 4, 8, 16, 32]
for i in range(7, n+1):
    ans = dp[i-1]%MOD + dp[i-2]%MOD + dp[i-3]%MOD + dp[i-4]%MOD + dp[i-5]%MOD + dp[i-6]%MOD
    dp.append(ans % MOD)
print(dp[n])
