n, m, x = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

ans = 0
j = 0
i = 0
while i < n and j < m:
    if abs(a[i] - b[j]) <= x:
        ans += 1
        i += 1
        j += 1
    elif a[i] < b[j]:
        i += 1
    else:
        j += 1
print(ans)
