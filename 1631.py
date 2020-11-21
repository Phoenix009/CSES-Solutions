

n = int(input())
arr = sorted(list(map(int, input().split())))


left = 0
right = sum(arr)
bestDiff = abs(left-right)
bestPart = right
for i in range(len(arr)):
    left += arr[i]
    right -= arr[i]
    newDiff = abs(left-right)
    if newDiff < bestDiff:
        bestDiff = newDiff
        bestPart = max(left, right)

print(bestPart*2)






