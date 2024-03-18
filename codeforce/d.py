def find_negative_cycle(n, matrix):
    distance = [float('inf')] * n
    parent = [-1] * n
    x = -1
    
    # Исполнение алгоритма Беллмана-Форда
    for k in range(n):
        x = -1
        for i in range(n):
            for j in range(n):
                if matrix[i][j] != 100000 and distance[j] > distance[i] + matrix[i][j]:
                    distance[j] = max(-1e9, distance[i] + matrix[i][j])
                    parent[j] = i
                    x = j
    if x == -1:
        print("NO")
    else:
        # Восстановление цикла отрицательного веса
        for i in range(n):
            x = parent[x]
        
        cycle = []
        cur = x
        while True:
            cycle.append(cur)
            if cur == x and len(cycle) > 1:
                break
            cur = parent[cur]
        cycle = cycle[::-1]
        
        print("YES")
        print(len(cycle))
        print(' '.join([str(v + 1) for v in cycle]))

def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    find_negative_cycle(n, matrix)

if __name__ == "__main__":
    main()