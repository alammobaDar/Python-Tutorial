# zip function
import pickle

def clear_data():
    confirmation = input("Are you sure you want to erase all of the existing datas? (Y/N)").upper()
    if confirmation == "Y":
        with open("data.pickle", "wb") as file:
            pickle.dump([], file)
        print("succesfully deleted")
    else:
        print("The datas remained")

while True:
    names = []
    age = []
    traits = []

    try:
        # Try to load data from a file named "data.pickle"
        with open("data.pickle", "rb") as file:
            names, age, traits = pickle.load(file)
        # If the file doesn't exist, it's the first run
    except FileNotFoundError:
        pass
    except (ValueError, pickle.UnpicklingError):
        print("Empty list, start a new\n")


    name1 = input("Enter a name: ")
    age1 = int(input("Enter age: "))
    traits1 = input("Enter traits: ")

    names.append(name1)
    age.append(age1)
    traits.append(traits1)

    with open("data.pickle", "wb") as file:
        pickle.dump((names, age, traits), file)

    exit = input("Do you want to exit? (Y/N)").upper()
    if exit == "Y":
        break

erase = input("Do you want to erase the datas? (Y/N)").upper()
if erase == "Y":
     clear_data()

else:

    infos = list(zip(names, age, traits))
    print("\nCharacters: ")
    for i in infos:
        print(i)
    print("Thank you 3x")

