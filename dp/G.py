MOD = 10**6 + 7

def count_knight_routes(N, M):
    dp = [[0] * M for _ in range(N)]
    dp[0][0] = 1  

    moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]

    for i in range(N):
        for j in range(M):
            for move in moves:
                prev_i, prev_j = i + move[0], j + move[1]
                if 0 <= prev_i < N and 0 <= prev_j < M:
                    dp[i][j] += dp[prev_i][prev_j]
                    dp[i][j] %= MOD

    return dp[N-1][M-1]

N, M = map(int, input().split())

print(count_knight_routes(N, M))