# reduce() function
from functools import reduce
# example of applications of reduce()

# Summarizing data :Calculating the sum, product,
# maximum, or minimum value of a collection of data.

numbers = [1, 2, 3, 4, 5, 6]

result = reduce(lambda x, y: x + y, numbers)
print(numbers , "\nSum of Numbers: ", result)

# Aggregating data: Combining data from multiple sources
# or reducing a sequence of values to a single value.

String = ["Edrich"," ", "Darren"," ", "Santuyo" ]
combined_string = reduce(lambda x, y: x + y, String)
print("\n",String , "\nCombined string: ", combined_string)

## finds the largest number
numbers1 = [54, 6, 99, 32, 17]
largest = reduce(lambda x,y: x if x > y else y, numbers1)
print("\n",numbers1, "\nThe largest number is: ", largest)



# Iterative Operations:  Performing iterative operations
# such as factorials, exponentiation, or any other
# computation that requires combining elements of an iterable.

def factorial(x):
    return reduce(lambda x,y: x * y, range(1, x+1))
print("\nThe result will be: ", factorial(5))

# Functional programming: Implementing functional programming
# concepts such as folding, reducing, or accumulating data.

data = [14,82, 45,23,6]
result = reduce(lambda x,y: x-y if x>y else y - x, data)
print(data ,"\nThe result of the custom operation is: ", result)


