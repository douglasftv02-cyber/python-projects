import random
import string


def generate_password(length):
    """Generate a random password."""

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("=" * 40)
    print("      PYTHON PASSWORD GENERATOR")
    print("=" * 40)

    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password must have at least 4 characters.")
            return

        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
