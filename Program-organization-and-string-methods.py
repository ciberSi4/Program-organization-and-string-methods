# Организация программ и методы строк

my_string = input ("Введите произвольный текст: ")
print ("Количество символов введённого текста: ", my_string.__len__())
print ("Переменная my_string в верхнем регистре: ", my_string.upper())
print ("Переменная my_string в нижнем регистре: ", my_string.lower())
print ("Переменная my_string с удалёнными пробелами: ", my_string.replace(" ", ""))
print ("Первый символ переменной my_string: ", my_string[0])
print ("Последний символ переменной my_string: ", my_string[-1])