import sys
sys.setrecursionlimit(10**9)

n = int(input())

def helper(n, steps):
    if n == 0: return steps
    if n in dp: return steps + n
    else:
        dig = int(max(str(n)))
        ans = helper(n-dig, steps+1)
        dp[n] = ans
        return ans

dp = {}
print(helper(n, 0))

