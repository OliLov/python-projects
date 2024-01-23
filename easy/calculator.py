"""Calculator."""


def display_calculator(input_str: str) -> None:
    """Display calculator.

    :param input: Input to display on calculator.
    """
    if len(input_str) > 15:
        input_str = input_str[:12] + "..."
    input_str = input_str[:15]
    input_padding = 15 - len(input_str)
    input_str = input_str + " " * input_padding

    calculator = f"""
         _____________________
        |  _________________  |
        | | {  input_str  } | |
        | |_________________| |
        |  ___ ___ ___   ___  |
        | | 7 | 8 | 9 | | + | |
        | |___|___|___| |___| |
        | | 4 | 5 | 6 | | - | |
        | |___|___|___| |___| |
        | | 1 | 2 | 3 | | x | |
        | |___|___|___| |___| |
        | | . | 0 | = | | / | |
        | |___|___|___| |___| |
        |_____________________|
    """
    print(calculator)


while True:
    user_input = input("Enter an equation (or 'q' to quit): ")

    if user_input == "q":
        break

    try:
        evaluation = eval(user_input)  # pylint: disable=eval-used
        display_calculator(user_input + " = " + str(evaluation))
    except Exception as e:  # pylint: disable=broad-exception-caught
        print("Error:", e)
