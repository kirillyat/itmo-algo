maxFlow = 0
startSum = 0
targetSum = 0

class Edge:
    def __init__(self, from_vertex=-1, to_vertex=-1, flow=0):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.flow = flow

class Graph:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.v_num = height * width + 2
        self.checked = [False] * self.v_num
        self.edge = [[] for _ in range(self.v_num)]

    def add_edge(self, from_vertex, to_vertex, flow=1):
        self.edge[from_vertex].append(Edge(from_vertex, to_vertex, flow))
        self.edge[to_vertex].append(Edge(to_vertex, from_vertex, 0))  # Добавляем обратное ребро

    def uncheck_all(self):
        self.checked = [False] * self.v_num

    def to_vert_num(self, i, j):
        return i * self.width + j + 1

    def init(self):
        global startSum, targetSum

        for i in range(self.height):
            row = input().strip()
            for j in range(self.width):
                atom = row[j]
                valence_value = valence(atom)
                if (i % 2 + j % 2) % 2 == 0:
                    self.add_edge(0, self.to_vert_num(i, j), valence_value)
                    startSum += valence_value
                    if i + 1 < self.height:
                        self.add_edge(self.to_vert_num(i, j), self.to_vert_num(i + 1, j))
                    if j + 1 < self.width:
                        self.add_edge(self.to_vert_num(i, j), self.to_vert_num(i, j + 1))
                    if i - 1 >= 0:
                        self.add_edge(self.to_vert_num(i, j), self.to_vert_num(i - 1, j))
                    if j - 1 >= 0:
                        self.add_edge(self.to_vert_num(i, j), self.to_vert_num(i, j - 1))
                else:
                    self.add_edge(self.to_vert_num(i, j), self.v_num - 1, valence_value)
                    targetSum += valence_value

def find_back_edge(G, edge):
    for child in range(len(G.edge[edge.to_vertex])):
        if G.edge[edge.to_vertex][child].to_vertex == edge.from_vertex:
            return child
    return -1

def valence(atom):
    return {'H': 1, 'O': 2, 'N': 3, 'C': 4}.get(atom, 0)

def try_push_flow(G, current=0, capacity=float('inf')):
    global maxFlow

    G.checked[current] = True
    if current == G.v_num - 1:
        maxFlow += capacity
        return capacity

    for e in range(len(G.edge[current])):
        edge = G.edge[current][e]

        if G.checked[edge.to_vertex] or edge.flow == 0:
            continue

        min_capacity = try_push_flow(G, edge.to_vertex, min(edge.flow, capacity))
        if min_capacity > 0:
            G.edge[current][e].flow -= min_capacity
            back_edge_num = find_back_edge(G, edge)
            if back_edge_num != -1:
                G.edge[edge.to_vertex][back_edge_num].flow += min_capacity
            else:
                G.edge[edge.to_vertex].append(Edge(edge.to_vertex, current, min_capacity))
            return min_capacity

    return 0

if __name__ == "__main__":
    height, width = map(int, input().strip().split())
    maxFlow = 0
    startSum = 0
    targetSum = 0

    G = Graph(height, width)
    G.init()

    while try_push_flow(G):
        G.uncheck_all()

    if maxFlow == startSum == targetSum != 0:
        print("Valid")
    else:
        print("Invalid")