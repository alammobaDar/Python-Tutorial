def add(number1, number2):
    return number1 + number2

def sub(number1, number2):
    return number1 - number2

def mul(number1,number2):
    return number1 * number2

def div(number1, number2):
    return number1 / number2

print("Welcome this is my simple calculator")

while True:
    num1 = float(input("Enter the first number: "))
    operators = input("what operator to use? (+,-,*,/) ")
    num2 = float(input("Enter the second number: "))

    if operators == '+':
        print(add(num1, num2))
    elif operators == '-':
        print(sub(num1, num2))
    elif operators == '*':
        print(mul(num1, num2))
    elif operators == '/':
        print(div(num1, num2))
    else:
        print("Can you please follow my simpliest instruction you dimwit!!!")

    exit = input("Do you want to Continue Y/N ")
    if exit.upper() != 'Y':
        break
print()
print("Thank you for using our simple calculator")
print("Thank you for being the best and doing the best all the time, Thank you and Godbless!")




