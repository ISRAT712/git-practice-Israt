import datetime

print("Name: Israt")

today = datetime.date.today()
print("Today's date:", today)

from utils import add, subtract, multiply

print("Addition:", add(5, 3))
print("Subtraction:", subtract(5, 3))
print("Multiplication:", multiply(5, 3))