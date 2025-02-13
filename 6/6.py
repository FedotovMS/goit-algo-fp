def greedy_algorithm(items, budget):
    # Сортуємо елементи за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    chosen_items = []
    
    for item, info in sorted_items:
        if budget >= info['cost']:
            chosen_items.append(item)
            total_calories += info['calories']
            budget -= info['cost']
    
    return chosen_items, total_calories


def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name, info = item_list[i - 1]
        cost, calories = info['cost'], info['calories']
        
        for b in range(budget + 1):
            if cost > b:
                dp[i][b] = dp[i - 1][b]
            else:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
    
    # Відновлення обраних страв
    chosen_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name, info = item_list[i - 1]
            chosen_items.append(name)
            b -= info['cost']
    
    return chosen_items, dp[n][budget]


# Дані про страви
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

print("Greedy Algorithm:", greedy_result)
print("Dynamic Programming:", dp_result)