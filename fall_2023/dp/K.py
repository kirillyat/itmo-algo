def longest_increasing_subsequence(seq):
    n = len(seq)
    lengths = [1] * n  
    predecessors = [-1] * n 
    
    for i in range(1, n):
        for j in range(0, i):
            if seq[j] < seq[i] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                predecessors[i] = j
    
    max_length = max(lengths)
    lis_index = lengths.index(max_length)
    
    lis = []
    while lis_index != -1:
        lis.append(seq[lis_index])
        lis_index = predecessors[lis_index]
    lis.reverse()

    return max_length, lis

n = int(input())
seq = list(map(int, input().split()))

length, lis = longest_increasing_subsequence(seq)

print(length)
print(' '.join(map(str, lis)))