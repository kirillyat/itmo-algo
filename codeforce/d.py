INF = 100000000
NOEDGE = 100000

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

def find_negative_cycle(n, edges):
    dist = [INF] * n
    p = [-1] * n
    x = -1
    dist[0] = 0

    for i in range(n):
        x = -1
        for edge in edges:
            u, v, w = edge.u, edge.v, edge.w
            if dist[v] > dist[u] + w:
                dist[v] = max(-INF, dist[u] + w)
                p[v] = u
                x = v

    if x == -1:
        print("NO")
    else:
        print("YES")
        cycle = []
        y = x
        for i in range(n):
            y = p[y]
        
        cur = y
        while True:
            cycle.append(cur)
            if cur == y and len(cycle) > 1:
                break
            cur = p[cur]

        cycle.reverse()

        print(len(cycle) - 1)
        for i in range(1, len(cycle)):
            print(cycle[i] + 1, end=" " if i != len(cycle) - 1 else "\n")

def main():
    n = int(input())
    edges = []

    for i in range(n):
        for j, w in enumerate(map(int, input().split())):
            if w != NOEDGE:
                edges.append(Edge(i, j, w))

    find_negative_cycle(n, edges)

if __name__ == "__main__":
    main()