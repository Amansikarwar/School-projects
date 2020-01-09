# Insertion sorting

ls = [4,93,54,65,7,3,43,31,74,10]
for i in range(1, len(ls)):
    key = ls[i]
    j = i - 1
    while j >= 0 and ls[j] > key:
        ls[j + 1] = ls[j]
        j -= 1
    ls[j + 1] = key
print(ls)