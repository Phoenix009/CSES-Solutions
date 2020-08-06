MAX = 10**9
n = 20
arr = [1 for i in range(20)]
best = MAX
for i in range(2**n):
    part2 = 0
    part1 = 0
    temp = i
    j = 0
    while(j < n):
        if temp&1<<j:
            part2 += arr[j]
        else:
            part1 += arr[j]
        j += 1
    best = min(best, abs(part2 - part1))

print(best)
