class SegmentTree:
    class Node:
        def __init__(self, s, l):
            self.sum = s
            self.add = 0
            self.set = None
            self.len = l

    def __init__(self, size):
        self.size = 1
        while self.size < size:
            self.size *= 2
        self.segment_tree = [self.Node(0, 1) for _ in range(2 * self.size - 1)]
        self._build(0, self.size, 0)

    def set(self, l, r, x):
        self._set(l, r, x, 0, self.size, 0)

    def sum(self, l, r):
        return self._sum(l, r, 0, self.size, 0)

    def add(self, l, r, x):
        self._add(l, r, x, 0, self.size, 0)

    def _build(self, lx, rx, v):
        if rx - lx == 1:
            self.segment_tree[v] = self.Node(0, 1)
        else:
            m = (lx + rx) // 2
            self._build(lx, m, 2 * v + 1)
            self._build(m, rx, 2 * v + 2)
            self.segment_tree[v] = self.Node(0, rx - lx)

    def _push(self, v):
        if self.segment_tree[v].set is not None:
            self.segment_tree[2 * v + 1].set = self.segment_tree[v].set
            self.segment_tree[2 * v + 2].set = self.segment_tree[v].set
            self.segment_tree[2 * v + 1].add = 0
            self.segment_tree[2 * v + 2].add = 0
            self.segment_tree[v].sum = self.segment_tree[v].set * self.segment_tree[v].len
            self.segment_tree[2 * v + 1].sum = self.segment_tree[v].set * self.segment_tree[2 * v + 1].len
            self.segment_tree[2 * v + 2].sum = self.segment_tree[v].set * self.segment_tree[2 * v + 2].len
            self.segment_tree[v].set = None
        if self.segment_tree[v].add != 0:
            self.segment_tree[v].sum += self.segment_tree[v].add * self.segment_tree[v].len
            self.segment_tree[2 * v + 1].add += self.segment_tree[v].add
            self.segment_tree[2 * v + 2].add += self.segment_tree[v].add
            self.segment_tree[v].add = 0

    def _add(self, l, r, x, lx, rx, v):
        if r <= lx or rx <= l:
            return
        if l <= lx and rx <= r:
            if rx - lx != 1:
                self._push(v)
            self.segment_tree[v].add += x
            return
        self._push(v)
        m = (lx + rx) // 2
        self._add(l, r, x, lx, m, 2 * v + 1)
        self._add(l, r, x, m, rx, 2 * v + 2)
        self.segment_tree[v].sum = (
            self.segment_tree[2 * v + 1].sum + self.segment_tree[2 * v + 2].sum +
            self.segment_tree[2 * v + 1].add * self.segment_tree[2 * v + 1].len +
            self.segment_tree[2 * v + 2].add * self.segment_tree[2 * v + 2].len
        )
        self.segment_tree[v].add = 0

    def _sum(self, l, r, lx, rx, v):
        if r <= lx or rx <= l:
            return 0
        if l <= lx and rx <= r:
            if rx - lx != 1:
                self._push(v)
            return self.segment_tree[v].sum + self.segment_tree[v].add * self.segment_tree[v].len
        self._push(v)
        m = (lx + rx) // 2
        return self._sum(l, r, lx, m, 2 * v + 1) + self._sum(l, r, m, rx, 2 * v + 2)

    def _set(self, l, r, x, lx, rx, v):
        if r <= lx or rx <= l:
            return
        if l <= lx and rx <= r:
            self.segment_tree[v].set = x
            self.segment_tree[v].sum = self.segment_tree[v].len * x
            self.segment_tree[v].add = 0
            return
        self._push(v)
        m = (lx + rx) // 2
        self._set(l, r, x, lx, m, 2 * v + 1)
        self._set(l, r, x, m, rx, 2 * v + 2)
        self.segment_tree[v].sum = (
            self.segment_tree[2 * v + 1].sum + self.segment_tree[2 * v + 2].sum +
            self.segment_tree[2 * v + 1].add * self.segment_tree[2 * v + 1].len +
            self.segment_tree[2 * v + 2].add * self.segment_tree[2 * v + 2].len
        )
        self.segment_tree[v].add = 0


def main():
    n, m = map(int, input().split())
    st = SegmentTree(n)
    answer = []

    for _ in range(m):
        command = input().split()
        if command[0] == '1':
            l = int(command[1])
            r = int(command[2])
            x = int(command[3])
            st.set(l, r, x)
        elif command[0] == '2':
            l = int(command[1])
            r = int(command[2])
            x = int(command[3])
            st.add(l, r, x)
        else:
            l = int(command[1])
            r = int(command[2])
            answer.append(st.sum(l, r))

    for ans in answer:
        print(ans)


if __name__ == '__main__':
    main()
