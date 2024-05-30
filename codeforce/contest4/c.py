import sys
from collections import deque

class Edge:
    def __init__(self, to, max_capacity, rev_index):
        self.to = to
        self.max_capacity = max_capacity
        self.flow = 0
        self.rev_index = rev_index

    def get_capacity(self):
        return self.max_capacity - self.flow

class Net:
    def __init__(self, vq):
        self.vq = vq
        self.start = 0
        self.finish = vq - 1
        self.edges = [[] for _ in range(vq)]
        self.order = []

    def update_size(self, new_size):
        self.edges.extend([[] for _ in range(new_size - len(self.edges))])
        self.vq = new_size

    def add_connection(self, from_vertex, to_vertex, max_capacity=1):
        self.order.append((from_vertex, len(self.edges[from_vertex])))
        self._insert(from_vertex, to_vertex, max_capacity)

    def get_reverse(self, from_vertex, index):
        e = self.edges[from_vertex][index]
        return self.edges[e.to][e.rev_index]

    def _insert(self, from_vertex, to_vertex, max_capacity):
        self.edges[from_vertex].append(Edge(to_vertex, max_capacity, len(self.edges[to_vertex])))
        self.edges[to_vertex].append(Edge(from_vertex, 0, len(self.edges[from_vertex]) - 1))

def bfs(capacity, net):
    level = [float('inf')] * net.vq
    level[net.start] = 0

    q = deque([net.start])

    while q:
        v = q.popleft()
        for e in net.edges[v]:
            if level[e.to] == float('inf') and e.get_capacity() >= capacity:
                level[e.to] = level[v] + 1
                q.append(e.to)

    return level[net.finish] != float('inf'), level

def dfs(v, net, block, level, min_capacity=float('inf')):
    if v == net.finish or min_capacity == 0:
        return min_capacity

    while block[v] < len(net.edges[v]):
        e = net.edges[v][block[v]]
        if level[e.to] == level[v] + 1:
            flow_get = dfs(e.to, net, block, level, min(min_capacity, e.get_capacity()))
            if flow_get > 0:
                e.flow += flow_get
                net.get_reverse(v, block[v]).flow -= flow_get
                return flow_get
        block[v] += 1

    return 0

def dinic_iter(capacity, net):
    result = 0
    keep_going, level = bfs(capacity, net)
    while keep_going:
        block = [0] * net.vq
        flow = dfs(net.start, net, block, level)
        while flow:
            result += flow
            flow = dfs(net.start, net, block, level)
        keep_going, level = bfs(capacity, net)

    return result

def dinic(net):
    maxcap = 2**30  # Large initial integer capacity
    answer = 0
    while maxcap:
        answer += dinic_iter(maxcap, net)
        maxcap >>= 1  # Right shift on an integer
    return answer

def get_bipartie_matching(net, left_quantity):
    net.update_size(net.vq + 2)
    net.start = net.vq - 2
    net.finish = net.vq - 1

    for i in range(left_quantity):
        net.add_connection(net.start, i)
    for i in range(left_quantity, net.finish):
        net.add_connection(i, net.finish)

    dinic(net)

    result = []
    for i in range(net.start):
        for e in net.edges[i]:
            if e.flow == 1 and e.to < net.start:
                result.append((min(i, e.to), max(i, e.to) - left_quantity))

    return result

def main():
    left_quantity, right_quantity = map(int, input().split())
    net = Net(left_quantity + right_quantity)

    for i in range(left_quantity):
        connections = list(map(int, input().split()))
        for right in connections:
            if right == 0:
                break
            net.add_connection(i, left_quantity + right - 1)

    result = get_bipartie_matching(net, left_quantity)
    print(len(result))
    for first, second in result:
        print(f"{first + 1} {second + 1}")

if __name__ == "__main__":
    main()