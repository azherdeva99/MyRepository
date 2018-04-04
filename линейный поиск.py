list = [1, 2, 45, 67, 78, 81, 93, 99]
x = 45

def linear_search(list, x):
    j = len(list) - 1 # число элементов в list -1
    s = 0
    while x != list[s]:
        s += 1
    return s if s < j else None
print(linear_search(list, x))