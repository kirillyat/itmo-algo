def build_segment_tree(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build_segment_tree(arr, tree, 2 * node + 1, start, mid)
        build_segment_tree(arr, tree, 2 * node + 2, mid + 1, end)
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2]

def update_segment_tree(tree, node, start, end, idx, val):
    if start == end:
        tree[node] = val
    else:
        mid = (start + end) // 2
        if start <= idx <= mid:
            update_segment_tree(tree, 2 * node + 1, start, mid, idx, val)
        else:
            update_segment_tree(tree, 2 * node + 2, mid + 1, end, idx, val)
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2]

def query_segment_tree(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[node]
    mid = (start + end) // 2
    return query_segment_tree(tree, 2 * node + 1, start, mid, left, right) + \
           query_segment_tree(tree, 2 * node + 2, mid + 1, end, left, right)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
tree = [0] * (4 * n)
build_segment_tree(arr, tree, 0, 0, n-1)

for _ in range(m):
    operation = list(map(int, input().split()))
    if operation[0] == 1:
        update_segment_tree(tree, 0, 0, n-1, operation[1], operation[2])
    elif operation[0] == 2:
        print(query_segment_tree(tree, 0, 0, n-1, operation[1], operation[2]-1))