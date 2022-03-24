number = float(input())
if number < -3:
    print("(-inf, -3)")
elif -3 <= number < -1:
    print("[-3, -1)")
elif -1 <= number < 2:
    print("[-1, 2)")
elif 2 <= number < 10:
    print("[2, 10)")
else:
    print("[10, inf)")