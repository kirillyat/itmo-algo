import heapq

def dijkstra(start, graph):
    n = len(graph)
    distances = [float("inf")] * n
    distances[start] = 0

    queue = [(0, start)]
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))

distances = dijkstra(0, graph)
print(' '.join(map(str, distances)))