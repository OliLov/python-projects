# Python Projects

This repository is a collection of various Python projects, each showcasing different aspects and capabilities of Python programming. These projects are part of a 30-day Python challenge, where I am committed to writing articles on Python topics for 30 consecutive days. You can follow my journey and read these articles on my [Medium](https://medium.com/@oliver.lovstrom) blog. Each project in this collection is standalone and demonstrates various Python concepts.

## Projects

### python-projects/easy
- Calculator: Performs basic arithmetic operations like addition, subtraction, multiplication, and division. Displays the result in a calculator.
- Dice Rolling Simulator: Simulates the roll of a die.
- Guess the Number: A game where the user tries to guess a randomly generated number.
- Mad Libs Generator: Creates a story based on user input.
- Palindrome Checker: Check if a phrase is a palindrome.
- Rock, paper, scissors: Classic game of rock, paper, scissors.
- Text analysis: Count words and characters in a text.

### python-projects/health
- Step Count: Extracting step count from Apple Health data, with different metrics for step count analysis.

### python-projects/pytest-plugin
- Pytest Plugin: Plugin for registering Pytest assert rewrite.

### python-projects/test
- Pytest Test Cases: Various test cases using Pytest.

## Usage

```bash
    # Easy challenges
    python easy/calculator.py
    python easy/dice_rolling_simulator.py
    python easy/fibonacci.py
    python easy/guess_the_number.py
    python easy/mad_libs_generator.py
    python easy/rock_paper_scissors.py
    python easy/palindrome_checker.py --help
    python easy/text_analysis.py --help

    # Health
    python health/step_count.py --help

    # Pytest
    export PYTHONPATH=/path/to/your/pytest_plugin:/path/to/your/bin/python
    pytest -p src.pytest_plugin test/test_dictionary.py
```

## Example Usage

### python-projects/easy
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

$ python easy/fibonacci.py
Enter the length of the Fibonacci sequence: 1000
Fibonacci sequence of length 1000 : [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...]

$ python easy/guess_the_number.py
Welcome to the Guess the Number Game!
I'm thinking of a number between 1 and 100.
Enter your guess: 123
Too high! Try again.
Enter your guess:

$ python easy/mad_libs_generator.py
Enter prompt: There once was a cat
Story: There once was a cat that seemed to run on the sidewalk for hours. Today it is a cat, not a dog. As in, it has to look like, well, the same cat that was sitting at one end. And the second time it did, it looked just like her; I found all of her bones missing and I asked, okay, what did she look like? And it looked like like a cat that would be out of shape.

% python easy/palindrome_checker.py "EYE"
The phrase EYE is a palindrome.

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

$ python easy/text_analysis.py example.txt
The file contains 4 words and 18 characters.
```

### python-projects/health

```
python health/step_count.py /path/to/your/apple_health_export/export.xml --steps 2000 --guideline 2000
The day with the most steps is 2019-05-30 with 33387 steps.
The longest streak of at least 2000 steps is 95 days, starting on 2023-09-12.
```

### python-projects/pytest-plugin

```
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

## Images

### easy/fibonacci.py
![Fibonacci spiral](/images/fibonacci.png)

### health/step_count.py
![Cumulative daily step count](/images/cumulative_steps.png)
![Average steps per weekday](/images/weekday_guideline.png)
![Daily Step Count Distribution](/images/distribution_guideline.png)

## References

- [**Medium**](https://medium.com/@oliver.lovstrom)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- Email: oliver.lovstrom@gmail.com
- Project URL: https://github.com/OliLov/python-projects
