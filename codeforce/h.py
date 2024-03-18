from collections import deque

def topological_sort(graph, n):
    in_degree = [0] * n
    for adj in graph.values():
        for _, v in adj:
            in_degree[v] += 1
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for _, v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    return order

def shortest_path(graph, n, s, t):
    order = topological_sort(graph, n)
    dist = [float('inf')] * n
    dist[s] = 0
    for u in order:
        if u in graph:  # Добавить проверку на наличие ключа
            for weight, v in graph[u]:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
    return dist[t]

n, m, s, t = map(int, input().split())

# Инициализация графа с пустым списком исходящих рёбер для каждой вершины
graph = {i: [] for i in range(n)}

for _ in range(m):
    b, e, w = map(int, input().split())
    graph[b-1].append((w, e-1))

result = shortest_path(graph, n, s-1, t-1)
if result == float('inf'):
    print("Unreachable")
else:
    print(result)
