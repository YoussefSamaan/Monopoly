import random

def roll_dice():
    return random.randint(1, 6)

def simulate_monopoly(num_turns):
    board = [
        "Go", "Mediterranean Ave", "Community Chest", "Baltic Ave", "Income Tax",
        "Reading Railroad", "Oriental Ave", "Chance", "Vermont Ave", "Connecticut Ave",
        "Just Visiting", "St. Charles Place", "Electric Company", "States Ave", "Virginia Ave",
        "Pennsylvania Railroad", "St. James Place", "Community Chest", "Tennessee Ave", "New York Ave",
        "Free Parking", "Kentucky Ave", "Chance", "Indiana Ave", "Illinois Ave",
        "B. & O. Railroad", "Atlantic Ave", "Ventnor Ave", "Water Works", "Marvin Gardens",
        "Go to Jail", "Pacific Ave", "North Carolina Ave", "Community Chest", "Pennsylvania Ave",
        "Short Line", "Chance", "Park Place", "Luxury Tax", "Boardwalk"
    ]
    
    position_counts = {space: 0 for space in board}
    current_position = 0  # Starting position is "Go"
    
    for turn in range(num_turns):
        roll = roll_dice() + roll_dice()  # Rolling two dice and adding the result
        current_position = (current_position + roll) % len(board)
        position_counts[board[current_position]] += 1
    
    return position_counts

def most_visited_places(position_counts, num_places=5):
    sorted_places = sorted(position_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_places[:num_places]

if __name__ == "__main__":
    num_turns = 100000
    position_counts = simulate_monopoly(num_turns)
    most_visited = most_visited_places(position_counts)
    print("Most visited places after", num_turns, "turns:")
    for place, count in most_visited:
        print(place, "was visited", count, "times.")
