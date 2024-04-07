from collections import defaultdict

def dfs(vertex, color):
    colors[vertex] = color
    for next_vertex in graph[vertex]:
        if colors[next_vertex] == 0:  # Если вершина не была посещена
            dfs(next_vertex, color)

def read_input():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    return graph, n

graph, n = read_input()


colors = [0] * (n + 1)

current_color = 0

for vertex in range(1, n + 1):
    if colors[vertex] == 0:
        current_color += 1
        dfs(vertex, current_color)

print(' '.join(map(str, colors[1:])))