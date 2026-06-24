"""
Completa la condición faltante.
“pairs” es una lista de tuplas (idx_original, valor) ya ordenada por valor.
"""

def two_sum_sorted(pairs, target):
    l, r = 0, len(pairs) - 1
    while l < r:
        s = pairs[l][1] + pairs[r][1]
        if s == target:
            return [pairs[l][0], pairs[r][0]]
        elif s < target:
            l += 1
        else:
            r -= 1