"""Local and global scope."""

app_name = "Python Basics"


def show_app_name():
    print("Inside function:", app_name)


def calculate_total():
    subtotal = 500
    tax = 50
    return subtotal + tax


show_app_name()
print("Outside function:", app_name)
print("Total:", calculate_total())

# subtotal is local to calculate_total(), so this would fail:
# print(subtotal)

