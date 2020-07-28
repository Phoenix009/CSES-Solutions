n = int(input())
start = []
end = []
r = 0
for i in range(n):
    a, b = map(int, input().split())
    start.append(a)
    end.append(b)
    r = max(r, end)


arr = [0 for i in range(r+1)]
for i in start:
    arr[i] =  1

for i in end:
    arr[i] = -1

ans = 0
temp = 0
for i in range(len(arr)):
    temp += arr[i]
    arr[i] = temp
    ans = max(ans, arr[i])

print(ans)
