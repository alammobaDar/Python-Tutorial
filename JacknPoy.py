import random

Computer = ["Rock", "Paper",  "Scissor"]

x = random.choice(Computer)
print("Let's play Jack n' poy!!")

while True:

    choice = input("Choose between (Rock, Paper, Scissor): ")

    if (choice.lower() == "rock" and x == "Paper" or choice.lower() == "paper" and x == "Scissor" or choice.lower() == "scissor" and x == "Rock"):
        print("You Lose!")
        print(x)
    elif(choice.lower() == "paper" and x == "Paper" or choice.lower() == "rock" and x == "Rock" or choice.lower() == "scissor" and x == "Scissor"):
        print("DRAWWWWWW!!!")
        print(x)
    elif(choice.lower() == "paper" and x == "Rock" or choice.lower() == "rock" and x == "Scissor" or choice.lower() == "scissor" and x == "Paper"):
        print("You Win!!")
        print(x)
    else:
        print("Wrong input you Broke ass nigga bitch!!")

    exit = input("Try again Y/N: ")
    if (exit.upper() != "Y"):
        break

print("Thank you for playing ahihihihi /// ///")