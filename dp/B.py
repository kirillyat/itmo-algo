def find_max_coins(n, k, coins):

    max_coins = [0] * n
    jumps = [-1] * n
    
    max_coins[0] = 0
    
    for i in range(1, n):
        for j in range(1, min(i, k) + 1):
            if max_coins[i] < max_coins[i-j] + coins[i]:
                max_coins[i] = max_coins[i-j] + coins[i]
                jumps[i] = i-j
                
    path = []
    position = n-1
    while position != -1:
        path.append(position + 1)
        position = jumps[position]
    path.reverse()
    
    return max_coins[-1], len(path) - 1, path

N, K = map(int, input().split())
coin_values = [0] + list(map(int, input().split())) + [0]

max_coins, num_jumps, path = find_max_coins(N, K, coin_values)


print(max_coins)
print(num_jumps)
print(" ".join(map(str, path)))