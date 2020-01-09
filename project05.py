# A python program to convert decimal to Hexadecimal

number = int(input("Enter the number: "))
hexadecimal = ""
temp = number
alpha = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
while number > 0:
    remainder = number % 16
    if remainder > 9:
        hexadecimal += alpha[remainder]
    else:
        hexadecimal += str(remainder)
    number = number // 16
print("The hexadecimal equavalent of %d is %s" % (temp , hexadecimal[::-1]))