
"""Phase 1: Basic testing of three search algorithms."""

from pathlib import Path
import sys

# Allow imports from the main project folder.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from algorithms import (
    recursive_binary_search,
    iterative_binary_search,
    sequential_search,
)


def run_searches(values, target, description):
    """Run and verify all three algorithms on the same input."""
    values = sorted(values)

    algorithms = [
        ("Recursive Binary Search", lambda: recursive_binary_search(
            values, target, 0, len(values) - 1
        )),
        ("Iterative Binary Search", lambda: iterative_binary_search(
            values, target
        )),
        ("Sequential Search", lambda: sequential_search(
            values, target
        )),
    ]

    print(f"\nTEST: {description}")
    print(f"List: {values}")
    print(f"Target: {target}")

    for name, search in algorithms:
        index = search()

        if index == -1:
            found = False
            correct = target not in values
        else:
            found = True
            correct = (
                0 <= index < len(values)
                and values[index] == target
            )

        status = "PASS" if correct else "FAIL"

        print(
            f"{name}: Found={found}, "
            f"Index={index}, Result={status}"
        )

        assert correct, f"{name} failed: {description}"


def main():
    """Test present, absent, boundary, and special cases."""
    values = [3, 5, 8, 12, 14, 18, 21]

    test_cases = [
        (values, 12, "Middle element"),
        (values, 9, "Absent target"),
        (values, 3, "First element"),
        (values, 21, "Last element"),
        ([12], 12, "One element - present"),
        ([12], 9, "One element - absent"),
        ([], 12, "Empty list"),
        ([3, 5, 5, 8, 12], 5, "Duplicate values"),
    ]

    for data, target, description in test_cases:
        run_searches(data, target, description)

    print("\nPHASE 1 COMPLETE: All 24 checks passed!")


if __name__ == "__main__":
    main()
