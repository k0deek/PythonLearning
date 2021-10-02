a = ["a", "b", "c", "a", "c", "z"]
b = {}
for el in a:
    if el in b.keys():
        b[el] = b[el]+1
    else:
        b[el] = 1
print(b)

