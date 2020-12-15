from bisect import bisect_right

n = int(input())
nums = list(map(int, input().split()))
res = [nums[0]]

for i in nums[1:]:
    if i <= res[-1]:
        idx = bisect_right(res, i)
        if idx != 0 and res[idx-1] == i: continue
        res[idx] = i
    else:
        res.append(i)
print(len(res))

