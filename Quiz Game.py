def new_game ():
    pass
def check_answer():
    pass
def score_display():
    pass
def try_again():
    pass
#---------------------------

questions = {"What is the chemical symbol for Gold?" : "D",
             "In what year was the first iPhone released?": "B",
             "What is the tallest mountain in the world?": "B",
             "Who painted the Mona Lisa?": "A"}

choices = ["A.Gd B.Go\nC.Ag D.Au",
           "A. 2005 B. 2007\nC. 2008 D. 2010",
           "A. K2 B. Mount Everest\nC. Mount Kilimanjaro D. Denali",
           "A. Leonardo da Vinci B. Michelangelo\nC. Raphael D. Caravaggio"]

print("Welcome to our Quiz Game!\n")

for i, question in enumerate(questions.keys()):
    print(question)
    for choice in choices[i]:
        print(choice, end = "")
    answer = input("\nYour Answer?: ")


print("\nThe end!")


