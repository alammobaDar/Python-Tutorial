# vowel counter

def reverse_string(string):
    for i in string[::-1]:
        print(i, end ="")


string = input("Enter a string: ")
reverse_string(string)