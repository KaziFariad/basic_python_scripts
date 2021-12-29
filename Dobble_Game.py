import string
import random
symbols = list(string.ascii_letters)
card1 = [0]*7
card2 = [0]*7
i = 0
ss = random.choice(symbols)
symbols.remove(ss)
posi1 = random.randrange(7)
posi2 = random.randrange(7)
if(posi1 == posi2):
    card1[posi1] = card2[posi2] = ss
else:
    card1[posi1] = ss
    card2[posi2] = ss
    card1[posi2] = random.choice(symbols)
    symbols.remove(card1[posi2])
    card2[posi1] = random.choice(symbols)
    symbols.remove(card2[posi1])
while(i < 7):
    if(i != posi1 and i != posi2):
        card1[i] = random.choice(symbols)
        symbols.remove(card1[i])
        card2[i] = random.choice(symbols)
        symbols.remove(card2[i])
    i += 1
print(card1, card2, sep='\n')
a = input("Enter your answer: ")
if(a == ss):
    print("Right!")
else:
    print("Wrong!")
