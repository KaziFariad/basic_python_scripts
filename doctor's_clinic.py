def Continue():
    print("Clinic is opening! Please collect tokens...")
    n = 1
    c = 1
    while(c):
        print("Token no.", n, ", Please come in!")
        ch = input("Continue?(y/n)")
        if(ch == 'n' or ch == 'no' or ch == 'No'):
            c = 0
            print("Clinic is closed! Please come again.")
        else:
            n = n + 1


Continue()
