n = int(input())
arr = list(map(int, input().split()))
stack = []
ans = []
for i in range(1, n+1):
    while stack and stack[-1][0] >= arr[i-1]:
        stack.pop()
 
    if not stack:
        ans.append(0)
        stack.append((arr[i-1], i))
    else:
        ans.append(stack[-1][1])
        if arr[i-1] >= stack[-1][0]:
            stack.append((arr[i-1], i))
 
print(*ans)
