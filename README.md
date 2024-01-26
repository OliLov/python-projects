# Python Projects

This project is a collection of Python projects.

## Projects

### python-projects/easy

- Calculator: Performs basic arithmetic operations like addition, subtraction, multiplication, and division. Displays the result in a calculator.
- Dice Rolling Simulator: Simulates the roll of a die.
- Guess the Number: A game where the user tries to guess a randomly generated.
- Mad Libs Generator: Creates a story based on user input.
- Rock, paper, scissors: Classic game of rock, paper, scissors.

### python-projects/pytest-plugin
- Plugin for registering Pytest assert rewrite.

### python-projects/test
- Pytest test cases.

## Usage

```bash
    # Easy challenges
    python easy/calculator.py
    python easy/dice_rolling_simulator.py
    python easy/guess_the_number.py
    python easy/mad_libs_generator.py
    python easy/rock_paper_scissors.py

    # Pytest
    export PYTHONPATH=/path/to/your/pytest_plugin:/path/to/your/bin/python
    pytest -p src.pytest_plugin test/test_dictionary.py
```

# Example Usage

```
$ python easy/calculator.py
Enter an equation (or 'q' to quit): 1+2+3

         _____________________
        |  _________________  |
        | | 1+2+3 = 6       | |
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

$ python easy/dice_rolling_simulator.py
._______.
| o   o |
|   o   |
| o   o |
'-------'

$ python easy/guess_the_number.py
Welcome to the Guess the Number Game!
I'm thinking of a number between 1 and 100.
Enter your guess: 123
Too high! Try again.
Enter your guess:

$ python easy/mad_libs_generator.py
Enter prompt: There once was a cat
Story: There once was a cat that seemed to run on the sidewalk for hours. Today it is a cat, not a dog. As in, it has to look like, well, the same cat that was sitting at one end. And the second time it did, it looked just like her; I found all of her bones missing and I asked, okay, what did she look like? And it looked like like a cat that would be out of shape.

$ python easy/rock_paper_scissors.py
Choose Rock, Paper, or Scissors: scissors
You chose
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

Computer chose
    ________
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
You win!
Play again? (yes/no): yes

pytest -p src.pytest_plugin test/test_dictionary.py
...
>       assert actual == expected, error_message
E       AssertionError: The dictionaries are not equal!
E         Omitting 13 identical items, use -vv to show
E         Differing items:
E         {'name': 'Alice'} != {'name': 'Bob'}
E         Use -v to get more diff

test/assertions.py:15: AssertionError
```

## References

- [**Medium**](https://medium.com/@oliver.lovstrom)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- Email: oliver.lovstrom@gmail.com
- Project URL: https://github.com/OliLov/python-projects
