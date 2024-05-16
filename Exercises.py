# fibonnacci sequence

def fibonacci(num):
    num1 = 0
    num2 = 1
    counter = 0
    for i in range(num):
        print(num1, end="\n" )

        num1 = num1 + num2
        num2 = num1 - counter
        counter = num2

num = int(input("Enter a number: "))
fibonacci(num)

