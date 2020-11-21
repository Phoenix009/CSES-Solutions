from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def helper(graph, currNode, ans):
    if not graph[currNode]:
        ans[currNode-1] = 0
        return 1
    else:
        temp = 0
        for node in graph[currNode]:
            temp += helper(graph, node, ans)
        ans[currNode-1] = temp
        return temp+1

def helperIter(graph):
    pass



n = int(input())
graph = defaultdict(set)
arr = list(map(int, input().split()))
for i in range(2, n+1):
    graph[arr[i-2]].add(i)

ans = [None for i in range(n)]
helper(graph, 1, ans)
print(*ans)

