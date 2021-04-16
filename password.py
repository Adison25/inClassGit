import random
import string
num = input("Please enter a number to find all divisors: ")
password = ""
i = 0
while i < int(num):
    password += random.choice(string.ascii_letters)
    #print(i)
    i = i + 1
print(password)