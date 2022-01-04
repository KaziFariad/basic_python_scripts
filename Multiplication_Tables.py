def Multiplication_Table():
    x = int(input("Enter a number for its multiplication table:"))
    for i in range(1, 13):
        print(x, "X", i, "=", x*i)


Multiplication_Table()
