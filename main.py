# list comprehension
## INSTEAD OF USING THIS:

List = []
for i in range(1,11):
    List.append(i*i)
print(List)

## Use this instead:
list = [i * i for i in range (1,11)]
print(list)

### Examples:

sections = [1,2,3,4,5,6,7,8,9,10,11,12]

list = [i for i in sections if i <= 6]
print("\nThe higher sections are: ", list)

list = [i if i <= 5 else str(i)+" (Lower section)" for i in sections]
print("\nThe higher sections are: ", list)