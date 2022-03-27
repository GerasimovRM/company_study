count = 0
number = int(input())
while number != 0:
    if number % 10 == 2 and number % 4 == 0:
        count += 1
    number = int(input())
print(count)
