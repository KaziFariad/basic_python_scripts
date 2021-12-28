str = input()

words = str.split(" ")

smallest_word = words[0]
biggest_word = words[0]

for word in words:
    if len(word) < len(smallest_word):
        smallest_word = word
    if len(word) > len(biggest_word):
        biggest_word = word

print("Biggest word is: " + biggest_word)
print("Smallest word is: " + smallest_word)
