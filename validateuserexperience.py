"""Validate a user's name using a few simple input rules."""

MAX_NAME_LENGTH = 12


def validate_name(name: str) -> str | None:
    """Return an error message for an invalid name, otherwise ``None``."""
    if len(name) > MAX_NAME_LENGTH:
        return "Name is too long. Please enter a name with 12 characters or fewer."
    if " " in name:
        return "Name cannot have spaces. Please enter a valid name."
    if not name.isalpha():
        return "Name must contain only letters. Please enter a valid name."
    return None


def main() -> None:
    """Read and validate a name from standard input."""
    name = input("Please enter your name: ").strip()
    error = validate_name(name)
    if error:
        print(error)
    else:
        print(f"Welcome, {name}!")


if __name__ == "__main__":
    main()
