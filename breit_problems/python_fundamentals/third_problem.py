"""
Ejercicio 7.3 – ¿Por qué este código falla lógicamente?
"""
def f(nums):
total = 0
for x in nums:
if x > 0:
total += x
return total