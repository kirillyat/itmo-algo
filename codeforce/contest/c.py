
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# Алгоритм Флойда
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for row in graph:
    print(' '.join(map(str, row)))
