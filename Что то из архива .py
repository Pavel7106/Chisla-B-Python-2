def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))


def min_max(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    return min_value, max_value

data = [1, 5, 9, 2, 8]
minimum, maximum = min_max(data)
print(f"Min: {minimum}, Max: {maximum}")


def find_first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
    return None

result = find_first_even([1, 3, 5, 8, 9])
print(result)


def can_access(age):
    if age >= 18:
        return "Доступ разрешён"
    return "Доступ запрещён"

print(can_access(16))
print(can_access(18))
print(can_access(21))
