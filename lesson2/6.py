print("Первая или последняя буква греческого алфавита")
# альфа омега
greek_letter_first = input()
greek_letter_last = input()
if greek_letter_first == "альфа" and greek_letter_last == "омега":
    print("Вы знаток греческой культуры")
elif greek_letter_first == "альфа" or greek_letter_last == "омега":
    print("Не, ну че-то Вы знаете")
else:
    print("Наверное, Вы разбираетесь в чем-то другом..")
