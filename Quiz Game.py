questions = {"What is the chemical symbol for Gold?" : "D",
             "In what year was the first iPhone released?": "B",
             "What is the tallest mountain in the world?": "B",
             "Who painted the Mona Lisa?": "A"}

choices = ["A.Gd B.Go\nC.Ag D.Au",
           "A. 2005 B. 2007\nC. 2008 D. 2010",
           "A. K2 B. Mount Everest\nC. Mount Kilimanjaro D. Denali",
           "A. Leonardo da Vinci B. Michelangelo\nC. Raphael D. Caravaggio"]

#_____________________________________________________________
def new_game ():
    print("Welcome to our Quiz Game!\n")

    score = 0

    for i, question in enumerate(questions.keys()):
        print("*-----------------------------------------*")
        print(question)
        for choice in choices[i]:
            print(choice, end = "")
        answer = input("\nYour Answer?: ").upper()
        score = check_answer(score, answer, question)

    score_display(score)
    try_again()
#_____________________________________________________________
def check_answer(score, answer, question):

    correct_answers = questions[question]
    if answer == correct_answers:
        score += 10
    return score
#_____________________________________________________________
def score_display(score):

   print("\nScore: ", score)

   if score == 40:
       print("You are Excellent")
   elif score == 30:
       print("That is great!")
   elif score == 20:
       print("You are good!")
   elif score == 10:
       print("Fair Enough!")
   else:
       print("Study more!")
#_____________________________________________________________
def try_again():
    reset = input("\nDo you want to try again? (Y/N)").upper()

    if reset == "Y":
        new_game()
    else:
        print("\nThank you for your time!")
#_____________________________________________________________

new_game()
print("The end!")


