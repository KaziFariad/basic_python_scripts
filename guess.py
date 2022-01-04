import random


def computerGuess(lowval, highval, randnum, count=0):
    if highval >= lowval:
        guess = lowval + (highval - lowval) // 2
        print(guess)
        if guess == randnum:
            print("Just Right!")
            return count
        elif guess > randnum:
            print("lower")
            count += 1
            return computerGuess(lowval, guess-1, randnum, count)
        else:
            print("higher")
            count += 1
            return computerGuess(guess+1, highval, randnum, count)
    else:
        return -1


randnum = random.randint(1, 101)

count = 0
guess = -99
while(guess != random):
    # Get the user's number
    guess = (int)(input("Enter a number between 1 and 100: "))
    if guess < randnum:
        print("higher")
    elif guess > randnum:
        print("lower")
    else:
        print("You guessed it!")
        break
    count += 1
# end of while loop

print("You took " + str(count) + " steps to guess the number")
print("Computer plays: ")
print("Computer took " + str(computerGuess(0, 100, randnum)) + " steps!")
