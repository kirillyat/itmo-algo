import math

def adjust_size(arr):
    """Ensure the array length is a power of 2 by appending zeros if necessary."""
    current_length = len(arr)
    new_length = 2 ** math.ceil(math.log2(current_length))
    arr.extend([0] * (new_length - current_length))

class SegmentTree:
    def __init__(self, arr):
        """Initialize the segment tree based on the input array."""
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self._build(arr, 0, 0, self.n)

    def update(self, idx, value, node=0, left=0, right=None):
        """Update the element at index `idx` with `value`."""
        if right is None:
            right = self.n
        
        if (right - left) == 1:
            self.tree[node] = value
            return
        
        midpoint = (left + right) // 2
        if idx < midpoint:
            self.update(idx, value, 2 * node + 1, left, midpoint)
        else:
            self.update(idx, value, 2 * node + 2, midpoint, right)
        
        self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query_above(self, value, left, node=0, lx=0, rx=None):
        """Find the smallest index with a value at least `value`, starting at index `left`."""
        if rx is None:
            rx = self.n
        
        if self.tree[node] < value:
            return -1
        if rx <= left:
            return -1
        if (rx - lx) == 1:
            return lx
        
        midpoint = (lx + rx) // 2
        res = self.query_above(value, left, 2 * node + 1, lx, midpoint)
        if res == -1:
            res = self.query_above(value, left, 2 * node + 2, midpoint, rx)
        return res

    def _build(self, arr, node, left, right):
        """Recursively build the segment tree."""
        if (right - left) == 1:
            if left < len(arr):
                self.tree[node] = arr[left]
        else:
            midpoint = (left + right) // 2
            self._build(arr, 2 * node + 1, left, midpoint)
            self._build(arr, 2 * node + 2, midpoint, right)
            self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])

if __name__ == "__main__":
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    
    adjust_size(array)
    n = len(array)
    segment_tree = SegmentTree(array)
    
    result = []
    for _ in range(m):
        query = list(map(int, input().split()))
        if query[0] == 1:
            idx, value = query[1], query[2]
            segment_tree.update(idx, value)
        else:
            value, left = query[1], query[2]
            result.append(segment_tree.query_above(value, left))
    
    print('\n'.join(map(str, result)))