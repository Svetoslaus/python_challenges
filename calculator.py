numberOne = int(input("Your first number, please: "))
numberTwo = int(input("Your first number, please: "))
operation = input("Select an operation(+, -, /, *), please: ")


if operation == "+":
    # 1st code variant
    add = numberOne + numberTwo
    print(add)
elif operation == "-":
    sub = numberOne - numberOne
    print(sub)
elif operation == "/":
    # 2nd code variant
    print(numberOne / numberTwo)
elif operation == "*":
    print(numberOne * numberTwo)
else:
    print("Wrong operation...")
