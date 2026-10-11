
"""Phase 3: Search algorithm runtime analysis."""

import csv
import random
import statistics
import sys
import time
from pathlib import Path

# Import the professor's search algorithms.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from algorithms import (
    recursive_binary_search,
    iterative_binary_search,
    sequential_search,
)

DATA_SIZES = [5_000, 50_000, 100_000, 150_000, 1_000_000]
NUMBER_OF_TRIALS = 10


def verify_result(values, target, index):
    """Verify the index returned by a search algorithm."""
    if index == -1:
        return target not in values

    return (
        0 <= index < len(values)
        and values[index] == target
    )


def measure_search(search_function):
    """Time only the search operation in microseconds."""
    start = time.perf_counter()
    index = search_function()
    elapsed = (time.perf_counter() - start) * 1_000_000
    return index, elapsed


def main():
    """Run the experiments and save median runtimes."""
    results = []

    for size in DATA_SIZES:
        print(f"\nTesting data size: {size:,}")

        times = {
            "recursive": [],
            "iterative": [],
            "sequential": [],
        }

        for trial in range(1, NUMBER_OF_TRIALS + 1):
            # Generate and sort data before timing.
            values = sorted(
                random.randint(1, 1_000_000)
                for _ in range(size)
            )

            # Alternate present and absent targets.
            if trial % 2 == 1:
                target = random.choice(values)
            else:
                target = 1_000_001

            searches = {
                "recursive": lambda: recursive_binary_search(
                    values, target, 0, len(values) - 1
                ),
                "iterative": lambda: iterative_binary_search(
                    values, target
                ),
                "sequential": lambda: sequential_search(
                    values, target
                ),
            }

            for name, search_function in searches.items():
                index, elapsed = measure_search(search_function)

                assert verify_result(values, target, index), (
                    f"{name} failed for size {size}, trial {trial}"
                )

                times[name].append(elapsed)

            print(f"  Trial {trial}/10 completed")

        recursive_median = statistics.median(times["recursive"])
        iterative_median = statistics.median(times["iterative"])
        sequential_median = statistics.median(times["sequential"])

        results.append([
            size,
            recursive_median,
            iterative_median,
            sequential_median,
        ])

        print(
            f"  Recursive: {recursive_median:.3f} us | "
            f"Iterative: {iterative_median:.3f} us | "
            f"Sequential: {sequential_median:.3f} us"
        )

    # Save all five data sizes to a CSV file.
    output_path = Path(__file__).parent / "results.csv"

    with open(output_path, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "data_size",
            "recursive_binary_us",
            "iterative_binary_us",
            "sequential_us",
        ])

        for row in results:
            writer.writerow([
                row[0],
                f"{row[1]:.3f}",
                f"{row[2]:.3f}",
                f"{row[3]:.3f}",
            ])

    print("\nPHASE 3 COMPLETE!")
    print("All 50 trials completed successfully.")
    print(f"Results saved to: {output_path}")


if __name__ == "__main__":
    main()
