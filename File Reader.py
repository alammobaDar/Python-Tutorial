path = input("Input a text file path: ")

purpose = input("How can i help you? (Read/Write/Append/Clear): ")

try:
    if purpose.lower() == "read":
        with open (path, 'r') as file:
            print(file.read())
    elif purpose.lower() == "write":
        with open(path, 'w') as file:
            input = input("Input a text: ")
            file.write(input)
    elif purpose.lower() == "append":
        with open(path, 'a') as file:
            input = input("Input a text: ")
            file.write(input)
    elif purpose.lower() == "clear":
        with open(path, 'r+')as file:
            file.seek(0)
            file.truncate()
except FileNotFoundError:
    print("such file does not exist")

