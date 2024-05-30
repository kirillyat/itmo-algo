from math import inf
from collections import deque

class Edge:
    def __init__(self, from_v, to_v, capacity, reverse_index):
        self.from_v = from_v
        self.to_v = to_v
        self.capacity = capacity
        self.flow = 0
        self.reverse_index = reverse_index

class Graph:
    def __init__(self, n):
        self.size = n
        self.adj = [[] for _ in range(self.size)]
        self.edge_order = []
        self.cut_edges = []
        self.total_caps = 0

    def add_edge(self, from_v, to_v, capacity):
        forward_edge = Edge(from_v, to_v, capacity, len(self.adj[to_v]))
        backward_edge = Edge(to_v, from_v, 0, len(self.adj[from_v]) - 1)
        self.adj[from_v].append(forward_edge)
        self.adj[to_v].append(backward_edge)
        self.edge_order.append(forward_edge)

    def push(self, v, t, flow, used):
        if v == t:
            return flow
        used[v] = True
        for edge in self.adj[v]:
            if not used[edge.to_v] and edge.flow < edge.capacity:
                next_flow = min(flow, edge.capacity - edge.flow)
                delta = self.push(edge.to_v, t, next_flow, used)
                if delta > 0:
                    edge.flow += delta
                    self.adj[edge.to_v][edge.reverse_index].flow -= delta
                    return delta
        return 0

    def bfs(self, s, t):
        dist = [-1] * self.size
        dist[s] = 0
        queue = deque([s])

        while queue:
            v = queue.popleft()
            for edge in self.adj[v]:
                if edge.flow < edge.capacity and dist[edge.to_v] == -1:
                    dist[edge.to_v] = dist[v] + 1
                    queue.append(edge.to_v)

        return dist[t] != -1

    def mark_reachable(self, v, reachable):
        if reachable[v]:
            return
        reachable[v] = True
        for edge in self.adj[v]:
            if edge.flow < edge.capacity:
                self.mark_reachable(edge.to_v, reachable)

    def find_min_cut(self, s):
        reachable = [False] * self.size
        self.mark_reachable(s, reachable)

        for edge in self.edge_order:
            if reachable[edge.from_v] and not reachable[edge.to_v]:
                self.cut_edges.append(f"{self.edge_order.index(edge) + 1}")
                self.total_caps += edge.capacity

def read_graph():
    n, m = map(int, input().split())
    graph = Graph(n)
    for _ in range(m):
        u, v, c = map(int, input().split())
        graph.add_edge(u - 1, v - 1, c)
    return graph

def main():
    graph = read_graph()
    s, t = 0, graph.size - 1
    max_flow = 0

    while graph.bfs(s, t):
        used = [False] * graph.size
        while True:
            delta = graph.push(s, t, inf, used)
            if delta <= 0:
                break
            max_flow += delta

    graph.find_min_cut(s)
    print(len(graph.cut_edges), graph.total_caps)
    print(" ".join(graph.cut_edges))

if __name__ == '__main__':
    main()