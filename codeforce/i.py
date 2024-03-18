import heapq

def can_deliver(max_weight, n, roads, time_limit=1440): # 1440 минут в сутках
    # Создаём адъяксентный список для графа
    adj = [[] for _ in range(n)]
    for a, b, t, w in roads:
        if w >= max_weight:  # Дорога может выдержать вес
            adj[a-1].append((b-1, t))
            adj[b-1].append((a-1, t))
    
    # Алгоритм Дейкстры с модификацией
    distance = [float('inf')] * n
    distance[0] = 0  # начинаем с города 1

    queue = [(0, 0)] # (время, город)
    while queue:
        current_time, u = heapq.heappop(queue)
        
        if current_time > distance[u]:
            continue
        
        for v, time in adj[u]:
            if current_time + time < distance[v]:
                distance[v] = current_time + time
                heapq.heappush(queue, (distance[v], v))

    # Проверяем, достигли ли мы Иннополис (город n) в заданное время
    return distance[n-1] <= time_limit


def binary_search(n, m, roads):
    left, right = 0, 30000  # начинаем двоичный поиск от 0 кружек до максимально возможного
    while left < right:
        mid = (left + right + 1) // 2
        weight = 3000 + mid * 0.1 # текущий вес грузовика в кг с кружками
        if can_deliver(weight, n, roads):
            left = mid
        else:
            right = mid - 1
    return left

n, m = map(int, input().split())
roads = []
for _ in range(m):
    a, b, t, w = map(int, input().split())
    roads.append((a, b, t, w)) 
max_cups = binary_search(n, m, roads)
print(max_cups)