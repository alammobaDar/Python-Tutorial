import os

source = 'sample.txt'
destination = "C:\\Users\\Admin\\Desktop\\sample.txt"

try:
    if os.path.exists(destination):
        print("There's such file!")
    else:
        os.replace(source,destination)
        print(source +" was moved")
except FileNotFoundError:
    print(source+" was not found")





