import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    try:
        filename: str = sys.argv[1]
        file: typing.IO = open(filename, "r")
    except (FileNotFoundError, PermissionError, IsADirectoryError) as error:
        print(
            f"[STDERR] Error opening file '{filename}': {error}",
            file=sys.stderr
            )
        return
    else:
        print(f"Accessing file '{filename}'")
    print("---")
    print()
    content: str = file.read()
    print(f"{content}")
    print()
    print("---")
    file.close()
    print(f"File '{filename}' was closed.")
    print()
    print("Transform data:")
    print("---")
    print()
    lines: list[str] = [line + "#" for line in content.split("\n")]
    for line in lines:
        print(line)
    print()
    print("---")
    while True:
        try:
            sys.stdout.write("Enter new file name (or empty): ")
            sys.stdout.flush()
            raw: str = sys.stdin.readline()
            if raw == "":
                raise EOFError
            new_filename: str = raw.strip("\n")
        except (KeyboardInterrupt, EOFError) as error:
            print(error)
        else:
            if new_filename == "":
                print("Not saving data.")
                return
            else:
                print(f"Saving data to '{new_filename}'")
                try:
                    new_file: typing.IO = open(new_filename, "w")
                except (FileNotFoundError, PermissionError, IsADirectoryError) as error:
                    print(
                        f"[STDERR] Error opening file '{new_filename}': {error}",
                        file=sys.stderr
                        )
                    print("Data not saved.")
                    return
                else:
                    for line in lines:
                        new_file.write(line)
                        new_file.write("\n")
                    print(f"Data saved in file '{new_filename}'")
                    new_file.close()
                    return


if __name__ == "__main__":
    main()
