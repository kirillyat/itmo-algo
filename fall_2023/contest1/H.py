class Heap:
    def __init__(self):
        self.heap = []

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, num):
        self.heap.append(num)
        idx = len(self.heap) - 1
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[parent] < self.heap[idx]:
                self.swap(parent, idx)
            else:
                break
            idx = parent

    def extract(self):
        extracted = self.heap[0]
        self.swap(0, len(self.heap) - 1)
        self.heap.pop()
        idx = 0
        while True:
            left = idx * 2 + 1
            right = idx * 2 + 2
            largest = idx
            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right
            if largest != idx:
                self.swap(largest, idx)
                idx = largest
            else:
                break
        return extracted

n = int(input())
commands = []
for _ in range(n):
    commands.append(input().split())

heap = Heap()

for command in commands:
    if command[0] == '0':
        heap.insert(int(command[1]))
    else:
        extracted = heap.extract()
        print(extracted)
