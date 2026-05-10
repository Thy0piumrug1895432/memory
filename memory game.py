memory game
import random
import time
import os

colors = ["red", "blue", "green", "yellow"]

# Optional shortcuts
color_map = {
    "r": "red",
    "b": "blue",
    "g": "green",
    "y": "yellow"
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_sequence(sequence):
    for item in sequence:
        print(item.upper())
        time.sleep(1)
        clear_screen()
        time.sleep(0.3)

def get_user_input(length):
    print(f"Enter the sequence (space-separated, {length} colors)")
    print("You can type full names or shortcuts: r b g y")
    user_input = input("> ").lower().strip().split()

    # Convert shortcuts to full color names
    converted = []
    for x in user_input:
        if x in color_map:
            converted.append(color_map[x])
        else:
            converted.append(x)  # assume full word like "red"
    
    return converted

def play_game():
    sequence = []
    round_num = 1

    print("Memory Game (Colors)! Repeat the sequence.")
    input("Press Enter to start...")

    while True:
        clear_screen()
        print(f"Round {round_num}")

        # Add a random color
        sequence.append(random.choice(colors))

        time.sleep(1)
        show_sequence(sequence)

        user_answer = get_user_input(len(sequence))

        if user_answer != sequence:
            print("Wrong sequence!")
            print("Correct was:", " ".join(sequence))
            print(f"You reached round {round_num}")
            break

        print("Correct!")
        round_num += 1
        time.sleep(1)

if __name__ == "__main__":
    play_game()