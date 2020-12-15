from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

def getAns(graph, currNode, marked, parent):
    if len(graph[currNode]):
        acc = 0
        for node in graph[currNode] :
            if node != parent:
                 acc += getAns(graph, node, marked, currNode)
                 if not marked[node-1] and not marked[currNode-1]:
                     marked[node-1] = True
                     marked[currNode-1] = True
                     acc += 1
        return acc
    
    return 0


n = int(input())
graph = defaultdict(set)
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

marked = [False for i in range(n)]
ans = getAns(graph, 1, marked, 0)
print(ans)


