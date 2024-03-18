import heapq

def find_next_good_weather(start_time, good_weathers):
    for x, y in good_weathers:
        if start_time <= y:  # Если начальное время уже находится в одном из хороших интервалов или раньше
            return max(start_time, x)
    return None  # Если после всех хороших интервалов

def dijkstra_with_weather(n, edges, good_weathers, start, end, start_time):
    graph = [[] for _ in range(n)]
    for u, v, w, q in edges:
        graph[u].append((v, w, q))
        graph[v].append((u, w, q))

    queue = [(start_time, start)]
    distances = [float('inf')] * n
    distances[start] = start_time

    while queue:
        time, u = heapq.heappop(queue)
        if time > distances[u]:
            continue
        for v, w, q in graph[u]:
            next_time = time
            if q == 1:  # Если дорога плохая
                next_time = find_next_good_weather(time, good_weathers)
                if next_time is None:  # Если нет подходящего времени
                    continue
            
            next_time += w
            if next_time < distances[v]:
                distances[v] = next_time
                heapq.heappush(queue, (next_time, v))
    
    return distances[end] if distances[end] != float('inf') else -1

n, m, k = map(int, input().split())  # Ввод данных
edges = [list(map(int, input().split())) for _ in range(m)]
good_weathers = [tuple(map(int, input().split())) for _ in range(k)]
a, b, t0 = map(int, input().split())

# Индексы узлов корректируются на -1, чтобы соответствовать индексации с 0
edges = [[u-1, v-1, w, q] for u, v, w, q in edges]
a -= 1
b -= 1

print(dijkstra_with_weather(n, edges, good_weathers, a, b, t0))
