def select_jewels(n, k, jewels):
    # Создаем список драгоценностей с информацией о ценности, весе и их отношении v[i]/w[i]
    jewels_info = [(jewels[i][0], jewels[i][1], jewels[i][0] / jewels[i][1]) for i in range(n)]

    # Сортируем список драгоценностей по убыванию отношения v[i]/w[i]
    sorted_jewels = sorted(jewels_info, key=lambda x: x[2], reverse=True)

    # Выбираем первые k драгоценностей отсортированного списка
    selected_jewels = [sorted_jewels[i][0] for i in range(k)]

    return selected_jewels

# Считываем входные данные
n, k = map(int, input().split())

jewels = []
for _ in range(n):
    v, w = map(int, input().split())
    jewels.append((v, w))

# Вызываем функцию выбора драгоценностей
selected = select_jewels(n, k, jewels)

# Вывод результатов
print(*selected)
