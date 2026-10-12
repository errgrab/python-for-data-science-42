from sys import argv


argc = len(argv)
try:
    assert argc <= 2, "more than one argument is provided"
    if argc == 1:
        exit()
    number = int(argv[1])
except ValueError:
    print("AssertionError: argument is not an integer")
    exit()
except AssertionError as error:
    print("AssertionError:", error)
    exit()

print("I'm Even." if number % 2 == 0 else "I'm Odd.")
