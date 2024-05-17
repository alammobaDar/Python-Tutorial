# list comprehension

def square_list(num):
    list = []
    for i in range(num):
        list.append(i*i)
    print(list)

num = int(input("Enter a number: "))
square_list(num)