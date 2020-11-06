n = int(input())
total = sum(list(map(int, input().split())))
actualTotal = (n*(n+1))//2
print(actualTotal - total)
