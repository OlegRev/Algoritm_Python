#   6 Пользователь вводит номер буквы в алфавите.
#   Определить, какая это буква.
print("введите номер буквы")
letter = int(input())

if letter < 27 and letter > 0:
       print(chr(letter + 96))
else:
    print("В латинском алфавите 26 букв!")

