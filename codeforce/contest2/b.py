class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(data, 0, 0, self.n - 1)
        
    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = (data[start], start)
        else:
            mid = (start + end) // 2
            self.build(data, 2 * node + 1, start, mid)
            self.build(data, 2 * node + 2, mid + 1, end)
            self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2], key=lambda x: x[0])
    
    def update(self, idx, value, node, start, end):
        if start == end:
            # Leaf node
            self.tree[node] = (value, start)
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self.update(idx, value, 2 * node + 1, start, mid)
            else:
                self.update(idx, value, 2 * node + 2, mid + 1, end)
            self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2], key=lambda x: x[0])
    
    def query(self, x, l, node, start, end):
        if start > end:
            return -1
        if start >= l and self.tree[node][0] >= x:
            if start == end:
                return start
            mid = (start + end) // 2
            left_result = self.query(x, l, 2 * node + 1, start, mid)
            if left_result != -1:
                return left_result
            return self.query(x, l, 2 * node + 2, mid + 1, end)
        return -1

def main():
    try:
        import sys
        input = sys.stdin.readline
        
        n, m = map(int, input().split())
        array = list(map(int, input().split()))
        
        seg_tree = SegmentTree(array)

        results = []
        for _ in range(m):
            op, *args = map(int, input().split())
            if op == 1:
                idx, value = args
                seg_tree.update(idx, value, 0, 0, len(array) - 1)
            elif op == 2:
                x, l = args
                result = seg_tree.query(x, l, 0, 0, len(array) - 1)
                results.append(result)
        
        print('\n'.join(map(str, results)))
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
