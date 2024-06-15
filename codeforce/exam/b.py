import heapq
import math

def dijkstra(node_count, adjacency_list, start_node, max_cost_allowed=None, min_cost_allowed=None):
    min_distances = [math.inf] * node_count
    min_distances[start_node] = 0
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)
        if current_distance > min_distances[u]:
            continue

        for cost, v in adjacency_list[u]:
            if (max_cost_allowed is not None and cost > max_cost_allowed) or (min_cost_allowed is not None and cost < min_cost_allowed):
                continue
            updated_distance = current_distance + cost
            if updated_distance < min_distances[v]:
                min_distances[v] = updated_distance
                heapq.heappush(priority_queue, (updated_distance, v))

    return min_distances


def find_shortest_path_with_cost_constraints(node_count, edge_count, start_node, end_node, edge_list, max_cost_A, min_cost_B):

    adjacent_list = [[] for _ in range(node_count)]
    for u, v, w in edge_list:
        adjacent_list[u - 1].append((w, v - 1))
        adjacent_list[v - 1].append((w, u - 1))

    distance_from_start = dijkstra(node_count, adjacent_list, start_node - 1, max_cost_allowed=max_cost_A)
    distance_from_end = dijkstra(node_count, adjacent_list, end_node - 1, min_cost_allowed=min_cost_B)

    min_cost = float('inf')
    for i in range(node_count):
        if distance_from_start[i] != float('inf') and distance_from_end[i] != float('inf'):
            min_cost = min(min_cost, distance_from_start[i] + distance_from_end[i])

    return min_cost if min_cost != float('inf') else -1


def main():
    n, m = map(int, input().strip().split())
    s, t = map(int, input().strip().split())
    edge_info = [tuple(map(int, input().strip().split())) for _ in range(m)]
    a_limit, b_limit = map(int, input().strip().split())

    result = find_shortest_path_with_cost_constraints(n, m, s, t, edge_info, a_limit, b_limit)
    print(result)


if __name__ == "__main__":
    main()