from collections import defaultdict
def restore_original_pairs(n, A, B, mixed_pairs):
    index_map_A = defaultdict(list)
    index_map_B = defaultdict(list)
    
    # Store indices of each number in A and B
    for idx, val in enumerate(A):
        index_map_A[val].append(idx)
    for idx, val in enumerate(B):
        index_map_B[val].append(idx)
    
    original_pairs = [None] * n
    used_indices_A = [False] * n
    used_indices_B = [False] * n

    for s, t in mixed_pairs:
        index_s, index_t = None, None
        
        # Find the next available index for s in A
        while index_map_A[s] and used_indices_A[index_map_A[s][-1]]:
            index_map_A[s].pop()
        if index_map_A[s]:
            index_s = index_map_A[s].pop()
        
        # Find the next available index for t in B
        while index_map_B[t] and used_indices_B[index_map_B[t][-1]]:
            index_map_B[t].pop()
        if index_map_B[t]:
            index_t = index_map_B[t].pop()
        
        # If we found indices for s in A and t in B, set the pair and mark the indices as used
        if index_s is not None and index_t is not None:
            original_pairs[index_s] = (s, t)
            used_indices_A[index_s] = True
            used_indices_B[index_t] = True
        else:
            # If a valid pair can't be formed, return "NO"
            return "NO"
    
    # If all pairs were formed, return "YES" and the pairs
    if all(pair is not None for pair in original_pairs):
        return ["YES"] + [" ".join(map(str, pair)) for pair in original_pairs]
    else:
        return "NO"



# Read input
n = int(input().strip())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))
mixed_pairs = [tuple(map(int, input().strip().split())) for _ in range(n)]

# Attempt to restore original pairs
result = restore_original_pairs(n, A, B, mixed_pairs)

# Output the result
if isinstance(result, list):
    for line in result:
        print(line)
else:
    print(result)