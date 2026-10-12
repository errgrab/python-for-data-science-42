from sys import argv


def main():
    """Count characters types in a string."""
    argc = len(argv)
    try:
        assert argc <= 2, "more than one argument is provided"
        text = argv[1] if argc == 2 else input(
            "What is the text to count?\n"
        ) + '\n'
    except AssertionError as error:
        print("AssertionError:", error)
        return

    upper = sum(c.isupper() for c in text)
    lower = sum(c.islower() for c in text)
    digits = sum(c.isdigit() for c in text)
    spaces = sum(c.isspace() for c in text)
    punct = sum(c in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' for c in text)

    print("The text contains", len(text), "characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punct, "punctuation marks")
    print(spaces, "spaces")
    print(digits, "digits")


if __name__ == "__main__":
    main()
