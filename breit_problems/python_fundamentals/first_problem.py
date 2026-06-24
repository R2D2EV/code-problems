"""
Escribe una función que retorne la suma de los dígitos de un entero x
(puede ser negativo), sin convertir a string.
"""

def sum_digits(num: int):
    result = 0
    num = abs(num)
    for i in range(1, num + 1):
        result += i
    return result


if __name__ == "__main__":
    num_1 = 5
    print(sum_digits(num_1))
    num_2 = -5
    print(sum_digits(num_2))