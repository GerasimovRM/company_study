a = int(input())
result_min = a
while a != 0:
    if result_min > a:
        result_min = a
    a = int(input())
print(result_min)
