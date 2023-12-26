N, K = map(int, input().split())
coins = [0] + list(map(int, input().split())) + [0] 
dp = [float('-inf')] * N
dp[0] = 0 

from_stick = [0] * N

for i in range(1, N):
    for j in range(1, min(K, i) + 1):
        if dp[i - j] + coins[i] > dp[i]:
            dp[i] = dp[i - j] + coins[i]
            from_stick[i] = i - j

stick = N - 1
path = [N]
while stick > 0:
    stick = from_stick[stick]
    path.append(stick + 1)

print(dp[N - 1])
print(len(path) - 1)
print(" ".join(map(str, path[::-1])))