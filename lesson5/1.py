# int, float, bool - значения
# str, list, tuple, set, dict - коллекция

st = "123sAd"

lst = [2, 3, 5, 6, True]
for i in range(len(lst)):
    print(lst[i])

for elem in lst:
    print(elem)


print(lst)
lst[2] = 125
print(lst)


print(lst[1:4])
print(lst)
lst.append("##")
print(lst)
elem = lst.pop(0)
print(lst, elem)

lst2 = [1, 2, 3] + [4, 5, 6]
print(lst2)
lst3 = [1, 2, 3] * 4
print(lst3)
