print("Simple Chat Bot project for beginners")
print("To start ")
nameOfUser = input("please Enter you Name: ")
developerName = "de Developer"
questionOne = "what is My Name?"
answerOne = "Your name is "+nameOfUser

questionTwo = "what is you Name?"
answerTwo = "My name is "+developerName

query = input("Enter Your Question Here")
if query == questionOne:
    print(answerOne)
elif query == questionTwo:
    print(answerTwo)
elif query == "Noun":
    print("Naming Word is called Noun")
elif query == "Verb":
    print("Action Word is called Verb")
elif query == "Pronoun":
    print("we use it instead of Noun")
else:
    print("Data not included yet")
    print("try the suggested word Below")
    print("suggested Words are \n 1: noun \n2: verb \n3: pronoun")
