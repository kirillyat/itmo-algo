def remove_digits(num: int, k: int) -> int:
    num_str = str(num)
    n = len(num_str)
    stack = []
    removed = 0

    for i in range(n):
        while stack and removed < k and stack[-1] < num_str[i]:
            stack.pop()
            removed += 1

        if removed == k:
            stack += num_str[i:]
            break

        stack.append(num_str[i])

    stack = stack[:-k] if removed < k else stack
    result = int(''.join(stack))
    return result




num = 987654321
k = 4
result = remove_digits(num, k)
print(result)

