n, k = map(int, input().split())
numbers = list(map(int, input().split()))

x = numbers[0]
y = numbers[-1]

for _ in range(k):
    if x < y:
        sum_val = (x + y) % (2**30)
        numbers.append(sum_val)
        numbers.pop(0)
        x = numbers[0]
        y = numbers[-1]
    else:
        diff_val = (y - x) % (2**30)
        numbers.insert(0, diff_val)
        numbers.pop()
        x = numbers[0]
        y = numbers[-1]

print(*numbers)
