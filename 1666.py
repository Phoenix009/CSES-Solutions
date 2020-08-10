n, m = map(int, input().split())
graph = dict(zip(
    range(1, n+1),
    [set() for i in range(n)]
))

for i in range(m):
    src, dest = map(int, input().split())
    graph[src].add(dest)
    graph[dest].add(src)



ans = []
prnt = None

vis = [0 for i in range(n)]

for currNode in graph:
    if not vis[currNode-1]:
        if not prnt:
            prnt = currNode
        else:
            ans.append((prnt, currNode))
        
        vis[currNode - 1] = 1
        stack = [currNode]
        while stack:
            _currNode = stack.pop()
            for node in graph[_currNode]:
                if not vis[node-1]:
                    vis[node-1] = 1
                    stack.append(node)

print(len(ans))
for i in ans:
    print(*i)

