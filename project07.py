# Binary search

def binary_search(ls, key, start, end):
    if start <= end:
        mid = int((start + end) / 2)
        if ls[mid] > key:
            return binary_search(ls, key, start, mid - 1)
        elif ls[mid] < key:
            return binary_search(ls, key, mid + 1, end)
        else:
            return mid
    else:
        print("key %s not found!" % key)
a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
print(binary_search(a, 15, 0, a[-1]))