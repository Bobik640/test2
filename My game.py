def add(x, y):
    """Функция для сложения двух чисел."""
    return x + y

def subtract(x, y):
    """Функция для вычитания двух чисел."""
    return x - y

def multiply(x, y):
    """Функция для умножения двух чисел."""
    return x * y

def divide(x, y):
    """Функция для деления двух чисел."""
    if y == 0:
        raise ValueError("Ошибка: Деление на ноль невозможно.")
    return x / y

def get_numbers_and_operation():
    """Функция для получения чисел и операции от пользователя."""
    operation = input("Введите операцию (+, -, *, /) или 'exit' для выхода: ")
    if operation.lower() == 'exit':
        return None, None, operation
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    return num1, num2, operation

def calculate(num1, num2, operation):
    """Функция для выполнения расчета в зависимости от операции."""
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)
    else:
        raise ValueError("Ошибка: Некорректная операция.")

def main():
    """Основная функция программы."""
    print("Добро пожаловать в калькулятор! Введите 'exit' в любой момент, чтобы выйти.")
    while True:
        try:
            num1, num2, operation = get_numbers_and_operation()
            if operation == 'exit':
                print("Выход из программы.")
                break
            result = calculate(num1, num2, operation)
            print(f"Результат: {result}")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"Произошла ошибка: {e}")

# Запуск программы
if __name__ == "__main__":
    main()
