import math
#скоро буду доделывать
def lvl_2(a, b, k):

    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y if y != 0 else None

    if k == 1:
        return add(a, b)
    elif k == 2:
        return subtract(a, b)
    elif k == 3:
        return multiply(a, b)
    elif k == 4:
        return divide(a, b)
    else:
        return None
    
def lvl_3(a, b, k):
    if k==1: return a+b
    elif k==2: return a-b
    elif k==3: return a*b
    elif k==4: return a/b
    else: return None

class Calc:
    def arithmetic(self, a, b, k):
        if k == 1:
            return a + b
        elif k == 2:
            return a - b
        elif k == 3:
            return a * b
        elif k == 4:
            return a / b if b != 0 else None
        else:
            return None

    def trignometric(self, a, k):
        if k == 5:
            return math.sin(a)
        elif k == 6:
            return math.cos(a)
        elif k == 7:
            return math.tan(a)
        else:
            return None

while True:
    a = int(input('Выберите уровень: 1, 2, 3, 4 >>> '))
    if a in [1,2,3]:
        b = int(input('Выберите операцию: 1) суммма, 2) вычитание, 3) умножение, 4) деление >>> '))
        if b not in [1,2,3,4]:
            print('Такой операции нет')
            continue
        else:
            x,y = list(map(int, input('Введите 2 числа через пробел >>> ').split()))
            if a==1:
                if b==1: print(x+y)
                elif b==2: print(x-y)
                elif b==3: print(x*y)
                elif b==4: print(x/y)
                else: 
                    print('Такой операции нет')
                    continue
            elif a==2: print(lvl_2(x,y,b))
            elif a==3: print(lvl_3(x,y,b))
    elif a == 4:
        b = int(input('Выберите операцию: 1) суммма, 2) вычитание, 3) умножение, 4) деление, 5) синус, 6) косинус, 7) тангенс >>> '))
        calc = Calc()
        if b in [1,2,3,4]:
            x,y = list(map(int, input('Введите 2 числа через пробел >>> ').split()))
            print(calc.arithmetic(x,y,b))
        elif b in [5,6,7]:
            x = float(input('Введите число в радианах >>> '))
            print(calc.trignometric(x,b))
        else: 
            print('Такой операции нет')
            continue
    else:
        print('Такого уровня нет')
        continue