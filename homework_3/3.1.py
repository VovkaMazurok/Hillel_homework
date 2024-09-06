x = int(input("Enter the first number: "))
w = input("Enter a mathematical operation: ")
y = int(input("Enter the second number: "))

if w == "+":
    print(x + y)
elif w == "-":
    print(x - y)
elif w == "*":
    print(x * y)
elif w == "/":
    if y == 0:
        print("The divisor cannot be equal to 0")
        y = int(input("Please enter a number that is not equal to 0: "))
    print(x / y)
