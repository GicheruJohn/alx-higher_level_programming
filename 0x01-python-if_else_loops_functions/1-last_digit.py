#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % 10 if number > 0 else int(repr(number)[-1]) * -1
if lastdigit == 0:
    print(f"Last digit of {number} is {lastdigit} and is 0")
elif lastdigit > 5:
    print(f"Last digit of {number} is {lastdigit} and is greater than 5")
else:
    print(f'''Last digit of {number} is {lastdigit} and\
 is less than 6 and not 0''')
