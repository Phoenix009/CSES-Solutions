
n, m = map(int, input().split())
t = sorted(list(map(int, input().split())))

ans = 0
lo, hi = 1, m*t[-1]
while lo <= hi:
    mid = lo + (hi-lo)//2
    rem = m
    flg = False
    for i in t:
        rem -= min(rem, mid//i)
        if not rem:
            flg = True
            break
    if flg:
        hi = mid-1
        ans = mid
    else:
        lo = mid+1

print(ans)







