def getAns(arr, x):
    for i in range(n):
        l = i+1
        r = n-1
        while l < r:
            temp = arr[i][0] + arr[l][0] + arr[r][0]
            if temp == x:
                return arr[i][1]+1, arr[l][1]+1, arr[r][1]+1
            elif temp < x:
                l += 1
            else:
                r -= 1
    return -1, -1, -1


n, x = map(int, input().split())
temp = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append((temp[i], i))
arr = sorted(arr, key = lambda x: x[0])
i, l, r = getAns(arr, x)
if i == -1:
    print('IMPOSSIBLE')
else:
    print(i, l, r)



