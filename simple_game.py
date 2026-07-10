import random

name = input("Enter your name: ")
print(f"\nWelcome {name} to Rock Paper Scissors Game!\n")

items = ["rock", "paper", "scissors"]

computer = random.choice(items)

user_score = 0
computer_score = 0

user = input("Enter your choice (paper, rock, scissors): ").lower()

if user not in items:
    print("❌ Invalid choice! Please choose rock, paper, or scissors.")
    exit()

print("Computer chooses :", computer)
if user == computer:
    print("It's a tie!")

elif (
    (user == "rock" and computer == "scissors") or
    (user == "paper" and computer == "rock") or
    (user == "scissors" and computer == "paper")
):
    print("You win!")
    user_score += 1
else:
    print("Computer wins!!!")
    computer_score += 1
    print(f"\nScore -> You: {user_score} | Computer: {computer_score}")