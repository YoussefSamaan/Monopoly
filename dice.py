import random
import matplotlib.pyplot as plt

def roll_two_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def simulate_dice_rolls(num_rolls):
    results = []
    for _ in range(num_rolls):
        result = roll_two_dice()
        results.append(result)
    return results

def plot_dice_results(results):
    counts = [results.count(i) for i in range(2, 13)]
    numbers = list(range(2, 13))
    
    plt.bar(numbers, counts)
    plt.xlabel('Sum of Dice')
    plt.ylabel('Frequency')
    plt.title('Simulated Dice Rolls')
    
    for i, count in enumerate(counts):
        plt.text(numbers[i], count, str(count), ha='center', va='bottom')
    
    plt.show()

if __name__ == "__main__":
    num_rolls = 10000
    dice_results = simulate_dice_rolls(num_rolls)
    plot_dice_results(dice_results)
