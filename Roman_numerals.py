def convert_roman(x):
    numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    result = 0
    prev_value = 0
    for char in x[::-1]:
        value = numerals[char]
        if value < prev_value:
            result -= value
        else:
            result += value
            prev_value = value
    return result

def convert_number(num):
    numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'Xl', 50: 'L', 90: 'LC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'DM', 1000: 'M'
    }
    result = ''
    for value in sorted(numerals.keys(), reverse=True):
        while num >= value:
            result += numerals[value]
            num -= value
    return result


# ___________________
print("Roman Converter\n")
option = ""
while option not in ["A", "B"]:
    option = input("A. Roman numerals to numbers \nB. Numbers to roman numerals\n")
    if option not in ["A", "B"]:
        print("Invalid Input")

if option.upper() == "A":
    char = input("Input a roman numerals: ").upper()
    print("The answer is: ", convert_roman(char))

elif option.upper() == "B":
    num = int(input("Input a number: "))
    print("The answer is: ", convert_number(num))




