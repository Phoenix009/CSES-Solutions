n = int(input())
nums = list(map(int, input().split()))
ans = 0
prev = nums[0]
for i in range(1, n):
    if nums[i] < prev:
        ans += (prev - nums[i])
    else:
        prev = nums[i]
 
print(ans)
