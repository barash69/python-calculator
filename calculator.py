print("Калькулятор")

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choice = input("Выберите действие: ")

if choice == "1":
    print("Результат:", a + b)
elif choice == "2":
    print("Результат:", a - b)
elif choice == "3":
    print("Результат:", a * b)
elif choice == "4":
    if b != 0:
        print("Результат:", a / b)
    else:
        print("Ошибка: деление на ноль")
else:
    print("Неверное действие")
