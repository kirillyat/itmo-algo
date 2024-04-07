# =====================================================================================
def find_min_max(nums):
    """
    Дан массив из 2n чисел.
    Найти минимальное и максимальное за 3n - 2 сравнения.
    """
    n = len(nums) // 2
    min_num, max_num = nums[0], nums[1]

    if min_num > max_num:
        max_num, min_num = min_num, max_num

    for i in range(1, n):
        num1, num2 = nums[2 * i], nums[2 * i + 1]
        if num1 < num2:
            if num1 < min_num:
                min_num = num1
            if num2 > max_num:
                max_num = num2
        else:
            if num2 < min_num:
                min_num = num2
            if num1 > max_num:
                max_num = num1

    return min_num, max_num


assert find_min_max([100, -1, 2, 3]) == (-1, 100)
assert find_min_max([1, 1]) == (1, 1)

assert find_min_max([-1, -1]) == (-1, -1)
assert find_min_max([1, 2, 3, 4]) == (1, 4)
print("find_min_max - done")


# =====================================================================================
def secondmax(arr):
    """
    Найти второй максимум в массиве за n + O(log n) сравнений.
    """
    n = len(arr)
    if n == 0:
        return None, None
    if n == 1:
        return arr[0], None

    def compare_pairs(left, right):
        if left[0] > right[0]:
            return left, right
        else:
            return right, left

    history = [(arr[i], []) for i in range(n)]

    while len(history) > 1:
        next_level = []
        for i in range(0, len(history), 2):
            if i + 1 < len(history):
                winner, loser = compare_pairs(history[i], history[i + 1])
                winner[1].append(loser[0])
                next_level.append(winner)
            else:
                next_level.append(history[i])
        history = next_level

    max_element = history[0][0]
    fights = history[0][1]

    if not fights:
        return max_element, None

    second_max = fights[0]
    for f in fights[1:]:
        if f > second_max:
            second_max = f

    return max_element, second_max


arr1 = [3, 1, 9, 7, 5]
max_elem1, second_max1 = secondmax(arr1)
assert max_elem1 == 9 and second_max1 == 7

arr2 = [10, 20, 30, 40, 50]
max_elem2, second_max2 = secondmax(arr2)
assert max_elem2 == 50 and second_max2 == 40

arr3 = [9]
max_elem3, _ = secondmax(arr3)
assert max_elem3 == 9

arr4 = [5, 1]
max_elem4, second_max4 = secondmax(arr4)
assert max_elem4 == 5 and second_max4 == 1


print("secondmax - done")


# =====================================================================================
def count_ways(n):
    """
    Кузнечик умеет прыгать со ступеньки с номером i на ступеньки с номерами i+1 и 2i.
    Найдите количество способов добраться с нулевой ступеньки до n-й за O(n) времени.
    """
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        dp[i] += dp[i - 1]
        if i % 2 == 0:
            dp[i] += dp[i // 2]

    return dp[n]


assert count_ways(0) == 1
assert count_ways(1) == 1
assert count_ways(2) == 2
assert count_ways(3) == 2
assert count_ways(4) == 4
assert count_ways(5) == 4
assert count_ways(8) == 10
assert count_ways(10) == 14

print("count_ways - done")


# =====================================================================================
def count_ways(n):
    """
    Кузнечик умеет прыгать на две или три ступеньки вперед, либо на одну назад.
    Но при этом прыжок назад можно совершать не более одного раза подряд.
    Найдите количество способов добраться с нулевой ступеньки до n-й за O(n) времени.
    """
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2] + dp[i - 3]
    return dp[n]


assert count_ways(0) == 1
assert count_ways(1) == 1
assert count_ways(2) == 3
assert count_ways(3) == 6
assert count_ways(4) == 13
print("count_ways 2 - done")


# =====================================================================================
def min_cost_to_reach_nth_stair(cost):
    """
    Кузнечик умеет прыгать на одну или две ступеньки вперед, у каждой ступеньки есть стоимость попадания на нее.
    Найдите количество способов добраться с нулевой ступеньки до n-й, потратив как можно меньше денег, за O(n) времени.
    """
    n = len(cost)
    if n == 0:
        return 0
    if n == 1:
        return cost[0]

    dp = [0 for _ in range(n)]
    dp[0], dp[1] = cost[0], cost[1]

    for i in range(2, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
    return min(dp[n - 1], dp[n - 2])


assert min_cost_to_reach_nth_stair([10, 15, 20]) == 15
assert min_cost_to_reach_nth_stair([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6

print("min_cost_to_reach_nth_stair - done")
