import random
import art
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def getNumber():
    '''Function to get random number between 1 and 100'''
    return random.randint(1,100)
def selectLevel():
    '''Function to select difficulty level'''
    level=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level=="easy":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def play():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    num = getNumber()
    print("num: ", num)

    numOfGuessleft = selectLevel()
    endGame = False
    while not endGame:

        print(f"You have {numOfGuessleft} attempts remaining to guess the number.")
        guess = int(input("Guess a num: "))
        numOfGuessleft -= 1
        if guess == num:
            endGame = True
            msg = "Correct Guess"
        elif num > guess:
            if num - guess > 10:
                msg = "Too Low"
            else:
                msg = "Low"
        else:
            if guess - num > 10:
                msg = "Too High"
            else:
                msg = "High"
        print(msg)
        if numOfGuessleft > 0 and not endGame:
            print("Guess Again")
        else:
            endGame = True
            print(f"You lose.Correct number is : {num}")


if __name__ == '__main__':
    print(art.logo)
    play()




