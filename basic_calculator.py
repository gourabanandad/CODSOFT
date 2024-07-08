"""                                                 TASK 2                                                          """
a, b = map(int, input("Enter two number: ").split())
print('''[Enter '+' for addition.
 Enter '-' for subtraction.
 Enter '*' for multiplication.
 Enter '/' for division.]''')
op = input("Enter the operator: ")
# """For Addition."""
if op == '+':
    print(f"Addition of {a} and {b} is {a+b}.")
# """ For Subtraction """
elif op == '-':
    print(f"Subtraction of {a} and {b} is {a-b}.")
# """ For Multiplication """
elif op == '*':
    print(f"Multiplication of {a} and {b} is {a*b}.")
# """ For Division """
elif op == '/':
    print(f"Division of {a} and {b} and {a/b}.")
# Check If user enter wrong operator.
else:
    print("ERROR: Enter Valid Operator.")
