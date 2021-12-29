import random


def evolve(x):
    index = random.randrange(0, len(x))
    p = random.randint(1, 100)

    if(p == 1):
        print("p = ", p, "and index =", index)
        if(x[index] == '0'):
            x[index] = '1'


with open("DNA.txt", 'r+') as file:
    x = list(file.read())
print(x)
file.close()
for i in range(1, 1000):
    evolve(x)
print(x)
