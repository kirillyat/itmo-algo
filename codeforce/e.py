def bellman_ford(n, m, s, edges):
    # Инициализация расстояний бесконечностями
    distance = [float('inf')] * n
    distance[s - 1] = 0  # Расстояние до начальной вершины равно 0

    # Алгоритм Беллмана-Форда
    for i in range(n - 1):
        for u, v, w in edges:
            if distance[u - 1] != float('inf') and distance[u - 1] + w < distance[v - 1]:
                distance[v - 1] = distance[u - 1] + w

    # Проверка на циклы отрицательного веса
    cycle = set()
    for i in range(n):
        for u, v, w in edges:
            if distance[u - 1] != float('inf') and distance[u - 1] + w < distance[v - 1]:
                distance[v - 1] = float('-inf')
                cycle.add(v - 1)

    # Вывод результатов
    for d in distance:
        if d == float('inf'):
            print('*')
        elif d == float('-inf'):
            print('-')
        else:
            print(d)

def main():
    n, m, s = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    bellman_ford(n, m, s, edges)

if __name__ == "__main__":
    main()