"""Useful standard library modules."""

from datetime import date, datetime, timedelta
import math
import random

today = date.today()
now = datetime.now()
tomorrow = today + timedelta(days=1)

print("Today:", today)
print("Current time:", now.strftime("%H:%M:%S"))
print("Tomorrow:", tomorrow)

print("Floor:", math.floor(5.9))
print("Ceiling:", math.ceil(5.1))
print("Power:", math.pow(2, 3))

print("Random float:", random.random())
print("Random item:", random.choice(["red", "green", "blue"]))

