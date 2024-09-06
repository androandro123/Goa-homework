def  calculator(num1,operation,num2):
    num1 = int(input("first number:"))
    operation1 = input("operation you want:")
    num2 = int(input("second number:"))
    return num1
    return operation1
    return num2
    answer = 0
    if operation == "+":
        print(num1 + num2)
    if operation == "-":
        print(num1 - num2)
    if operation == "/":
        print(num1 / num2)
    if operation == "*":
        print(num1 * num2)
    else:
        print("this is not valid operation")
    if num2 == 0:
        print("this operation cannot happen")
    print(calculator(num1,operation1,num2))
