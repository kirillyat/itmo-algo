class MinQueue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, x):
        min_val = x if not self.enqueue_stack else min(x, self.enqueue_stack[-1][1])
        self.enqueue_stack.append((x, min_val))

    def dequeue(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                val = self.enqueue_stack.pop()[0]
                min_val = val if not self.dequeue_stack else min(val, self.dequeue_stack[-1][1])
                self.dequeue_stack.append((val, min_val))
        return self.dequeue_stack.pop()[0]

    def get_min(self):
        min_vals = []
        if self.enqueue_stack:
            min_vals.append(self.enqueue_stack[-1][1])
        if self.dequeue_stack:
            min_vals.append(self.dequeue_stack[-1][1])
        return min(min_vals) if min_vals else -1  # Если оба стека пусты, возвращаем -1

q = int(input())

queue = MinQueue()

for _ in range(q):
    query = input().split()
    if query[0] == '+':
        queue.enqueue(int(query[1]))
        print(queue.get_min())
    else:
        queue.dequeue()
        print(queue.get_min())
