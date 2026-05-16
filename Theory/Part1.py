# =========================================
# VARIABLES EN PYTHON
# =========================================

# Asignación básica
nombre = "Arturo"
edad = 29
altura = 1.75

# Convenciones:
# - snake_case para variables
# - nombres descriptivos
total_usuarios_activos = 100

# Python es dinámico (no necesitas declarar tipo)
x = 10
x = "ahora soy texto"

# =========================================
# ASIGNACIÓN MÚLTIPLE
# =========================================

a, b, c = 1, 2, 3

# Intercambio de valores
a, b = b, a

# =========================================
# TIPOS DE DATOS
# =========================================

# Strings
texto = "Hola mundo"

# Números
entero = 10
flotante = 3.14

# Colecciones
lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
diccionario = {"nombre": "Arturo", "edad": 29}

# =========================================
# CONVERSIÓN DE TIPOS
# =========================================

numero = "10"
numero_int = int(numero)
numero_float = float(numero)

# =========================================
# STRINGS AVANZADOS
# =========================================

# Comillas
texto1 = "Hola"
texto2 = 'Hola'
texto_multilinea = """Esto es
un texto
de varias líneas"""

# Búsqueda
"Hola" in texto_multilinea  # True o False

# =========================================
# SLICING, REPLACE, SPLIT
# =========================================

texto = "Python es genial"

# slicing
print(texto[0:6])  # Python

# replace
nuevo = texto.replace("genial", "increíble")

# split
palabras = texto.split(" ")

# =========================================
# BOOLEANOS
# =========================================

verdadero = True
falso = False

# casting a bool
bool(0)       # False
bool(1)       # True
bool("")      # False
bool("hola")  # True

# =========================================
# NONE
# =========================================

valor = None

# =========================================
# OPERADORES ARITMÉTICOS
# =========================================

a = 10
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b
potencia = a ** b

# =========================================
# OPERADORES DE ASIGNACIÓN
# =========================================

x = 10
x += 5  # x = x + 5

# Walrus operator (:=)
if (n := 5) > 3:
    print(n)

# =========================================
# OPERADORES LÓGICOS
# =========================================

True and False
True or False
not True

# =========================================
# CONDICIONALES
# =========================================

edad = 18

if edad >= 18:
    print("Mayor de edad")
elif edad == 17:
    print("Casi adulto")
else:
    print("Menor de edad")

# pass (placeholder)
if True:
    pass

# =========================================
# MATCH (Python 3.10+)
# =========================================

dia = "lunes"

match dia:
    case "lunes":
        print("Inicio de semana")
    case _:
        print("Otro día")

# =========================================
# WHILE
# =========================================

contador = 0

while contador < 5:
    contador += 1
    
    if contador == 3:
        continue  # salta iteración
    
    if contador == 4:
        break  # rompe el ciclo
    
    print(contador)

# =========================================
# FOR
# =========================================

for i in range(5):
    print(i)

for item in [1, 2, 3]:
    print(item)

# =========================================
# LISTAS
# =========================================

lista = [1, 2, 3]

lista.append(4)
lista.remove(2)
lista[0] = 10

# =========================================
# TUPLAS
# =========================================

tupla = (1, 2, 3)

# tupla[0] = 10  # ERROR (inmutable)

# =========================================
# CONJUNTOS (SETS)
# =========================================

conjunto = {1, 2, 3}

conjunto.add(4)
conjunto.remove(2)

# Operaciones
a = {1, 2, 3}
b = {3, 4, 5}

union = a | b
interseccion = a & b

# =========================================
# DICCIONARIOS
# =========================================

persona = {
    "nombre": "Arturo",
    "edad": 29
}

# acceso
print(persona["nombre"])

# agregar/modificar
persona["ciudad"] = "CDMX"

# =========================================
# FUNCIONES
# =========================================

def saludar(nombre):
    return f"Hola {nombre}"

print(saludar("Arturo"))

# =========================================
# LAMBDA
# =========================================

suma = lambda a, b: a + b

print(suma(2, 3))

# =========================================
# MÓDULOS
# =========================================

# archivo: mi_modulo.py
# def funcion():
#     print("Hola")

# en otro archivo:
# import mi_modulo
# mi_modulo.funcion()

# =========================================
# MANEJO DE ERRORES
# =========================================

try:
    x = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero")
finally:
    print("Esto siempre se ejecuta")

# =========================================
# ARCHIVOS
# =========================================

# escritura
with open("archivo.txt", "w") as f:
    f.write("Hola mundo")

# lectura
with open("archivo.txt", "r") as f:
    contenido = f.read()
    print(contenido)