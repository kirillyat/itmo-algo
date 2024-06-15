import heapq

def calc_clones_remaining(clones, droids):
    return clones if clones > droids else clones // 2

def maximum_clones_remaining(n, graph, clones, droids):
    clones_start = calc_clones_remaining(clones, droids[0])
    max_clones_room = [0] * n
    max_clones_room[0] = clones_start

    pq = [(-clones_start, 0)]
    while pq:
        clones_room, u = heapq.heappop(pq)
        clones_room = -clones_room

        if clones_room == 0:
            continue

        for v in graph[u]:
            clones_next_room = calc_clones_remaining(clones_room, droids[v])
            if clones_next_room > max_clones_room[v]:
                max_clones_room[v] = clones_next_room
                heapq.heappush(pq, (-clones_next_room, v))

    return max_clones_room[-1]


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

clones = int(input())
droids = [int(room) for room in input().split()]

print(maximum_clones_remaining(n, graph, clones, droids))

