import random


number = random.randrange(0, 10)
print(number)
Score = 100
Difficulty = 0
guess = 0
continuePlaying = True
playGame = input("hello, would you like to play a guessing game with me? (Y/N): ")

while continuePlaying == True:
    if playGame == "N":
        print("Ok, maybe next time")
        continuePlaying = False
    if playGame == "Y":
        Mode = input("Yay! What level of difficulty would you like? Easy, Medium, or Hard? (E/M/H): ")
        if Mode == "M":
            Difficulty = 10
        if Mode == "H":
            Difficulty = 20
        else:
            Difficulty = 5
        guess = input("Great! Guess a number between 0 and 10: ")
        while int(guess) != number and Score > 0:
            if int(guess) >= number:
                guess = input("Lower! Guess again: ")
                Score = Score - Difficulty
            elif int(guess) <= number:
                guess = input("Higher! Guess again: ")
                Score = Score - Difficulty
            else:
                guess = input("Sorry, could you try again: ")
        if Score > 0:
            playGame = input("You guessed it! Would you like to play again? (Y/N)")
        else:
            playGame = input("Sorry, you ran out of tries! Would you like to play again? (Y/N): ")
    else:
        playGame = input("I'm sorry, I didn't get that, could you repeat? ")
        

        