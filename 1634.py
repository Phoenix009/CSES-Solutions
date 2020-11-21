MAX = 10**9
n, cap = map(int, input().split())
w = list(map(int, input().split()))
ans = [0]
for i in range(1, cap+1):
    temp = MAX
    for j in w:
        temp = min(temp, ans[i-j]+1 if i-j > -1 else MAX)
    ans.append(temp)
print(ans[-1])


