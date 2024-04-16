import sys
from sys import setrecursionlimit, stdin, maxsize
setrecursionlimit(10**6)


def dfs(v, p, parent):
    parent[v][0] = p
    for level in range(1, 20):  # Достаточно для n <= 10^5
        if parent[v][level - 1] != -1:
            parent[v][level] = parent[parent[v][level - 1]][level - 1]
        else:
            break

    for u in tree[v]:
        if u != p:
            dfs(u, v, parent)


def kth_ancestor(v, k, parent):
    for i in range(19, -1, -1):
        if (1 << i) <= k:
            v = parent[v][i]
            k -= (1 << i)
            if v == -1:
                return 1
    return v if v != -1 else 1


n = int(input().strip())
tree = [[] for _ in range(n + 1)]
parent = [[-1] * 20 for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().strip().split())
    tree[x].append(y)
    tree[y].append(x)

dfs(1, -1, parent)  # Запускаем DFS из корня

m = int(input().strip())
answers = []

for _ in range(m):
    v, k = map(int, input().strip().split())
    try:
        ans = kth_ancestor(v, k, parent)
        answers.append(str(ans))
    except Exception as e:
        answers.append("ERROR")

print("\n".join(answers))
