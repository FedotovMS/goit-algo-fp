import random
import matplotlib.pyplot as plt

def monte_carlo_dice_simulation(num_rolls=100000):
    sum_counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        dice_sum = random.randint(1, 6) + random.randint(1, 6)
        sum_counts[dice_sum] += 1
    
    probabilities = {s: (count / num_rolls) * 100 for s, count in sum_counts.items()}
    return probabilities

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    plt.bar(sums, probs, color='blue', alpha=0.7)
    plt.xlabel("Сума")
    plt.ylabel("Ймовірність (%)")
    plt.title("Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)")
    plt.xticks(sums)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Запуск симуляції
num_rolls = 100000
probabilities = monte_carlo_dice_simulation(num_rolls)

# Вивід таблиці
print("Сума\tЙмовірність (%)")
for s in sorted(probabilities.keys()):
    print(f"{s}\t{probabilities[s]:.2f}%")

# Побудова графіка
plot_probabilities(probabilities)