
from heapq import heappop, heappush
from sys import stdin, stdout

def dijkstra(weights, time_limits, n):
    max_possible_cups = 30000  # С учетом максимально возможного веса 3 тонны и веса одной кружки
    queue = [(0, 0, 0)]  # Время, текущий город, количество кружек
    visited = [[False] * (max_possible_cups + 1) for _ in range(n + 1)]

    while queue:
        time, city, cups = heappop(queue)
        if city == n - 1:
            return cups
        if visited[city][cups]:
            continue
        visited[city][cups] = True

        for next_city, (limit, t) in enumerate(zip(weights[city], time_limits[city])):
            if limit >= cups * 100 + 3000000:  # Учет веса кружек и грузовика
                if time + t <= 1440:  # Не более 24 часов
                    heappush(queue, (time + t, next_city, cups))

    return 0

def main():
    n, m = map(int, stdin.readline().split())
    weights = [[0] * n for _ in range(n)]
    time_limits = [[1441] * n for _ in range(n)]

    for _ in range(m):
        a, b, t, w = map(int, stdin.readline().split())
        weights[a - 1][b - 1] = w
        weights[b - 1][a - 1] = w
        time_limits[a - 1][b - 1] = t
        time_limits[b - 1][a - 1] = t

    stdout.write(f"{dijkstra(weights, time_limits, n)}\n")

if __name__ == "__main__":
    main()
