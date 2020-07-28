n = int(input())
arr = list(map(int, input().split()))

vis = dict(zip(
    arr,
    [False for i in range(n)]
))

idx = dict(zip(
    arr,
    [None for i in range(n)]
))

ans = 0
l = 0
r = 0
while(r < n):
    if vis[arr[r]]:
        for j in range(l, idx[arr[r]] + 1):
            vis[arr[j]] = False
        l = idx[arr[j]] + 1

    vis[arr[r]] = True
    idx[arr[r]] = r
    ans = max(ans, r-l+1)

    r += 1

print(ans)


