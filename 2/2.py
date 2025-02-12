import matplotlib.pyplot as plt
import numpy as np

def draw_tree(x, y, angle, length, level, ax):
    if level == 0:
        return
    
    # Обчислюємо координати кінця поточної гілки
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)
    
    # Малюємо лінію між початковою та кінцевою точкою (гілка дерева)
    ax.plot([x, x_end], [y, y_end], color="brown", lw=2)
    
    # Викликаємо рекурсивно для двох нових гілок
    new_length = length * np.sqrt(2) / 2  # Відстань для гілки наступного рівня
    new_angle_left = angle - np.pi / 4  # Лівий кут
    new_angle_right = angle + np.pi / 4  # Правий кут
    
    # Рекурсивно малюємо ліву та праву гілки
    draw_tree(x_end, y_end, new_angle_left, new_length, level - 1, ax)
    draw_tree(x_end, y_end, new_angle_right, new_length, level - 1, ax)

def create_pythagorean_tree(level):
    # Створюємо графік
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.set_axis_off()
    
    # Початкові параметри
    x, y = 0, 0  # Початкова точка (низ дерева)
    angle = np.pi / 2  # Початковий кут (вертикально вгору)
    length = 10  # Довжина першої гілки (основний стовбур дерева)
    
    # Малюємо дерево Піфагора
    draw_tree(x, y, angle, length, level, ax)
    
    # Виводимо графік
    plt.show()

# Запитуємо користувача про рівень рекурсії
level = int(input("Введіть рівень рекурсії для дерева Піфагора: "))
create_pythagorean_tree(level)