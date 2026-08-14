import random
from datetime import datetime


# =========================================================
# ROCK PAPER SCISSORS
# Professional Python Mini Project - Version 2
# =========================================================

CHOICES = ["rock", "paper", "scissors"]

WINNING_MOVES = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}


def get_player_name():
    """Get a valid player name."""

    while True:
        name = input("Enter your name: ").strip()

        if name:
            return name

        print("❌ Name cannot be empty. Please try again.")


def get_rounds():
    """Allow the player to select 3 or 5 rounds."""

    while True:
        try:
            rounds = int(
                input("\nHow many rounds? (3 or 5): ")
            )

            if rounds in (3, 5):
                return rounds

            print("⚠️ Please enter only 3 or 5.")

        except ValueError:
            print("❌ Please enter a valid number.")


def get_player_choice():
    """Get and validate player's choice."""

    while True:

        print("\nChoose your move:")
        print("1. 🪨 Rock")
        print("2. 📄 Paper")
        print("3. ✂️ Scissors")

        choice = input(
            "Enter 1, 2 or 3: "
        ).strip().lower()

        choices = {
            "1": "rock",
            "2": "paper",
            "3": "scissors",
            "rock": "rock",
            "paper": "paper",
            "scissors": "scissors"
        }

        if choice in choices:
            return choices[choice]

        print("❌ Invalid choice. Please try again.")


def determine_winner(player, computer):
    """Determine the winner of a round."""

    if player == computer:
        return "Tie"

    if WINNING_MOVES[player] == computer:
        return "Player"

    return "Computer"


def display_score(player_score, computer_score, ties):
    """Display current scoreboard."""

    print("\n" + "-" * 50)
    print("📊 CURRENT SCORE")
    print("-" * 50)
    print(f"👤 You       : {player_score}")
    print(f"🤖 Computer   : {computer_score}")
    print(f"🤝 Ties       : {ties}")
    print("-" * 50)


def play_round(round_number):
    """Play one round and return its result."""

    print(f"\n========== ROUND {round_number} ==========")

    player = get_player_choice()
    computer = random.choice(CHOICES)

    print(f"\n👤 Your Choice     : {player.title()}")
    print(f"🤖 Computer Choice : {computer.title()}")

    result = determine_winner(player, computer)

    if result == "Player":
        print("🎉 You Win This Round!")

    elif result == "Computer":
        print("🤖 Computer Wins This Round!")

    else:
        print("🤝 It's a Tie!")

    return player, computer, result


def display_round_history(history):
    """Display complete round history."""

    print("\n" + "=" * 65)
    print("📜 ROUND HISTORY")
    print("=" * 65)

    for record in history:
        print(
            f"Round {record['round']}: "
            f"You = {record['player'].title()} | "
            f"Computer = {record['computer'].title()} | "
            f"Result = {record['result']}"
        )

    print("=" * 65)


def display_final_result(
    name,
    rounds,
    player_score,
    computer_score,
    ties,
    history
):
    """Display final match result."""

    print("\n" + "=" * 60)
    print("🏆 FINAL MATCH RESULT")
    print("=" * 60)

    print(f"👤 Player          : {name}")
    print(f"🎯 Total Rounds    : {rounds}")
    print(f"🥇 Your Score      : {player_score}")
    print(f"🤖 Computer Score  : {computer_score}")
    print(f"🤝 Total Ties      : {ties}")

    if player_score > computer_score:
        print(f"\n🎉 Congratulations {name}!")
        print("🏆 YOU WON THE MATCH!")

    elif computer_score > player_score:
        print("\n🤖 COMPUTER WON THE MATCH!")

    else:
        print("\n🤝 THE MATCH IS A DRAW!")

    display_round_history(history)


def play_match(name):
    """Run a complete match."""

    rounds = get_rounds()

    player_score = 0
    computer_score = 0
    ties = 0

    history = []

    for round_number in range(1, rounds + 1):

        player, computer, result = play_round(
            round_number
        )

        if result == "Player":
            player_score += 1

        elif result == "Computer":
            computer_score += 1

        else:
            ties += 1

        history.append({
            "round": round_number,
            "player": player,
            "computer": computer,
            "result": result
        })

        display_score(
            player_score,
            computer_score,
            ties
        )

    display_final_result(
        name,
        rounds,
        player_score,
        computer_score,
        ties,
        history
    )


def main():
    """Main program."""

    print("\n" + "=" * 60)
    print("        🎮 ROCK PAPER SCISSORS GAME")
    print("        🐍 Professional Python Mini Project")
    print("=" * 60)

    name = get_player_name()

    print(f"\n👋 Welcome, {name}!")
    print("Let's start the game! 🚀")

    while True:

        play_match(name)

        print("\n" + "-" * 60)
        print("Would you like to play again?")
        print("1. 🔄 Play Again")
        print("2. 🚪 Exit")

        choice = input(
            "Enter your choice (1/2): "
        ).strip()

        if choice == "1":
            print("\n🔄 Starting a new match...")

        elif choice == "2":
            print(
                f"\n👋 Thank you for playing, {name}!"
            )
            print("🎮 See you next time!")
            break

        else:
            print(
                "⚠️ Invalid choice. "
                "Exiting the game."
            )
            break


# =========================================================
# PROGRAM START
# =========================================================

if __name__ == "__main__":
    main()