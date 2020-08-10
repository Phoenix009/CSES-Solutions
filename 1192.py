import sys

n, m = map(int, input().split())
mat = [list(sys.stdin.readline()) for i in range(n)]

vis = [[0 for i in range(m)] for i in range(n)]

_x = [-1, 0, 0, 1]
_y = [0, -1, 1, 0]

ans = 0
for i in range(n):
    for j in range(m):
        if mat[i][j] == '.':
            ans += 1
            mat[i][j] = 1
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                for k in range(4):
                    if -1 < x + _x[k] < n and -1 < y + _y[k] < m:
                        if mat[x+_x[k]][y+_y[k]] == '.' :
                            mat[x+_x[k]][y+_y[k]] = 1
                            stack.append((x+_x[k], y+_y[k]))

print(ans)



