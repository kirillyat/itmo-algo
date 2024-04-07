from collections import defaultdict
INF = 2e9+5

def roadblock(N, M, a, b, c):
    D = [INF] * N
    P = [(-1, -1)] * N
    for i in range(M):
        a[i] -= 1
        b[i] -= 1
    D[0] = 0

    for i in range(N):  # Bellman-Ford
        for j in range(M):
            newD = D[a[j]] + c[j]
            if newD < D[b[j]]:
                D[b[j]] = newD
                P[b[j]] = (a[j], j)
            newD2 = D[b[j]] + c[j]
            if newD2 < D[a[j]]:
                D[a[j]] = newD2
                P[a[j]] = (b[j], j)
                
    bst = D[N-1]
    ind = []
    i = N-1
    while P[i][1] != -1:
        ind.append(P[i][1])
        i = P[i][0]

    delta = 0
    for i in ind:
        c[i] *= 2  # Double the weight
        D = [INF] * N
        D[0] = 0
        for j in range(N):
            for k in range(M):
                newD = D[a[k]] + c[k]
                if newD < D[b[k]]:
                    D[b[k]] = newD
                newD2 = D[b[k]] + c[k]
                if newD2 < D[a[k]]:
                    D[a[k]] = newD2

        delta = max(delta, D[N-1] - bst)
        c[i] //= 2  # Restore the weight
        
    return delta

def main():
    N, M = map(int, input().split())
    a, b, c = [], [], []
    for _ in range(M):
        ai, bi, ci = map(int, input().split())
        a.append(ai)
        b.append(bi)
        c.append(ci)

    print(roadblock(N, M, a, b, c))

if __name__ == "__main__":
    main()
