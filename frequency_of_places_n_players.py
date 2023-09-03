import random

def roll_dice():
    return random.randint(1, 6)

def simulate_monopoly(num_players, num_turns):

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
    
    players = [0] * num_players  # Starting positions for all players are "Go"
    position_counts = [{space: 0 for space in board} for _ in range(num_players)]
    
    chance_cards = ["Go", "Just Visiting", "Illinois Ave", "St. Charles Place", "Electric Company", "Reading Railroad", "Just Visiting", "Boardwalk"]
    community_chest_cards = ["Go", "Just Visiting", "Just Visiting", "Boardwalk"]
    
    for turn in range(num_turns):
        for player in range(num_players):
            roll = roll_dice() + roll_dice()  # Rolling two dice and adding the result
            players[player] = (players[player] + roll) % len(board)
            current_space = board[players[player]]
            
            # Handle "Go to Jail" rule
            if current_space == "Go to Jail":
                players[player] = board.index("Just Visiting")
                current_space = board[players[player]]
            
            # Handle "Chance" space
            if current_space == "Chance":
                chance_card = random.choice(chance_cards)
                players[player] = board.index(chance_card)
                current_space = board[players[player]]
            
            # Handle "Community Chest" space
            if current_space == "Community Chest":
                community_chest_card = random.choice(community_chest_cards)
                players[player] = board.index(community_chest_card)
                current_space = board[players[player]]
            
            position_counts[player][current_space] += 1
    
    return position_counts

def most_visited_places(position_counts, num_places=5):
    merged_counts = {}
    for player_counts in position_counts:
        for space, count in player_counts.items():
            if space not in merged_counts:
                merged_counts[space] = 0
            merged_counts[space] += count
    
    sorted_places = sorted(merged_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_places[:num_places]

if __name__ == "__main__":
    num_players = 4
    num_turns = 100000
    position_counts = simulate_monopoly(num_players, num_turns)
    most_visited = most_visited_places(position_counts,11)
    print("Most visited places by all players after", num_turns, "turns:")
    for place, count in most_visited:
        print(place, "was visited", count, "times.")
