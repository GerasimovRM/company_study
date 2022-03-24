# от строки к другим типам
st = "123"
num_int = int(st)
print(type(st), type(num_int))

st2 = "123.45"
print(float(st2) + 3)


num = 123
st3 = str(num)
print(st3 + "Роман")