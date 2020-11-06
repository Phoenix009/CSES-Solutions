def BFS(graph, src, dest):
    vis = [0 for i in range(n)]
    pred = [None for i in range(n)]
    vis[src - 1] = 1
 
    queue = [src]
    while queue and not pred[dest - 1]:
        currNode = queue.pop(0)
        for node in graph[currNode]:
            if not vis[node-1]:
                vis[node-1] = 1
                pred[node-1] = currNode
                queue.append(node)
    
    if not pred[dest - 1]:
        return False
    else:
        ans = []
        currNode = dest
        while pred[currNode - 1]:
            ans.append(currNode)
            currNode = pred[currNode - 1]
        ans.append(currNode)
        return ans[::-1]
 
 
 
 
n, m = map(int, input().split())
graph = dict(zip(
    range(1, n+1),
    [set() for i in range(n)]
))
 
for i in range(m):
    src, dest = map(int, input().split())
    graph[src].add(dest)
    graph[dest].add(src)
 
 
path = BFS(graph, 1, n)
if not path:
    print('IMPOSSIBLE')
else:
    print(len(path))
    print(*path)
