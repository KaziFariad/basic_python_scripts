import random


def pick():
    l = ['Computer', 'Grand Mother', 'New York',
         'Computer Science', 'Network', 'Fossil', 'Samsung']
    return random.choice(l)


def jumble(w):
    w = w.replace(" ", "")
    w = w.lower()
    return "".join(random.sample(w, len(w)))


def thank(p1n, p2n, p1s, p2s):
    print(p1n, ", Your score is:", p1s)
    print(p2n, ", Your score is:", p2s)
    print("Thanks for playing ", p1n, " and ", p2n)


def play():
    p1n = input("Player 1, Enter your name:")
    p2n = input("Player 2, Enter your name:")
    p1s = 0
    p2s = 0
    turn = 0
    while(1):
        if(turn % 2 == 0):
            print("Player 1, Your turn:")
            picked = pick()
            q = jumble(picked)
            print(q)
            guess = input("What do you think?")
            if(guess == picked or guess.lower() == picked.lower()):
                print("You got it!")
                p1s = p1s + 10
                print("Your score is: ", p1s)
            else:
                print("The word was: "+picked)
            c = int(input("Do you want to continue?(0/1):"))
            if(c == 0):
                thank(p1n, p2n, p1s, p2s)
                break
        else:
            print("Player 2, Your turn:")
            picked = pick()
            q = jumble(picked)
            print(q)
            guess = input("What do you think?")
            if(guess == picked or guess.lower() == picked.lower()):
                print("You got it!")
                p2s = p2s + 10
                print("Your score is: ", p2s)
            else:
                print("The word was: "+picked)
            c = int(input("Do you want to continue?(0/1):"))
            if(c == 0):
                thank(p1n, p2n, p1s, p2s)
                break
        turn = turn + 1


play()
