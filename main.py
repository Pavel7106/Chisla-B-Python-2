def calculate_average(numbers):
    """Функция для подсчёта среднего арифметического"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_max(numbers):
    """Поиск максимального числа"""
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def find_min(numbers):
    """Поиск минимального числа"""
    if not numbers:
        return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def filter_positive(numbers):
    """Оставляет только положительные числа"""
    return [num for num in numbers if num > 0]

def filter_negative(numbers):
    """Оставляет только отрицательные числа"""
    return [num for num in numbers if num < 0]

def main():
    test_numbers = [10, -5, 23, -1, 8, -3, 15, 0, -7, 42]
    
    print("Тестирование утилит для работы с числами")
    print(f"Исходный массив: {test_numbers}")
    print(f"Среднее значение: {calculate_average(test_numbers)}")
    print(f"Максимум: {find_max(test_numbers)}")
    print(f"Минимум: {find_min(test_numbers)}")
    print(f"Положительные: {filter_positive(test_numbers)}")
    print(f"Отрицательные: {filter_negative(test_numbers)}")

if __name__ == "__main__":
    main()
