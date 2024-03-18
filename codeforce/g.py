import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')]*n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u-1].append((v-1, w))
    graph[v-1].append((u-1, w))
    edges.append((u-1, v-1, w))

dist_from_start = dijkstra(graph, 0)
dist_from_end = dijkstra(graph, n-1)
min_path = dist_from_start[n-1]

max_increase = 0
for u, v, w in edges:
    # Путь при удвоении длины этой дороги
    increase = (dist_from_start[u] + w*2 + dist_from_end[v]) - min_path
    max_increase = max(max_increase, increase)
    increase = (dist_from_start[v] + w*2 + dist_from_end[u]) - min_path
    max_increase = max(max_increase, increase)

print(max_increase)
