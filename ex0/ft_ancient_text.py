import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    try:
        filename: str = sys.argv[1]
        file: typing.IO = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return
    else:
        print(f"Accessing file '{filename}'")
    print("---")
    print()
    try:
        content: str = file.read()
    except ValueError as error:
        print(f"Error reading from file '{filename}': {error}")
    else:
        print(f"{content}")
        print()
        print("---")
        file.close()
        print(f"File '{filename}' was closed.")


if __name__ == "__main__":
    main()
