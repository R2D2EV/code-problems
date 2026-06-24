"""
Ejercicio 8.1 – Completa la línea faltante para que la función retorne los índices correctos.
"""

def two_sum(nums, target):
    seen = {}

    for i, x in enumerate(nums):
        need = target - x
        print(i)
        if need in seen:
            return [seen[need], i]

        seen[x] = i
    

if __name__ == "__main__":
    nums = [6, 1, 5, 4]
    print(two_sum(nums, 5))