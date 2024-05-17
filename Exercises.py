# vowel counter

def vowel_counter(string):
    counter = 0
    for i in string[0:len(string)]:
        if i == "a" or i == "e" or i == "i" or i == "o"or i == "u":
            counter = counter + 1
    print(counter)

string = input("Enter a string")
vowel_counter(string)
