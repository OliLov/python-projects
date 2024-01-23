"""Dice rolling simulator."""
import os
import random
import time

rolling_dice = (
    [
        "  .-------.",
        " /   o   /|",
        "/_______/o|",
        "| o     | |",
        "|   o   |o/",
        "|     o |/ ",
        "'-------'  ",
    ],
    [
        "   ______   ",
        "  /\\     \\  ",
        " /o \\  o  \\ ",
        "/   o\\_____\\",
        "\\o   /o    /",
        " \\ o/  o  / ",
        "  \\/____o/  ",
    ],
)

dice_face = {
    1: [
        "._______.",
        "|       |",
        "|   o   |",
        "|       |",
        "'-------'",
    ],
    2: [
        "._______.",
        "| o     |",
        "|       |",
        "|     o |",
        "'-------'",
    ],
    3: [
        "._______.",
        "| o     |",
        "|   o   |",
        "|     o |",
        "'-------'",
    ],
    4: [
        "._______.",
        "| o   o |",
        "|       |",
        "| o   o |",
        "'-------'",
    ],
    5: [
        "._______.",
        "| o   o |",
        "|   o   |",
        "| o   o |",
        "'-------'",
    ],
    6: [
        "._______.",
        "| o   o |",
        "| o   o |",
        "| o   o |",
        "'-------'",
    ],
}

roll = random.randint(1, 6)

for idx in range(1, 10):
    if idx % 2 == 1:
        dice = rolling_dice[0]
    else:
        dice = rolling_dice[1]

    for line in dice:
        print(line)
    time.sleep(0.2)

    # Clear console.
    os.system("clear" if os.name == "posix" else "cls")

for line in dice_face[roll]:
    print(line)
