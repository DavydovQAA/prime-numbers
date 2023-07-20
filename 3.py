def prime_numbers(num):            # Проверяет является ли число простым
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def print_primes(limit):
    for num in range(2, limit + 1):
        if prime_numbers(num):
            print(num)

# Выводим простые числа до 30
print_primes(30)
