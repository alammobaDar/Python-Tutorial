try:
    with open("C:\\Users\\Admin\\Desktop\\test.txt.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("Di nahanap ang file haha")