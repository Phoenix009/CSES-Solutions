
def helper(coins, idx, rem):
    if rem == 0: return 1
    if idx == len(coins): return 0 
    elif (idx, rem) in dp: return dp[(idx, rem)]
    else:
        ans = 0
        i = 0
        while coins[idx]*i <= rem:
            ans += helper(coins, idx+1, rem-coins[idx]*i)
            i += 1
        dp[(idx, rem)] = ans
        return ans

n, x = map(int, input().split())
coins = list(map(int, input().split()))
dp = {}
ans = helper(coins, 0, x)
print(ans)
