# A python program to check whether a number is perfect square

from math import sqrt, floor

try:
    n = int(input("Enter a number to check: "))
    s = sqrt(n)
    if floor(s) == s:
        print("%d is a perfect square" % n)
    else:
        print("%d is not a perfect square" % n)
except ValueError as error:
    print("Invalid input!")
    print("ERROR: %s" % error)
