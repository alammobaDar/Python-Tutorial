words = {'prejudice' : 'preconceived opinion that is not based on reason or actual experience.'
        , 'rendezvous' : 'a meeting at an agreed time and place, typically between two people.'
        , 'entrepreneur' : 'an individual who creates a new business, bearing most of the risks and enjoying most of the rewards.'
        , 'intrapersonal' : ' occurring within the individual mind or self. '}

question = input("enter a word: ")

if question == 'prejudice':
    print(words['prejudice'])
elif question == 'rendezvous':
    print(words['rendezvous'])
elif question == 'entreprenuer':
    print(words['entrepreneur'])
elif question == 'intrapersonal':
    print(words['intrapersonal'])
else:
    print(words.get(question))