def dfs(v, direction, graph, gg, used, n):
    used[v] = True
    for i in range(n):
        if (gg[i][v] if direction else gg[v][i]) and not used[i]:
            dfs(i, direction, graph, gg, used, n)

def visit_all(used):
    return all(used)

def main():
    with open("avia.in", "r") as input_file:
        n = int(input_file.readline())
        graph = [list(map(int, input_file.readline().split())) for _ in range(n)]

    gg = [[0 for _ in range(n)] for _ in range(n)]  # Initialize gg as a 2D list
    used = [False] * n  # Initialize used as a list
    
    l, r = 0, 1000000000
    while l < r:
        middle = (l + r) // 2
        for i in range(n):
            for j in range(n):
                gg[i][j] = 1 if graph[i][j] <= middle else 0
        
        used = [False] * n
        dfs(0, False, graph, gg, used, n)
        
        done = False
        if visit_all(used):
            used = [False] * n
            dfs(0, True, graph, gg, used, n)
            if not visit_all(used):
                done = True
        else:
            done = True
        
        if not done:
            r = middle
        else:
            l = middle + 1

    with open("avia.out", "w") as output_file:
        output_file.write(f"{l}\n")

if __name__ == "__main__":
    main()