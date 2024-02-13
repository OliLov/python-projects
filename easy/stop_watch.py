"""Stop watch."""

import time


def stopwatch():
    """Stop watch."""
    while True:
        choice = input("Press Enter to start the stopwatch, or 'q' to quit...")
        start_time = time.time()
        if choice == "q":
            break

        choice = input("Press Enter to stop the stopwatch...")
        end_time = time.time()
        if choice == "q":
            break

        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    stopwatch()
