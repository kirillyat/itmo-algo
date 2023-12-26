def dfs(vertex, graph, visited, order, cycle_detected):
    if cycle_detected[0]:  
        return
    visited[vertex] = 1 
    for neighbor in graph[vertex]:
        if visited[neighbor] == 0:
            dfs(neighbor, graph, visited, order, cycle_detected)
        elif visited[neighbor] == 1:
            cycle_detected[0] = True 
            return
    visited[vertex] = 2  
    order.append(vertex)  

def topological_sort(n, edges):
    graph = {i: [] for i in range(1, n + 1)}
    visited = {i: 0 for i in range(1, n + 1)}  #
    order = []
    cycle_detected = [False] 

    for u, v in edges:
        graph[u].append(v)

    for vertex in range(1, n + 1):
        if visited[vertex] == 0:
            dfs(vertex, graph, visited, order, cycle_detected)
            if cycle_detected[0]:
                return -1  

    return order[::-1]  


n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

sorted_order = topological_sort(n, edges)

if sorted_order == -1:
    print(-1)
else:
    print(*sorted_order)