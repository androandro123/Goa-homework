def symbol(number):
    if int(number) > 0:
        print("this number is positive")
    if int(number) < 0:
        print("this number is negative")
    if int(number) == 0:
        print("this number equals to 0")
symbol(input("your number:"))