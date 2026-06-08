"""Problem: Convert temperature using a class."""

# Problem:
# Convert Celsius to Fahrenheit and vice versa.


class TemperatureConverter:
    @staticmethod
    def c_to_f(celsius):
        return (celsius * 9 / 5) + 32

    @staticmethod
    def f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5 / 9


# Solution:
print("C to F:", TemperatureConverter.c_to_f(30))
print("F to C:", TemperatureConverter.f_to_c(86))

# Logic:
# 1. Put conversion formulas into static methods.
# 2. Call the methods without creating an object.
# 3. Print the converted values.

# Explanation:
# Static methods fit utility-style class behavior.
