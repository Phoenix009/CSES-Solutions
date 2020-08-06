def findAns(a, b):
    l = 0
    r = a // 2
    while l <= r:
        k1 = l + (r-l)//2
        k2 = a - 2*k1

        bPoss = 2*k2 + k1
        if bPoss == b:
            return True
        elif bPoss < b:
            r = k1-1
        else:
            l = k1+1

    return False



for t in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if findAns(a, b):
        print('YES')
    else:
        print('NO')
