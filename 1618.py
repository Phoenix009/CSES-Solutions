n = int(input())
ans = 0
i = 5
while n//i:
    ans += n//i
    i *= 5
print(ans)
