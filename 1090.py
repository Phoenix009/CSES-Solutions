n, x = map(int, input().split())
p = sorted(list(map(int, input().split())))

i = 0
j = n-1
ans = 0
while(i < j):
    if p[i] + p[j] <= x:
        ans += 1
        i += 1
        j -= 1
    else:
        if p[j] <= x:
            ans += 1
        j -= 1

if i == j and p[i] <x:
    ans += 1

print(ans)
