class Node:
    def __init__(self, key):
        self.key = key
        self.sum = key
        self.min = key
        self.max = key
        self.height = 1
        self.left = None
        self.right = None

    def get_height_left(self):
        return self.left.height if self.left else 0

    def get_height_right(self):
        return self.right.height if self.right else 0

    def get_balance(self):
        return self.get_height_right() - self.get_height_left()

    def get_sum_left(self):
        return self.left.sum if self.left else 0

    def get_sum_right(self):
        return self.right.sum if self.right else 0

    def get_min_left(self):
        return self.left.min if self.left else float('inf')

    def get_min_right(self):
        return self.right.min if self.right else float('inf')

    def get_max_left(self):
        return self.left.max if self.left else float('-inf')

    def get_max_right(self):
        return self.right.max if self.right else float('-inf')

    def recalc_min_max(self):
        self.min = min(self.get_min_left(), self.get_min_right(), self.key)
        self.max = max(self.get_max_left(), self.get_max_right(), self.key)

    def recalc_sum(self):
        self.sum = self.get_sum_left() + self.get_sum_right() + self.key

    def recalc(self):
        self.height = 1 + max(self.get_height_left(), self.get_height_right())
        self.recalc_min_max()
        self.recalc_sum()


def find(cur_node, val):
    if cur_node is None or cur_node.key == val:
        return cur_node
    if cur_node.key < val:
        return find(cur_node.right, val)
    return find(cur_node.left, val)


def exists(cur_node, val):
    return find(cur_node, val) is not None


def right_rotate(cur_node):
    left = cur_node.left
    cur_node.left = left.right
    left.right = cur_node

    cur_node.recalc()
    left.recalc()
    return left


def left_rotate(cur_node):
    right = cur_node.right
    cur_node.right = right.left
    right.left = cur_node

    cur_node.recalc()
    right.recalc()
    return right


def rebalance(cur_node):
    if cur_node.get_balance() == 2:
        if cur_node.right.get_balance() < 0:
            cur_node.right = right_rotate(cur_node.right)
        return left_rotate(cur_node)
    if cur_node.get_balance() == -2:
        if cur_node.left.get_balance() > 0:
            cur_node.left = left_rotate(cur_node.left)
        return right_rotate(cur_node)
    return cur_node


def insert(cur_node, new_key):
    if cur_node is None:
        return Node(new_key)
    if new_key < cur_node.key:
        cur_node.left = insert(cur_node.left, new_key)
    else:
        cur_node.right = insert(cur_node.right, new_key)

    cur_node.recalc()
    return rebalance(cur_node)


def insert_node(cur_node, new_key):
    if exists(cur_node, new_key):
        return cur_node
    return insert(cur_node, new_key)


def range_sum(cur_node, l, r):
    if cur_node is None:
        return 0
    if cur_node.key > r:
        return range_sum(cur_node.left, l, r)
    if cur_node.key < l:
        return range_sum(cur_node.right, l, r)
    if cur_node.left is None and cur_node.right is None:
        return cur_node.key
    if cur_node.min >= l and cur_node.max <= r:
        return cur_node.sum

    return range_sum(cur_node.left, l, r) + range_sum(cur_node.right, l, r) + cur_node.key


TEN = 1000000000


def main():
    root = None
    prev = '+'
    res = 0
    n = int(input().strip())

    for _ in range(n):
        c = input().strip().split()

        if c[0] == '+':
            x = int(c[1])

            if prev == '?':
                root = insert_node(root, (x + res) % TEN)
            else:
                root = insert_node(root, x)
        else:
            l = int(c[1])
            r = int(c[2])

            res = range_sum(root, l, r)
            print(res)

        prev = c

if __name__ == "__main__":
    main()