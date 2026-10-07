

def secure_archive(filename: str, action: str = "r", content: str = "") -> tuple[bool, str]:
    try:
        if action == "r":
            with open(filename, "r") as f:
                data: str = f.read()
            return (True, data)
        else:
            with open(filename, "w") as f:
                f.write(content)
            return (True, "Content successfuly written to file")
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("☆ ★ ✮ ★ ☆  Cyber Archives Recovery & Preservation ☆ ★ ✮ ★ ☆\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    ok, data = secure_archive("ancient_fragment.txt")
    print(ok, repr(data))
    print()

    print("Using 'secure_archive' to write previous content "
          "to a new file:")
    print(secure_archive("new_fragment.txt", "w", data))


if __name__ == "__main__":
    main()
