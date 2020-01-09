# A Python program to convert decimals to binary

try:
    number = int(input("Enter the number: "))
    binary = ""
    temp = number
    while number > 0:
        remainder = number % 2
        binary += str(remainder)
        number = number // 2
    print("The binary equavalent of %d is %s" % (temp , binary[::-1]))
except:
    print("Invalid input!")