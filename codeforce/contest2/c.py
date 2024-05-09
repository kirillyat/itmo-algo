from collections import defaultdict

class SegmentTree:
    def __init__(self, n):
        self.tree = defaultdict(int)
        self.n = n

    def update(self, l, r, v):
        self._update(l, r, v, 1, self.n)

    def _update(self, l, r, v, cl, cr):
        """
        Update the segment tree with a new value.

        Parameters:
            l (int): The starting index of the range.
            r (int): The ending index of the range.
            v (int): The new value to update.
            cl (int): The starting index of the current subtree.
            cr (int): The ending index of the current subtree.
        """
        # Check if the range is within the current subtree
        if l <= cl and r >= cr:
            # Update the values at the leaf nodes
            self.tree[cl] = v
            self.tree[cr + 1] = v
            return

        # Find the midpoint of the current subtree
        m = (cl + cr) // 2

        # Recursively update the left and right subtrees
        if l <= m:
            self._update(l, r, v, cl, m)
        if r > m:
            self._update(l, r, v, m + 1, cr)

    def add(self, l, r, v):
        self._add(l, r, v, 1, self.n)

    def _add(self, l, r, v, cl, cr):
        """
        Add the value `v` to the range [l, r] in the segment tree.

        Parameters:
            l (int): The starting index of the range.
            r (int): The ending index of the range.
            v (int): The value to add.
            cl (int): The starting index of the current subtree.
            cr (int): The ending index of the current subtree.
        """
        # Check if the range is within the current subtree
        if l <= cl and r >= cr:
            # If the range is within the current subtree, add the value to the
            # leaf nodes
            self.tree[cl] += v
            self.tree[cr + 1] += v
            return

        # Find the midpoint of the current subtree
        m = (cl + cr) // 2

        # Recursively add the value to the left and right subtrees
        if l <= m:
            self._add(l, r, v, cl, m)
        if r > m:
            self._add(l, r, v, m + 1, cr)

    def get(self, l, r):
        return self._get(l, r, 1, self.n)

    def _get(self, l, r, cl, cr):
        """
        Get the sum of values in the range [l, r] in the segment tree.

        Parameters:
            l (int): The starting index of the range.
            r (int): The ending index of the range.
            cl (int): The starting index of the current subtree.
            cr (int): The ending index of the current subtree.

        Returns:
            int: The sum of values in the range.
        """
        # Check if the range is within the current subtree
        if l <= cl and r >= cr:
            # If the range is within the current subtree, return the value at
            # the leaf node
            return self.tree[cl]

        # Find the midpoint of the current subtree
        m = (cl + cr) // 2

        # Recursively get the sum of values in the left and right subtrees
        sum = 0
        if l <= m:
            sum += self._get(l, r, cl, m)
        if r > m:
            sum += self._get(l, r, m + 1, cr)
        return sum



if __name__ == "__main__":
    n, m = map(int, input().split())
    st = SegmentTree(n)
    for _ in range(m):
        op, l, r, *v = map(int, input().split())
        if op == 1:
            st.update(l, r, v[0])
        elif op == 2:
            st.add(l, r, v[0])
        elif op == 3:
            print(st.get(l, r))