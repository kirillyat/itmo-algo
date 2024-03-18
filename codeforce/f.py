def bellman_ford(edges, N, M, K, S):
    distance = [[float('inf') for _ in range(N + 1)] for _ in range(K + 1)]
    distance[0][S] = 0
    
    for i in range(1, K + 1):
        for u, v, w in edges:
            if distance[i - 1][u] + w < distance[i][v]:
                distance[i][v] = distance[i - 1][u] + w
    
    return [distance[K][i] if distance[K][i] != float('inf') else -1 for i in range(1, N + 1)]

def main():
    N, M, K, S = map(int, input().split())
    edges = []
    
    for _ in range(M):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
        
    results = bellman_ford(edges, N, M, K, S)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
