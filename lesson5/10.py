lst = []
while True:
    elem = input()
    if elem == "стоп":
        break
    lst.append(int(elem))

print(lst)
print(sum(lst))
