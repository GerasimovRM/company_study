lst = [1, 2, 10, 12, 4]
lst2 = []
for elem in lst:
    lst2.append(elem ** 2)
print(lst2)

lst3 = [elem ** 2 for elem in lst]
print(lst3)