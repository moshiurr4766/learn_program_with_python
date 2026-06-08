"""Exception handling with try, except, else, and finally."""


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError:
        print("Both values must be numbers.")
    else:
        print("Result:", result)
    finally:
        print("Division attempt finished.")


divide(10, 2)
divide(10, 0)
divide("10", 2)

