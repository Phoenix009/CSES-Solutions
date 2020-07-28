from bisect import bisect_right

n = int(input())
arr = list(map(int, input().split()))

ans = [arr[0]]
for i in range(1, n):
    idx = bisect_right(ans, arr[i])
    if idx == len(ans):
        ans.append(arr[i])
    else:
        ans[idx] = arr[i]

print(len(ans))
