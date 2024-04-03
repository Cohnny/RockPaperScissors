import random

choices = ["Rock", "Paper", "Scissors"]

winning_conditions = {
    "Rock": "Scissors",
    "Scissors": "Paper",
    "Paper": "Rock"
}


def main():
    while True:
        computer_choice = random_choice()

        print("")
        choice = input("Rock, Paper or Scissors?\n").capitalize()

        if choice not in choices:
            print("Invalid choice. Please choose: Rock, Paper or Scissors.")
            continue

        print("Computers choice: ", computer_choice)

        if choice == computer_choice:
            print("It's a tie!")
        elif winning_conditions[choice] == computer_choice:
            print("You won!")
            return
        else:
            print("You lost!")
            return


def random_choice():
    random_number = random.randint(0, 2)
    return choices[random_number]


if __name__ == "__main__":
    main()
