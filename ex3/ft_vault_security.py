def secure_archive(filename: str, mode: str = "r", content: str = ""
                   ) -> tuple[bool, str]:
    try:
        valid: bool = False
        with open(filename, mode) as file:
            if mode == "r":
                content = file.read()
            elif mode in ("w", "a"):
                file.write(content)
                content = "Content successfully written to file"
            else:
                content = f"Invalid mode '{mode}'"
                return (valid, content)
    except (
        FileNotFoundError, PermissionError, IsADirectoryError, ValueError
            ) as error:
        content = str(error)
    valid = True
    return (valid, content)


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistant file:")
    print(secure_archive("non/exisant/file", "r"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("no_permission", "r"))
    print()
    print("Using 'secure_archive' to read regular file:")
    print(secure_archive("test.txt", "r"))
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive(
        "test.txt", "w",
        "[FRAGMENT 001] Digital preservation protocols established"
        "2087\n[FRAGMENT 002] Knowledge must survive the entropy"
        "wars\n[FRAGMENT 003] Every byte saved is a victory against oblivion"
        ))


if __name__ == "__main__":
    main()
