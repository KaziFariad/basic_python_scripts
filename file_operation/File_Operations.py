with open('Test.txt', 'r+') as f:
    print(f.read())
    f.write("How are you?")
f.close()
