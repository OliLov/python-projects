"""Rock, paper, scissors."""
import random
import time

ICON = {
    1: [
        "    _______  ",
        "---'   ____) ",
        "      (_____)",
        "      (_____)",
        "      (____) ",
        "---.__(___)  ",
    ],
    2: [
        "    ________      ",
        "---'    ____)____ ",
        "           ______)",
        "          _______)",
        "         _______) ",
        "---.__________)   ",
    ],
    3: [
        "    _______        ",
        "---'   ____)____   ",
        "          ______)  ",
        "       __________) ",
        "      (____)       ",
        "---.__(___)        ",
    ],
}

CHOICES = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
    "r": 1,
    "p": 2,
    "s": 3,
    "1": 1,
    "2": 2,
    "3": 3,
}


def render_choice(choice: int, render_time: float = 0) -> None:
    """Render choice.

    :param choice: Integer representing the choice.
    :param render_time: Float representing the time to render the icon.
    """
    for line in ICON[choice]:
        print(line)
        time.sleep(render_time / len(ICON[choice]))


print("Welcome to Rock, Paper, Scissors!")

while True:
    computer_choice = random.randint(1, 3)
    user_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()

    if user_choice not in CHOICES:
        print("Invalid input.")
        continue

    user_choice = CHOICES[user_choice]

    print("You chose")
    render_choice(user_choice)

    print("\nComputer chose")
    render_choice(computer_choice, render_time=1)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (  # pylint: disable=too-many-boolean-expressions
        (user_choice == 1 and computer_choice == 3)
        or (user_choice == 2 and computer_choice == 1)
        or (user_choice == 3 and computer_choice == 2)
    ):
        print("You win!")
    else:
        print("Computer wins!\n")

    play_again = input("Play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        break
