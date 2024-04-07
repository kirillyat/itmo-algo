def has_cycle(graph):
    visited = set()
    stack = set()
    path = []

    def dfs(node):
        if node in stack:
            index = path.index(node)
            print("YES")
            print(" ".join(map(str, path[index+1:] + [node])))
            return True
        if node in visited:
            return False

        visited.add(node)
        stack.add(node)
        path.append(node)

        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True

        stack.remove(node)
        path.pop()
        return False

    for node in graph:
        if dfs(node):
            return True

    return False

import collections
graph = collections.defaultdict(list)

n, m = list(map(int, input().split()))
for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)

if not has_cycle(graph):
    print('NO')
