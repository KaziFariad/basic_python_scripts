def Sum_to_n(n):
    answer = 0
    for i in range(1, n+1):
        answer = answer + i
        if(answer <= 1):
            print("First number is:", answer)
        else:
            print("First", i, "numbers sums up to: ")
            print(answer)


Sum_to_n(int(input("Enter n numbers to sum up to: ")))
