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

        for neighbor, weight in enumerate(graph[current_vertex]):
            if weight >= 0:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

    return distances


n, s, f = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

distances = dijkstra(s - 1, graph)
print(distances[f - 1] if distances[f - 1] != float("inf") else -1)
