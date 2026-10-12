from sys import argv


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",    "B": "-... ",  "C": "-.-. ",  "D": "-.. ",
    "E": ". ",     "F": "..-. ",  "A": ".- ",    "B": "-... ",
    "C": "-.-. ",  "D": "-.. ",   "E": ". ",     "F": "..-. ",
    "G": "--. ",   "H": ".... ",  "I": ".. ",    "J": ".--- ",
    "K": "-.- ",   "L": ".-.. ",  "M": "-- ",    "N": "-. ",
    "O": "--- ",   "P": ".--. ",  "Q": "--.- ",  "R": ".-. ",
    "S": "... ",   "T": "- ",     "U": "..- ",   "V": "...- ",
    "W": ".-- ",   "X": "-..- ",  "Y": "-.-- ",  "Z": "--.. ",
    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
    "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
    "8": "---.. ", "9": "----. ",
}


def main():
    """Encode a string into Morse code."""
    argc = len(argv)
    try:
        assert argc == 2
        text = argv[1].upper()
        assert all(char in NESTED_MORSE for char in text)
    except AssertionError:
        print("AssertionError: the arguments are bad")
        return

    print("".join(NESTED_MORSE[char] for char in text))


if __name__ == "__main__":
    main()
