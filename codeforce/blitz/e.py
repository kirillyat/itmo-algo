import sys
from collections import defaultdict, Counter

def dfs(node, graph, colors, results):
    color_count = Counter({colors[node]: 1})
    for child in graph[node]:
        child_color_count = dfs(child, graph, colors, results)
        for color, count in child_color_count.items():
            color_count[color] += count
    
    results[node] = len(color_count)
    return color_count

def main():
    n = int(input().strip())
    
    if n == 1:
        print(1)
        return
    
    graph = defaultdict(list)
    colors = [0] * (n + 1)  # Задаем массив цветов для вершин
    
    for i in range(1, n + 1):
        p, c = map(int, input().strip().split())
        colors[i] = c
        if p != 0:
            graph[p].append(i)

    # Определение корня дерева (вершина без родителя)
    root = None
    for i in range(1, n + 1):
        if not any(i in graph[x] for x in graph if x != i):
            root = i
            break

    results = [0] * (n + 1)
    dfs(root, graph, colors, results)
    
    # Вывод результатов для каждой вершины
    print(" ".join(map(str, results[1:])))

if __name__ == "__main__":
    main()