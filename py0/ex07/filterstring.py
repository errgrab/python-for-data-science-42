from sys import argv


def main():
    """Filter words by lenght."""
    argc = len(argv)

    try:
        assert argc == 3
        assert not argv[1].isdigit()
        n = int(argv[2])
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")
        return

    words = argv[1].split()
    print([w for w in words if (lambda w: len(w) > n)(w)])


if __name__ == "__main__":
    main()
