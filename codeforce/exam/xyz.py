import math

def find_min_angle_to_destroy_house(d, h, w, k):
    if h >= w and 2 * d <= k:
        return 0.0  # Прямой путь возможен горизонтально

    if 2 * d > k:
        return -1  # Дальность пучка недостаточна даже для достижения дома

    # Вычислим угол α, при котором пучок достигает дома
    angle_to_reach_house = math.atan(h / (2 * d))

    # Проверим, не попадает ли пучок на щит при таком угле
    if d / math.cos(angle_to_reach_house) <= k and w / math.tan(angle_to_reach_house) > 2 * d:
        return math.degrees(angle_to_reach_house)

    # В случае неудачи, вернем -1
    return -1

# Чтение входных данных
d, h, w, k = map(int, input().strip().split())

# Вычисление и вывод результата
result = find_min_angle_to_destroy_house(d, h, w, k)
if result == -1:
    print(result)
else:
    print(f"{result:.4f}")