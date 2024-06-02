from collections import deque

def is_valid(x, y, n):
    """Проверка, что координаты (x, y) находятся в пределах доски размером n x n."""
    return 0 <= x < n and 0 <= y < n

def min_knight_moves(n, start1, start2, end1, end2):
    """Находит минимальное количество ходов для обмена местами двух коней на доске размером n x n."""
    # Варианты ходов коня
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    # Очередь для BFS
    queue = deque([(start1[0], start1[1], start2[0], start2[1], 0)])
    
    # Множество посещённых состояний
    visited = set()
    visited.add((start1[0], start1[1], start2[0], start2[1]))
    
    while queue:
        x1, y1, x2, y2, d = queue.popleft()
        
        # Если оба коня достигли своих конечных позиций
        if (x1, y1) == end1 and (x2, y2) == end2:
            return d
        
        for move1 in moves:
            new_x1, new_y1 = x1 + move1[0], y1 + move1[1]
            if is_valid(new_x1, new_y1, n):
                for move2 in moves:
                    new_x2, new_y2 = x2 + move2[0], y2 + move2[1]
                    if is_valid(new_x2, new_y2, n) and (new_x1, new_y1) != (new_x2, new_y2):
                        new_state = (new_x1, new_y1, new_x2, new_y2)
                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append((new_x1, new_y1, new_x2, new_y2, d + 1))
    
    return -1  # В случае невозможности достичь цели

n = 30
start1 = (0, 0)
end1 = (29, 29)
start2 = (29, 29)
end2 = (0, 0)

# Минимальные шаги для обмена местами коней
min_steps = min_knight_moves(n, start1, start2, end1, end2)

print(f"Минимальное количество ходов для обмена местами коней: {min_steps}")
