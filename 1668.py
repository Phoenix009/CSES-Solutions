from collections import defaultdict
 
n, m = map(int, input().split())
graph = defaultdict(lambda : [])
teams = [0 for i in range(n)]
 
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
 
flg = True
i = 0
while i < n and flg:
    if not teams[i]:
        teams[i] = 1
        stack = [i+1]
        while stack and flg:
            currNode = stack.pop()
            for node in graph[currNode]:
                if teams[node-1] == 0:
                    teams[node-1] = 1 if teams[currNode-1] == 2 else 2
                    stack.append(node)
                elif teams[node-1] == teams[currNode-1]:
                    flg = False
                    break
    i += 1
 
if flg:
    print(*teams)
else:
    print('IMPOSSIBLE')
 
