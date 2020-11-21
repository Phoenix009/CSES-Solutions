import sys
sys.setrecursionlimit(10**6)


def getStart(mat):
    x, y = 0, 0
    for x in range(n):
         for y in range(m):
            if mat[x][y] == 'A': return x, y
 
 
def getPath(mat, x, y, x_, y_, di, path):
    for i in range(4):
        tx, ty = x+x_[i], y+y_[i]
        if -1<tx<n and -1<ty<m and mat[tx][ty] != "#" and mat[tx][ty] !='X':
            if mat[tx][ty] == 'B': yield path + [di[i]]
            else:
                mat[tx][ty] = 'X'
                yield from getPath(mat, tx, ty, x_, y_, di, path+[di[i]])
                mat[tx][ty] = '.'
 
n, m = map(int, input().split())
mat = [list(sys.stdin.readline()) for i in range(n)]
x, y = getStart(mat)
x_ = [0, -1, 0, 1]
y_ = [-1, 0, 1, 0]
di = ['L', 'U', 'R', 'D']
 
ansPath = list(getPath(mat, x, y, x_, y_, di, []))
if not ansPath: print("NO")
else:
    bestPath = min(ansPath, key =  lambda x: len(x))
    print(len(bestPath))
    print("".join(bestPath))
