def multiplier(x):
    def multiplicant(y):
        return y * x
    return multiplicant

multiply = multiplier(23)
print(multiply(5))

#this is where a funtion was returned

def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()
def convey(func):
    text = func("Maayong gabi sa inyo mga real niggas")
    print(text)

convey(quiet)

# this is where a function becomes an object


# without walrus operator

# sports = list()
# while True:
#      sport = input("Enumerate the sports you know: ")
#      if sport.lower() == "quit":
#          break
#      sports.append(sport)

# with walrus operator

sports = list()
while sport := input("Enumerate the sports you know: ") != "quit":
    sports.append(sport)

for i in sports:
    print(i)



