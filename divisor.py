num = input("Please enter a number to find all divisors: ")
i = 1
while i <= int(num):
    if (int(num) % i == 0):
        print(str(i) + " "),
    i = i + 1
    #print(i)
