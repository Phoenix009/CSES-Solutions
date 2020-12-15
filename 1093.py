MOD = 10**9 + 7

n = int(input())

cap = (n*(n+1))//2
if cap%2: print(0)
else:
    cap //= 2
    dp = [[0 for i in range(cap+1)] for i in range(n+1)]
    for i in range(n+1): dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, cap+1):
            dp[i][j] = dp[i-1][j]
            if j-i > -1: 
                dp[i][j] += dp[i-1][j-i] 
                dp[i][j] %= MOD

    print((dp[n][cap]//2)%MOD)

