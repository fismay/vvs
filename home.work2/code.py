def one(text_1, n):
    if n==1: return (text_1.upper())
    if n==2: return (text_1.lower())
    if n==3: return (text_1.capitalize())

def two(text_2, n, x, y):
    if n==1: (text_2.find(x))
    if n==2: (text_2.replace(x, y, 1))
    if n==3: (text_2.count(x.upper()) + text_2.count(x.lower()))

def tree(text_3, n):
    if n==1: return (text_3.split())
    if n==2: return (text_3.join(text_3.split()))

def four (text_4, n):
    if n==1: return (text_4.isdigit()) #все символы - цифры и строка не пустая.
    if n==2: return (text_4.isalpha()) #все символы буквы и строка не пустая.
    if n==3: return (text_4.strip()) #без пробелов по краям
    if n==4: return (text_4.format()) 

def five(text_5):
    text_5 = ((text_5).strip()).capitalize()
    text_5 = text_5.replace(';', ' ')
    text_5 = text_5.replace('-', ' ')
    text_5 = text_5.replace('+', ' ')
    return text_5

while True:
    n = int(input('Выберите уровень: 1, 2, 3, 4, 5 >>> ')) #номер уровня

    if n==1: 
        metod = int(input('Выберите метод: 1)upper, 2)lower, 3)capitalize >>> '))
        text = input('Введите строку: ')
        print(one(text, metod))

    if n==2:
        metod = int(input('Выберите метод: 1)find, 2)replace, 3)count >>> '))
        text = input('Введите строку: ')
        if metod=='1':
            x = int(input('Введите слово, первое вхождение которого хотите найти: >>> '))
        if metod=='2':
            x = int(input('Введите слово, которое хотите заменить: >>> '))
            y = int(input('Введите слово, на которое хотите заменить: >>> '))
        if metod=='3':
            x = int(input('Введите букву, количество которых вы хотите посчитать: >>> '))
        print(two(text, metod, x, y))
    
    if n==3:
        metod = int(input('Выберите метод: 1)split, 2)join >>> '))
        text = input('Введите строку: ')
        print(tree(text, metod))
    
    if n==4: 
        metod = int(input('Выберите метод: 1)isdigit, 2)isalpha, 3)strip, 4)format >>> '))
        text = input('Введите строку: ')
        print(four(text, metod))
    
    if n==5:
        text = str(input('Введите строку: '))
        print(five(text))


