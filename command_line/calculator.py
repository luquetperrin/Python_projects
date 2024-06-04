import sys


if len(sys.argv) != 4:
    print("Usage: python calculator.py <num1> <operator> <num2>")
    sys.exit(1)

num1 = float(sys.argv[1])
operator = sys.argv[2]
num2 = float(sys.argv[3])

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print(f"Invalid operator: {operator}")
    sys.exit(1)

print(f"The result is: {result}")
