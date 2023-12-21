def length_of_lis(sequence):
    from bisect import bisect_left
    dp = []
    for x in sequence:
        i = bisect_left(dp, x) 
        if i == len(dp):
            dp.append(x) 
        else:
            dp[i] = x  
    return len(dp)  

n, a1, k, b, m = map(int, input().split())

sequence = [a1]
for i in range(1, n):
    sequence.append((k * sequence[-1] + b) % m)  
lis_length = length_of_lis(sequence)

print(lis_length)