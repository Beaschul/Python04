import sys

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename: str = sys.argv[1]

    print("\n☆ ★ ✮ ★ ☆  Cyber Archives Recovery & Preservation ☆ ★ ✮ ★ ☆\n")
    print(f" ★ Accessing file '{filename}' ★ ")
    print("────୨ৎ────\n")

    try:
        f = open(filename, "r")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return

    content: str = f.read()
    print(content, end="")
    print("\n")
    print("────୨ৎ────")

    f.close()
    print(f" ★ File '{filename}' closed. ★")

    print("\n⋆˚࿔ Transform data: ⋆˚࿔\n")

    transformed: str = ""
    for line in content.splitlines():
        transformed += line + "#\n"

    print(transformed, end="")
    print("\n────୨ৎ────")

    new_name: str = input("Enter new file name (or empty): ")
    if new_name == "":
        print("( ˶°ㅁ°) Not saving data. !!")
        return
    print(f"Saving data to '{new_name}'")
    try:
        f2 = open(new_name, "w")
    except OSError as e:
        print(f"Error opening file '{new_name}' (ó﹏ò｡) : {e}")
        print("Data not saved (O_O)!")
        return

    f2.write(transformed)
    f2.close()
    print(f"Data saved in file '{new_name}' ૮₍˶ᵔ ᵕ ᵔ˶₎ა")
    

if __name__ == "__main__":
    main()