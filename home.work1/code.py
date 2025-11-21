import math

def lvl_2(a, b, k):
    def add(x, y):
        return x + y
        
    def sub(x, y):
        return x - y
        
    def mul(x, y):
        return x * y
        
    def div(x, y):
        if y == 0:
            return None
        return x / y

    if k == 1:
        return add(a, b)
    elif k == 2:
        return sub(a, b)
    elif k == 3:
        return mul(a, b)
    elif k == 4:
        return div(a, b)
    else:
        return None


def lvl_3(a, b, k):
    if k == 1:
        return a + b
    elif k == 2:
        return a - b
    elif k == 3:
        return a * b
    elif k == 4:
        if b == 0:
            return None
        return a / b
    else:
        return None


class Calculator:
    def arithmetic(self, a, b, operation):
        if operation == 1:
            return a + b
        elif operation == 2:
            return a - b
        elif operation == 3:
            return a * b
        elif operation == 4:
            if b == 0:
                return None
            return a / b
        else:
            return None
    
    def trigonometric(self, a, operation):
        if operation == 5:
            return math.sin(a)
        elif operation == 6:
            return math.cos(a)
        elif operation == 7:
            return math.tan(a)
        else:
            return None


while True:
    try:
        level = int(input('Выберите уровень: 1, 2, 3, 4 >>> '))
        
        if level == 1:
            operation = int(input('Выберите операцию: 1) сумма, 2) вычитание, 3) умножение, 4) деление >>> '))
            
            if operation not in [1, 2, 3, 4]:
                print('Такой операции нет')
                continue
            
            numbers = input('Введите 2 числа через пробел >>> ').split()
            if len(numbers) != 2:
                print('Нужно ввести ровно 2 числа')
                continue
                
            x = float(numbers[0])
            y = float(numbers[1])
            
            if operation == 1:
                result = x + y
                print(f"{x} + {y} = {result}")
            elif operation == 2:
                result = x - y
                print(f"{x} - {y} = {result}")
            elif operation == 3:
                result = x * y
                print(f"{x} * {y} = {result}")
            elif operation == 4:
                if y == 0:
                    print("Ошибка: деление на ноль")
                    continue
                result = x / y
                print(f"{x} / {y} = {result}")
                
        elif level == 2:
            operation = int(input('Выберите операцию: 1) сумма, 2) вычитание, 3) умножение, 4) деление >>> '))
            
            if operation not in [1, 2, 3, 4]:
                print('Такой операции нет')
                continue
            
            numbers = input('Введите 2 числа через пробел >>> ').split()
            if len(numbers) != 2:
                print('Нужно ввести ровно 2 числа')
                continue
                
            x = float(numbers[0])
            y = float(numbers[1])
            
            result = lvl_2(x, y, operation)
            if result is None and operation == 4:
                print("Ошибка: деление на ноль")
            elif result is not None:
                operations = {1: '+', 2: '-', 3: '*', 4: '/'}
                print(f"{x} {operations[operation]} {y} = {result}")
            else:
                print("Ошибка вычисления")
                
        elif level == 3:
            operation = int(input('Выберите операцию: 1) сумма, 2) вычитание, 3) умножение, 4) деление >>> '))
            
            if operation not in [1, 2, 3, 4]:
                print('Такой операции нет')
                continue
            
            numbers = input('Введите 2 числа через пробел >>> ').split()
            if len(numbers) != 2:
                print('Нужно ввести ровно 2 числа')
                continue
                
            x = float(numbers[0])
            y = float(numbers[1])
            
            result = lvl_3(x, y, operation)
            if result is None and operation == 4:
                print("Ошибка: деление на ноль")
            elif result is not None:
                operations = {1: '+', 2: '-', 3: '*', 4: '/'}
                print(f"{x} {operations[operation]} {y} = {result}")
            else:
                print("Ошибка вычисления")
                
        elif level == 4:
            operation = int(input('Выберите операцию: 1) сумма, 2) вычитание, 3) умножение, 4) деление, 5) синус, 6) косинус, 7) тангенс >>> '))
            
            calc = Calculator()
            
            if operation in [1, 2, 3, 4]:
                numbers = input('Введите 2 числа через пробел >>> ').split()
                if len(numbers) != 2:
                    print('Нужно ввести ровно 2 числа')
                    continue
                    
                x = float(numbers[0])
                y = float(numbers[1])
                
                result = calc.arithmetic(x, y, operation)
                if result is None and operation == 4:
                    print("Ошибка: деление на ноль")
                elif result is not None:
                    operations = {1: '+', 2: '-', 3: '*', 4: '/'}
                    print(f"{x} {operations[operation]} {y} = {result}")
                else:
                    print("Ошибка вычисления")
                    
            elif operation in [5, 6, 7]:
                x = float(input('Введите угол в радианах >>> '))
                
                result = calc.trigonometric(x, operation)
                if result is not None:
                    operations = {5: 'sin', 6: 'cos', 7: 'tan'}
                    print(f"{operations[operation]}({x}) = {result}")
                else:
                    print("Ошибка вычисления")
            else:
                print('Такой операции нет')
                continue
                
        else:
            print('Такого уровня нет')
            continue
            
    except ValueError:
        print("Ошибка: введите корректные числовые значения")
    except KeyboardInterrupt:
        print("\nПрограмма завершена")
        break