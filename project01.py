# A Python program to print double sided stair-case pattern 

NOL = int(input("Enter the number of lines: "))

for LI in range(1, NOL + 1):

    EI = LI if (LI % 2 == 0) else LI + 1

    for CI in range(EI, NOL):
        if CI >= EI:
            print(end = " ")

    for l in range(0, EI):
        if l == EI - 1:
            print("*")
        else:
            print("*", end = " ")
    
    # Created by Aman Sikarwar
