"""
Escribe una función que reciba una lista de enteros y retorne un diccionario
{valor: frecuencia}.
"""

def value_frequency(nums: list):
    frequency_dict = {}
    for num in nums:
        if str(num) not in frequency_dict:
            frequency_dict[num] = 1
        else:
            print(num)
            frequency_dict[num] += 1
    return frequency_dict


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 5, 6]
    print(value_frequency(nums))