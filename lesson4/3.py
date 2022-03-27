text = input()
a = int(input())
b = int(input())
result = ""
for i in range(a - 1, b):
    result += text[i]
print(result)
