# Prime numbers

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        print(i)
        if num % i ==0:
            return False
    return True

Enter a number: 53
2
3
4
5
6
7
2
3
4
5
6
7
Its a prime

num = int(input("Enter a number: "))
is_prime(num)


if is_prime(num)== True:
    print("Its a prime")
else:
    print("Its, not")

# for i in range(2, int(20**0.5)+1):
#         print(i)