from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)


def getDiameter(graph):
    def dfs(currNode, graph, parent):
        if not graph[currNode]: return 1
        else:
            maxLength = 0
            for node in graph[currNode]:
                if node != parent:
                    maxLength = max(maxLength,
                                    dfs(node, graph, currNode))
            return maxLength+1

    acc = []
    for node in graph[1]:
        acc.append(dfs(node, graph, 1))
    acc.sort()

    if len(graph[1]) == 1: return acc[-1] + 1
    else: return acc[-1] + acc[-2]

if __name__ == '__main__':
    n = int(input())
    graph = defaultdict(set)

    for i in range(n-1):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)
    
    ans = getDiameter(graph)
    print(ans)

