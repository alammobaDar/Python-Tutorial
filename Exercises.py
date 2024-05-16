#Palindrome checker

def is_palindrome(string):
    reverse_string = string[::-1]
    return reverse_string

string = input("Enter a word: ").upper()

reversed_string = is_palindrome(string)
if reversed_string== string:
    print(string," is a palindrome!")
else:
    print(string," is not a palindrome!")