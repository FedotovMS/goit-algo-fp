import heapq

# Алгоритм Дейкстри для знаходження найкоротших шляхів
def dijkstra(graph, start):
    # Встановлюємо початкові відстані для всіх вершин як нескінченність
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    # Створюємо бінарну купу, де кожен елемент - це пара (відстань, вершина)
    priority_queue = [(0, start)]  # Починаємо з початкової вершини
    heapq.heapify(priority_queue)
    
    while priority_queue:
        # Вибираємо вершину з мінімальним значенням відстані
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Якщо відстань для поточної вершини вже більша за знайдену (це вже оброблено)
        if current_distance > distances[current_vertex]:
            continue
        
        # Оновлюємо відстані для сусідніх вершин
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Якщо знайдена краща відстань до сусіда, оновлюємо відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Приклад графа
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Визначаємо початкову вершину
start = 'A'

# Викликаємо алгоритм Дейкстри
shortest_paths = dijkstra(graph, start)

# Виводимо результат
print(f"Найкоротші шляхи від вершини {start}:")
for vertex, distance in shortest_paths.items():
    print(f"{vertex}: {distance}")