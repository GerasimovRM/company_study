n = int(input())
lst = [i ** 2 for i in range(n)]
lst2 = [str(elem) for elem in lst]
st = " ".join(lst2)
print(st)
