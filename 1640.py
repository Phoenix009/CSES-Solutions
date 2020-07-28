n, x = map(int, input().split())
arr = list(map(int, input().split()))
vis = set()
idx = {}
for i in range(n):
    if x - arr[i] in vis:
        print(i+1, idx[x-arr[i]])
        break
    else:
        idx[arr[i]] = i+1
        vis.add(arr[i])
else:
    print('IMPOSSIBLE')
