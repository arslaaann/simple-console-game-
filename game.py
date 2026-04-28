import random

# ──────────────────────────────────────────
# STONE - PAPER - SCISSORS LOGIC
# ──────────────────────────────────────────

CHOICES = ["Stone", "Paper", "Scissors"]
BEATS = {
    "Stone": "Scissors",
    "Paper": "Stone",
    "Scissors": "Paper"
}

def get_computer_choice():
    return random.choice(CHOICES)

def determine_sps_winner(player, computer):
    if player == computer:
        return "Draw"
    elif BEATS[player] == computer:
        return "Player"
    else:
        return "Computer"

def get_player_sps_choice():
    print("\n  [1] Stone")
    print("  [2] Paper")
    print("  [3] Scissors")
    while True:
        choice = input("  Your choice (1/2/3): ").strip()
        if choice == "1":
            return "Stone"
        elif choice == "2":
            return "Paper"
        elif choice == "3":
            return "Scissors"
        else:
            print("  Invalid input. Please enter 1, 2, or 3.")

def play_stone_paper_scissors():
    print("\n" + "=" * 45)
    print("       STONE - PAPER - SCISSORS")
    print("=" * 45)

    scores = {"Player": 0, "Computer": 0, "Draw": 0}

    while True:
        print(f"\n  Score --> You: {scores['Player']}  |  CPU: {scores['Computer']}  |  Draws: {scores['Draw']}")

        player = get_player_sps_choice()
        computer = get_computer_choice()

        print(f"\n  You chose   : {player}")
        print(f"  CPU chose   : {computer}")

        result = determine_sps_winner(player, computer)
        scores[result] += 1

        if result == "Player":
            print("  Result      : You WIN this round!")
        elif result == "Computer":
            print("  Result      : CPU WINS this round!")
        else:
            print("  Result      : It's a DRAW!")

        again = input("\n  Play another round? (y/n): ").strip().lower()
        if again != "y":
            break

    print("\n" + "-" * 45)
    print("  FINAL SCORE")
    print(f"  You: {scores['Player']}  |  CPU: {scores['Computer']}  |  Draws: {scores['Draw']}")
    if scores["Player"] > scores["Computer"]:
        print("  Overall Winner : YOU! Congratulations!")
    elif scores["Computer"] > scores["Player"]:
        print("  Overall Winner : CPU! Better luck next time.")
    else:
        print("  Overall Result : It's a TIE!")
    print("-" * 45)


# ──────────────────────────────────────────
# DICE ROLL LOGIC
# ──────────────────────────────────────────

def roll_dice():
    return random.randint(1, 6)

def determine_dice_winner(player_roll, computer_roll):
    if player_roll > computer_roll:
        return "Player"
    elif computer_roll > player_roll:
        return "Computer"
    else:
        return "Draw"

def play_dice_roll():
    print("\n" + "=" * 45)
    print("           DICE ROLL GAME")
    print("   Highest number wins each round!")
    print("=" * 45)

    scores = {"Player": 0, "Computer": 0, "Draw": 0}

    while True:
        print(f"\n  Score --> You: {scores['Player']}  |  CPU: {scores['Computer']}  |  Draws: {scores['Draw']}")
        input("\n  Press ENTER to roll the dice...")

        player_roll = roll_dice()
        computer_roll = roll_dice()

        print(f"\n  You rolled  : {player_roll}")
        print(f"  CPU rolled  : {computer_roll}")

        result = determine_dice_winner(player_roll, computer_roll)
        scores[result] += 1

        if result == "Player":
            print("  Result      : You WIN this round!")
        elif result == "Computer":
            print("  Result      : CPU WINS this round!")
        else:
            print("  Result      : It's a DRAW!")

        again = input("\n  Roll again? (y/n): ").strip().lower()
        if again != "y":
            break

    print("\n" + "-" * 45)
    print("  FINAL SCORE")
    print(f"  You: {scores['Player']}  |  CPU: {scores['Computer']}  |  Draws: {scores['Draw']}")
    if scores["Player"] > scores["Computer"]:
        print("  Overall Winner : YOU! Congratulations!")
    elif scores["Computer"] > scores["Player"]:
        print("  Overall Winner : CPU! Better luck next time.")
    else:
        print("  Overall Result : It's a TIE!")
    print("-" * 45)


# ──────────────────────────────────────────
# MAIN MENU
# ──────────────────────────────────────────

def display_main_menu():
    print("\n" + "=" * 45)
    print("        PyGame Arcade - Mini Games")
    print("=" * 45)
    print("  [1]  Stone - Paper - Scissors")
    print("  [2]  Dice Roll Game")
    print("  [3]  Exit")
    print("  " + "-" * 40)

def main():
    print("\n  Welcome to PyGame Arcade!")

    while True:
        display_main_menu()
        choice = input("  Enter your choice (1/2/3): ").strip()

        if choice == "1":
            play_stone_paper_scissors()
        elif choice == "2":
            play_dice_roll()
        elif choice == "3":
            print("\n  Thanks for playing! See you next time.\n")
            break
        else:
            print("  Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
