import sys
sys.setrecursionlimit(10**9)


def helper(i, j, turn, nums, scr1, scr2, dp):
    if i>j: return (scr1, scr2)
    elif (i, j, turn) in dp: 
        return dp[(i, j, turn)]
    elif (i, j, turn^1) in dp: 
        return reversed(dp[(i, j, turn)])
    else:
        if turn:
            ans = max(
                helper(i+1, j, turn^1, nums, scr1+nums[i], scr2, dp),
                helper(i, j-1, turn^1, nums, scr1+nums[j], scr2, dp),
            )
        else:
            ans = max(
                helper(i+1, j, turn^1, nums, scr1, scr2+nums[i], dp),
                helper(i, j-1, turn^1, nums, scr1, scr2+nums[j], dp),
            )
        dp[(i, j, turn)] = ans
        dp[(i, j, turn^1)] = tuple(reversed(ans))
        return ans


n = int(input())
nums = list(map(int, input().split()))
dp = {}
helper(0, n-1, 1, nums, 0, 0, dp)
print(max(*dp[(0, n-1, 1)], *dp[0, n-1, 0]))
