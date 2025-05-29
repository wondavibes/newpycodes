def main():
    word = input("enter a word: ")
    char = input("enter a character: ")

    indices = find_index(word, char)

    if indices:
        print(f"the character '{char}' is found at indices: {indices}")
    else:
        print(f"the character '{char}' is not found in the word")


def find_index(word, char):
    index = [i for i, c in enumerate(word) if c == char]
    return index


if __name__ == "__main__":
    main()