#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_digit = number%10
else:
    last_digit = number%(-10)
answer = ""
if last_digit > 5:
    answer = "is greater than 5"
elif last_digit == 0:
    anwer = f"is {number}"
else:
    answer = f"is less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} and {answer}")
