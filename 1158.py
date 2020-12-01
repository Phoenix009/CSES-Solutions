n, cap = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))


prev = [0 for i in range(cap+1)]
new = [0]
for i in range(1, n+1):
    for j in range(1, cap+1):
        new.append(prev[j])
        if j-weights[i-1] > -1:
            new[j] = max(new[j], prev[j-weights[i-1]] + values[i-1])
    prev= new
    new = [0]

print(prev[-1])


