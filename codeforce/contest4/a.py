from collections import deque

INF = float('inf')

class Edge:
    def __init__(self, a, b, c, f):
        self.a = a
        self.b = b
        self.c = c
        self.f = f

def dfs(u, flow):
    if u == t or flow == 0:
        return flow
    while p[u] < len(graph[u]):
        id = graph[u][p[u]]
        v = edges[id].b
        if d[v] == d[u] + 1:
            pushed = dfs(v, min(flow, edges[id].c - edges[id].f))
            if pushed:
                edges[id].f += pushed
                edges[id ^ 1].f -= pushed
                return pushed
        p[u] += 1
    return 0

def bfs():
    d[:] = [INF] * n
    d[s] = 0
    q.append(s)
    while q:
        u = q.popleft()
        for id in graph[u]:  # number of edge (uv)
            v = edges[id].b
            if d[v] == INF and edges[id].f < edges[id].c:
                d[v] = d[u] + 1
                q.append(v)
    return d[t] != INF

def algo_dinic():
    flow = 0
    while bfs():
        p[:] = [0] * n
        f = dfs(s, INF)
        while f:
            flow += f
            f = dfs(s, INF)
    return flow

if __name__ == "__main__":
    n, m = int(input()), int(input())
    graph = [[] for _ in range(n)]
    d = [0] * n
    p = [0] * n
    q = deque()
    edges = []

    s = 0
    t = n - 1

    for _ in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1
        graph[ai].append(len(edges))
        edges.append(Edge(ai, bi, ci, 0))
        graph[bi].append(len(edges))
        edges.append(Edge(bi, ai, ci, 0))

    result = algo_dinic()

    print(result)
    for i in range(0, 2 * m, 2):
        print(edges[i].f)