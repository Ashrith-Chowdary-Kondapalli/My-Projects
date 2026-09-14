"""Interactive donation confirmation exercise.

This script demonstrates integer input, confirmation, validation, and
number formatting. It does not process real payments or transfer money.
"""


def main() -> None:
    """Prompt for a donation amount and confirm it with the user."""
    while True:
        try:
            donation = int(input("Enter the amount you would like to donate: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if donation < 0:
            print("Donation amount cannot be negative.")
            continue

        confirmation = input(
            f"Are you sure you want to donate ${donation:,}? (yes/no): "
        ).strip().lower()

        if confirmation == "yes":
            print(f"Thank you for your generous donation of ${donation:,}!")
            return

        print("Donation cancelled.")
        return


if __name__ == "__main__":
    main()
