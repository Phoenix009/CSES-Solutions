n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = list(map(int, input().split()))

temp = []
for i in range(m):
    temp.append((b[i], i))

b = sorted(temp, key=lambda x: x[0])



i = n-1
j = m-1

ans = [-1 for i in range(m)]

while i > -1 and j > -1:
    if b[j][0] >= a[i]:
        ans[b[j][1]] = a[i]
        i -= 1
        j -= 1
    else:
        i -= 1
for i in ans:
    print(i)


