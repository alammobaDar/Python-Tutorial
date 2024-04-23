def info(**name):
    result= ""
    print("Here's your full address")
    for arg in name.values():
        result += arg
        print (arg, end=" ")


    return result

print("enter your address")

number= input("Enter your House Number ")
street= input("Enter your Street: ")
town= input("Enter your Town: ")
city = input("Enter your City: ")
province= input("Enter your province: ")
country= input("Enter your Country: ")

info(a= number, b= street, c= town, d= city, e= province, f= country )



