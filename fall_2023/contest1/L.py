def find_x(C):
    epsilon = 1e-6
    left = 0
    right = C

    while abs(right - left) >= epsilon:
        mid = (left + right) / 2
        square = mid * mid
        sqrt = mid ** 0.5

        if square + sqrt < C:
            left = mid
        else:
            right = mid

    return left


C = float(input())

x = find_x(C)

print('{:.6f}'.format(x))
