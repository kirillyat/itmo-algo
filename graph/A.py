def dfs(v):
    color[v] = 1  # Серый цвет вершины
    for u in graph[v]:
        if color[u] == 0:  # У вершины белый цвет
            parent[u] = v  # Указываем родителя
            if dfs(u):
                return True
        elif color[u] == 1:  # У вершины серый цвет
            # Нашли цикл
            cycle.append(u)
            tmp = v
            while tmp != u:  # Восстанавливаем цикл
                cycle.append(tmp)
                tmp = parent[tmp]
            cycle.reverse() # Переворачиваем для правильного порядка
            return True
    color[v] = 2  # Черный цвет вершины
    return False

n, m = map(int, input().split())
graph = {i: [] for i in range(n)}
color = [0] * n  # 0 - белый, 1 - серый, 2 - черный
parent = [-1] * n
cycle = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)  # Нумерация с 0

for i in range(n):
    if color[i] == 0:  # Если вершина не посещена
        if dfs(i):
            print("YES")
            print(' '.join(map(str, [x + 1 for x in cycle])))  # Нумерация с 1
            break
else:  # Если цикл не найден
    print("NO")