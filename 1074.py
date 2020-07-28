n = int(input())
arr = sorted(list(map(int, input().split())))
med = arr[n//2]
ans = 0
for i in arr:
    ans += abs(med - i)

print(ans)
