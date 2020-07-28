n = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]
for i in arr[1:]:
    dp.append(max(dp[-1] + i, i))
print(max(dp))
