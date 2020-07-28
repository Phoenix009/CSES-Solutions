n, q = map(int, input().split())
arr = list(map(int, input().split()))
pre = [0 for i in range(n+1)]
for i in range(1, n+1):
    pre[i] = pre[i-1] + arr[i-1]

for i in range(q):
    a, b = map(int, input().split())
    print(pre[b] - pre[a-1])