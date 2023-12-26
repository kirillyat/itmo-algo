MOD = 10**6 + 7

N, M = map(int, input().split())

dp = [[0 for _ in range(M)] for _ in range(N)]

dp[0][0] = 1

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < M

moves = [(-1, -2), (-2, -1), (-1, 2), (-2, 1)]

for i in range(N):
    for j in range(M):
        for move in moves:
            prev_x, prev_y = i + move[0], j + move[1]
            if is_valid(prev_x, prev_y):
                dp[i][j] += dp[prev_x][prev_y]
                dp[i][j] %= MOD

print(dp[N-1][M-1])