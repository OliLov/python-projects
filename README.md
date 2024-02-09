# Python Projects

This repository is a collection of various Python projects, each showcasing different aspects and capabilities of Python programming. These projects are part of a 30-day Python challenge, where I am committed to writing articles on Python topics for 30 consecutive days. You can follow my journey and read these articles on my [Medium](https://medium.com/@oliver.lovstrom) blog. Each project in this collection is standalone and demonstrates various Python concepts.

## Projects

### python-projects/data_extraction
- HTML zip extractor to CSV: Opens a zip file to extract the names of HTML files contained within. It then creates a CSV file with the following format: [File name, Views, Reads]

### python-projects/easy
- Calculator: Performs basic arithmetic operations like addition, subtraction, multiplication, and division. Displays the result in a calculator.
- Currency Converter: Convert amount in USD to your currency.
- Dice Rolling Simulator: Simulates the roll of a die.
- Fibonacci: Generate Fibonacci sequence and Fibonacci spiral.
- Guess the Number: A game where the user tries to guess a randomly generated number.
- Mad Libs Generator: Creates a story based on user input.
- Palindrome Checker: Check if a phrase is a palindrome.
- Rock, paper, scissors: Classic game of rock, paper, scissors.
- Text analysis: Count words and characters in a text.
- Web Scraper: Simple web scraper implementation.

### python-projects/health
- Step Count: Extracting step count from Apple Health data, with different metrics for step count analysis.

### python-projects/image_analysis
- Annotate Blood Cells: Annotate blood smear images using XML file. Currently, parses files according to the format in [Complete Blood Cell Count Dataset](https://github.com/MahmudulAlam/Complete-Blood-Cell-Count-Dataset/tree/master)

### python-projects/machine_learning
- Object Detection Example: Performs object detection on example image.
- Object Detection: Performs object detection on given image.
- Convert Dataset: Convert dataset from PASCAL VOC XML format to YOLO format.
- Webcam Hand Draw: Simple script for drawing on webcam using MediaPipe.

### python-projects/notebooks
- Blood Count Yolo: Code for fine-tuning YOLOv8 on blood smear data.

### python-projects/pytest_plugin
- Pytest Plugin: Plugin for registering Pytest assert rewrite.

### python-projects/test
- Pytest Test Cases: Various test cases using Pytest.

## Usage

```bash
# Data Extraction
python data_extraction/html_zip_extractor_to_csv.py --help

# Easy Challenges
python easy/calculator.py
python easy/currency_converter.py --help
python easy/dice_rolling_simulator.py
python easy/fibonacci.py
python easy/guess_the_number.py
python easy/mad_libs_generator.py
python easy/rock_paper_scissors.py
python easy/palindrome_checker.py --help
python easy/text_analysis.py --help
python easy/web_scraper.py

# Health
python health/step_count.py --help

# Image Analysis
python image_analysis/annotate_blood_cells.py --help

# Machine Learning
python machine_learning/object_detection_example.py
python machine_learning/object_detection.py --help
python machine_learning/convert_dataset.py --help
python machine_learning/webcam_hand_draw.py

# Pytest
export PYTHONPATH=/path/to/your/pytest_plugin:/path/to/your/bin/python
pytest -p src.pytest_plugin test/test_dictionary.py
```

## Example Usage
For visuals, see output in [Images](#image-section)

### python-projects/data_extraction
```
$ python data_extraction/html_zip_extractor_to_csv.py your.zip
```

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

$ python easy/currency_converter.py "API_URL"
Convert USD to currency (Type 'exit' to quit): SEK
Amount in USD: 100
100.0 USD is 1039.6924999999999 SEK.
Convert USD to currency (Type 'exit' to quit): exit

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
The file has 4 words and 18 characters.

$ python easy/web_scraper.py
Oliver Lövström – Medium
```

### python-projects/health

```
$ python health/step_count.py /path/to/your/apple_health_export/export.xml --steps 2000 --guideline 2000
The day with the most steps is 2019-05-30 with 33387 steps.
The longest streak of at least 2000 steps is 95 days, starting on 2023-09-12.
```

### python-projects/image_analysis
```
$ python image_analysis/annotate_blood_cells.py IMAGE XML
```

### python-projects/machine_learning
```
$ python machine_learning/object_detection_example.py

$ python machine_learning/object_detection.py images/pedestrian_crossing.jpg --output images/pedestrian_crossing_output.jpg

$ python machine_learning/convert_dataset.py path/to/your/Complete-Blood-Cell-Count-Dataset/Training/Annotations yolo_data/training

$ python machine_learning/webcam_hand_draw.py
```

### python-projects/pytest_plugin

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

## Images <a name="image-section"></a>

### easy/fibonacci.py
![Fibonacci spiral](/images/fibonacci.png)

### health/step_count.py
![Cumulative daily step count](/images/cumulative_steps.png)
![Average steps per weekday](/images/weekday_guideline.png)
![Daily Step Count Distribution](/images/distribution_guideline.png)

### image_analysis/annotate_blood_cells.py
![Annotate Blood Cells](/images/blood_cells_example.png)

### machine_learning/object_detection_example.py
![Pedestrian Crossing](/images/pedestrian_crossing.jpg)
Image credit: [Photo by Mitchell Luo on Unsplash](https://unsplash.com/photos/a-group-of-people-walking-across-a-street-o7DGTER0POE)

### machine_learning/webcam_hand_draw.py
![Webcam Hand Draw](/images/webcam_hand_draw.jpg)

## References

- [**Medium**](https://medium.com/@oliver.lovstrom)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- Email: oliver.lovstrom@gmail.com
- Project URL: https://github.com/OliLov/python-projects
