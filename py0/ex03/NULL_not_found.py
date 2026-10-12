from typing import Any


def NULL_not_found(object: Any) -> int:
    match object:
        case None:
            print("Nothing:", object, type(object))
            return 0
        case float():
            print("Cheese:", object, type(object))
            return 0
        case int() if not object:
            print("Zero:", object, type(object))
            return 0
        case str() if not object:
            print("Empty:", type(object))
            return 0
        case bool() if not object:
            print("Fake:", object, type(object))
            return 0
        case _:
            print("Type not Found")
    return 1
