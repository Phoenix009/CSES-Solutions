n = int(input())
reqSum = ((n*(n+1))//2)/2
if reqSum % 1:
    print('NO')
else:
    print('YES')
    set1 = []
    set2 = []
    for i in range(n, 0, -1):
        if i <= reqSum:
            set1.append(i)
            reqSum -= i
        else:
            set2.append(i)
    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)
