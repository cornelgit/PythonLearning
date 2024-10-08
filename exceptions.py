import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print('Error: Invalid error.')
    sys.exit(1)

# exception handling
try:
    result = x/y
except ZeroDivisionError:
    print('Error: Cannot divide by 0.')
    sys.exit(1)

print(f"{x} / {y} = {result}")