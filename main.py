# Dictionary comprehension

c_cities = {"MANILA": 31, "CAVITE": 33, "TAGAYTAY": 25, "TUGUEGARAO": 37 }
f_cities = {keys: round(value*(9/5))+32 for(keys, value) in c_cities.items()}
print(f_cities)

#--------------------------------------------------

c_cities = {"MANILA": 31, "CAVITE": 33, "TAGAYTAY": 25, "TUGUEGARAO": 37 }
sunny = {keys: value for(keys,value) in c_cities.items() if value <= 30}
print(sunny)

#--------------------------------------------------

c_cities = {"MANILA": 31, "CAVITE": 33, "TAGAYTAY": 25, "TUGUEGARAO": 37 }
disc_cities = {keys: ("warm" if value >=30  else "cold") for(keys, value) in c_cities.items()}
print(disc_cities)

#--------------------------------------------------
def temp(value):
    if value > 33:
        return "Hot!"
    elif value >= 33 >30:
        return "Warm!"
    else:
        return "Cold!"

c_cities = {"MANILA": 31, "CAVITE": 33, "TAGAYTAY": 25, "TUGUEGARAO": 37 }
disc_cities = {keys: temp(value) for(keys, value) in c_cities.items()}
print(disc_cities)
