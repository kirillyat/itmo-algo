import heapq

n = int(input())
a = list(map(int, input().split()))
min_heap = a.copy()
heapq.heapify(min_heap)
max_heap = [-x for x in a]
heapq.heapify(max_heap)

min_candies = 0
while max_heap and min_heap and max_heap[0] - min_heap[0] > 1:
  min_candies += max_heap[0] - min_heap[0] - 1
  heapq.heappop(max_heap)
  heapq.heappop(min_heap)

print(min_candies)
