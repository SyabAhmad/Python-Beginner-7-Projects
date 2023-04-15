print("Guess The Number Game in Python")
import random as md
print("Welcome to my Number Guessing Game")
print("To start the game First Enter Your Beautiful Name: ")
userName = input("Name: ")
print(f"Hello {userName} first clearly understand the rules")
print("1: guess the Number between 1 to 10")
print("2: and the computer will also guess the number between 1 to 10")
print("3: if both are equal you won else your moves will be decrement by 1")
print("4: if you all got wrong, the game will be over for you")
print("*Note, Total Number of Moves are 3")


numberOfMoves = 3
while numberOfMoves != 0:
    randNumber = md.randint(1, 10)
    userGuessednumber = input("Ener Any Number Between 1 and 10")
    numberOfMoves = numberOfMoves - 1
    if userGuessednumber==randNumber:
        print(f"You got it {userName}, 'Correct Answer'")
        break
    else:
        print(f"it is Game Over For you MR. {userName}, 'incorrect Answer'")
        print(f"it was {randNumber}")
