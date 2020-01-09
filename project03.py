# A Python program to check a number is Armstrong number

i = input("Enter the number: ")
try:
    n = len(i)
    s = 0
    for c in i:
        s += int(c)**n
    if s == int(i):
        print("%s is a Armstrong Number!" % i)
    else:
        print("%s is not a Armstrong Number!" % i)
except:
    print("Invalid input!")