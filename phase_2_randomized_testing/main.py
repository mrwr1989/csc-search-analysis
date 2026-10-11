
"""Phase 2: Randomized testing of search algorithms."""

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from algorithms import (
    recursive_binary_search,
    iterative_binary_search,
    sequential_search,
)


def check_result(values, target, index):
    """Check whether a returned search index is valid."""
    if index == -1:
        return target not in values
    return 0 <= index < len(values) and values[index] == target


def main():
    """Run controlled randomized search tests."""
    successful = 0
    unsuccessful = 0

    for trial in range(1, 11):
        values = [random.randint(1, 100) for _ in range(20)]
        values.sort()

        # Alternate cases to guarantee both outcomes.
        expected_to_be_present = trial % 2 == 1

        if expected_to_be_present:
            target = random.choice(values)
            successful += 1
        else:
            target = 101
            unsuccessful += 1

        print(f"\nTRIAL {trial}")
        print(f"Sorted list: {values}")
        print(f"Target: {target}")
        print(f"Expected present: {expected_to_be_present}")

        results = {
            "Recursive Binary": recursive_binary_search(
                values, target, 0, len(values) - 1
            ),
            "Iterative Binary": iterative_binary_search(
                values, target
            ),
            "Sequential": sequential_search(values, target),
        }

        for name, index in results.items():
            correct = check_result(values, target, index)
            status = "PASS" if correct else "FAIL"
            print(f"{name}: Index={index}, {status}")
            assert correct, f"{name} failed on trial {trial}"

    print("\nPHASE 2 COMPLETE")
    print(f"Successful searches: {successful}")
    print(f"Unsuccessful searches: {unsuccessful}")
    print("All 30 algorithm checks passed!")


if __name__ == "__main__":
    main()
