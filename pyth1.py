import math

def calculator():
    print("Доступные операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("11. Выход")

    choice = input("Выберите номер операции: ")

    if choice == '11':
        return

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
        try:
            num1 = float(input("Введите первое число: "))
            if choice in ('6', '7', '8', '9', '10'):
                if choice == '6' and num1 < 0:
                    print("Ошибка: нельзя извлечь корень из отрицательного числа")
                
            elif choice == '7' and num1 < 0:
                print("Ошибка: нельзя вычислить факториал отрицательного числа")
                
            if choice in ('1', '2', '3', '4', '5'):
                num2 = float(input("Введите второе число: "))

            if choice == '1':
                result = num1 + num2
            elif choice == '2':
                result = num1 - num2
            elif choice == '3':
                result = num1 * num2
            elif choice == '4':
                if num2 == 0:
                    print("Ошибка: деление на ноль")
                else:    
                    result = num1 / num2
            elif choice == '5':
                result = num1 ** num2
            elif choice == '6':
                result = math.sqrt(num1)
            elif choice == '7':
                result = math.factorial(int(num1))
            elif choice == '8':
                result = math.sin(num1)
            elif choice == '9':
                result = math.cos(num1)
            elif choice == '10':
                if math.tan(num1) == 0:
                    print("Ошибка: тангенс не определен для угла, при котором косинус равен нулю")
                    return
                else:
                    result = math.tan(num1)

            print("Результат:", result)
        except ValueError:
            print("Ошибка: Введите корректное число")
    else:
        print("Ошибка: Неверный выбор операции")

while True:
    calculator()
    break