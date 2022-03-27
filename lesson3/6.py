number = int(input())  # 123 -> 1 + 2 + 3 = 6
count = 0
while number != 0:
    count += number % 10
    number = number // 10
print(count)
