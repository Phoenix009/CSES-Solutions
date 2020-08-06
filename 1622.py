from itertools import permutations

ans = sorted(set(permutations(input())))
print(len(ans))
for i in ans:
    print(''.join(i))