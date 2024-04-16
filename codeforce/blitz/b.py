import sys
sys.setrecursionlimit(10**8)

def main():
    n = int(input())  # Число вершин
    
    # Создаем структуру данных для графа и предков
    graph = [[] for _ in range(n + 1)]
    parent = [[-1] * 18 for _ in range(n + 1)]
    depth = [0] * (n + 1)
    LOG = 18
    
    # Чтение связей и построение графа
    for i in range(2, n + 1):
        x = int(input())
        graph[x].append(i)
        graph[i].append(x)
    
    # Функция для выполнения обхода в глубину (DFS)
    def dfs(v, p):
        parent[v][0] = p
        depth[v] = depth[p] + 1
        for u in graph[v]:
            if u != p:
                dfs(u, v)
    
    # Внеший DFS с корня дерева, который считаем 1
    dfs(1, 1)
    
    # Подготовка данных для быстрого вычисления LCA (Двоичный подъем)
    for i in range(1, LOG):
        for v in range(1, n + 1):
            if parent[v][i - 1] != -1:
                parent[v][i] = parent[parent[v][i - 1]][i - 1]
    
    # Функция для вычисления LCA
    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        
        # Поднимаем u на уровень v
        diff = depth[u] - depth[v]
        for i in range(LOG):
            if diff & (1 << i):
                u = parent[u][i]
        
        if u == v:
            return u
        
        # Поднимаем обоих до последнего общего предка
        for i in range(LOG - 1, -1, -1):
            if parent[u][i] != parent[v][i]:
                u = parent[u][i]
                v = parent[v][i]
        
        return parent[u][0]
    
    # Считываем количество запросов
    m = int(input())
    
    results = []
    for _ in range(m):
        u, v = map(int, input().split())
        results.append(str(lca(u, v)))
    
    # Вывод ответов на запросы
    print("\n".join(results))

if __name__ == "__main__":
    main()