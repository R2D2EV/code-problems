"""
Completa la línea faltante para construir el entero invertido sin strings.
"""

def reverse_int(x):
    sign = 1
    if x < 0:
        sign = -1
        x = -x
    out = 0
    while x > 0:
        a = x % 10
        out = out * 10 + a
        x //= 10
    return sign * out

print(reverse_int(21))