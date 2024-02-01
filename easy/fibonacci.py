"""Fibonacci."""
import numpy as np
from matplotlib import pyplot as plt


def fibonacci(length: int) -> list[int]:
    """Generate Fibonacci sequence.

    :param length: The length of the Fibonacci sequence.
    :return: The Fibonacci sequence of length.
    """
    if length <= 0:
        return []

    if length == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < length:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence


def plot_fibonacci(sequence: list[int]) -> None:
    """Plot Fibonacci spiral.

    :param sequence: Fibonacci sequence.
    """
    # Calculate the golden ratio
    golden_ratio = sequence[-1] / sequence[-2]

    # Generate angles for the spiral
    angles = np.linspace(0, 8 * np.pi, num=len(sequence))

    # Calculate radius for logarithmic spiral
    radius = golden_ratio ** (angles / np.pi)

    # pylint: disable=invalid-name
    # Convert to Cartesian coordinates
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)

    # Create the plot
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, color="blue", linewidth=2)
    plt.axis("equal")
    plt.axis("off")
    plt.show()


def main() -> None:
    """Main function."""
    while True:
        try:
            length = int(input("Enter the length of the Fibonacci sequence: "))
            if length < 0:
                print("Please enter a non-negative integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    sequence = fibonacci(length)
    print(f"Fibonacci sequence of length {length}: {sequence}")
    plot_fibonacci(sequence)


if __name__ == "__main__":
    main()
