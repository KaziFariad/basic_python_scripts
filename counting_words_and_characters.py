s = list(input())

chars = 0
words = 0

for i in s:
    if (i == " "):
        words += 1
    else:
        chars += 1
words += 1
print(chars)
print(words)
