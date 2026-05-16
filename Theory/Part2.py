# =========================================
# PEP 8 + FORMATEO (NOTAS PRÁCTICAS)
# =========================================

# Instalar Ruff (linter + formatter moderno)
# pip install ruff

# Ejecutar:
# ruff check .
# ruff format .

# Reglas básicas PEP 8:
# - snake_case para variables y funciones
# - 4 espacios de indentación
# - líneas < 79-100 caracteres
# - imports al inicio


# =========================================
# COMPREHENSIONS (LIST, DICT, SET)
# =========================================

numeros = [1, 2, 3, 4, 5]

# List comprehension
cuadrados = [n**2 for n in numeros]

# Con condición
pares = [n for n in numeros if n % 2 == 0]

# Dict comprehension
diccionario = {n: n**2 for n in numeros}

# Set comprehension
conjunto = {n % 2 for n in numeros}


# =========================================
# COMPREHENSIONS ANIDADAS
# =========================================

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

# Aplanar lista (flatten)
flat = [num for fila in matriz for num in fila]

# Filtrar múltiples condiciones
filtrado = [n for n in flat if n > 2 if n % 2 == 0]


# =========================================
# F-STRINGS
# =========================================

nombre = "Arturo"
edad = 29

mensaje = f"Hola {nombre}, tienes {edad} años"


# =========================================
# F-STRINGS AVANZADOS
# =========================================

import datetime

precio = 1234.5678

# Formato decimal
print(f"{precio:.2f}")  # 1234.57

# Separador de miles
print(f"{precio:,.2f}")  # 1,234.57

# Fecha
hoy = datetime.datetime.now()
print(f"{hoy:%Y-%m-%d}")


# =========================================
# *ARGS Y **KWARGS
# =========================================

# *args -> múltiples argumentos posicionales
def suma(*args):
    return sum(args)

print(suma(1, 2, 3, 4))


# **kwargs -> argumentos nombrados dinámicos
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Arturo", edad=29)


# =========================================
# CLIENTE API FLEXIBLE (SIMULADO)
# =========================================

def construir_url(base_url: str, **params) -> str:
    """
    Construye una URL con parámetros dinámicos.
    """
    query = "&".join(f"{k}={v}" for k, v in params.items())
    return f"{base_url}?{query}"


url = construir_url(
    "https://newsapi.org/v2/top-headlines",
    country="mx",
    category="technology"
)

print(url)


# =========================================
# EXAMPLE ARGS Y KWARGS EN PRÁCTICA

def newsapi_client(api_key, query, timeout=30, retries=3):
    return f'NewsAPI: {query} con timeout {timeout}'

def guardian_client(api_key, section, from_data, timeout=30, retries=3):
    return f'Guardian {section} desde {from_data} con timeout {timeout}'

def fetch_api_client(api_client, *args, **kwargs):
    """
    Función flexible para conectar con la API
    """

    base_config = {
        'timeout': 30,
        'retries': 3
    }

    config = {
        **base_config,
        **kwargs
    }

    api_clients = {
        "newsapi": newsapi_client,
        "guardian": guardian_client
    }

    client = api_client[api_client]

    return client(*args, **config)





# =========================================

try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Bloque finally ejecutado")


# =========================================
# EXCEPCIONES PERSONALIZADAS
# =========================================

class APIError(Exception):
    """Error personalizado para APIs"""
    pass


def obtener_datos(simular_error=False):
    if simular_error:
        raise APIError("Fallo en la API")
    return {"data": "ok"}


# =========================================
# TYPE HINTS
# =========================================

def saludar(nombre: str) -> str:
    return f"Hola {nombre}"


# Tipado en estructuras
from typing import List, Dict

def procesar_numeros(nums: List[int]) -> Dict[int, int]:
    return {n: n**2 for n in nums}


# =========================================
# DOCSTRINGS (PEP 257)
# =========================================

def multiplicar(a: int, b: int) -> int:
    """
    Multiplica dos números.

    Args:
        a (int): Primer número
        b (int): Segundo número

    Returns:
        int: Resultado de la multiplicación
    """
    return a * b


# =========================================
# ENTORNOS VIRTUALES (COMANDOS)
# =========================================

# Crear entorno
# python -m venv venv

# Activar (Mac/Linux)
# source venv/bin/activate

# Activar (Windows)
# venv\Scripts\activate

# Instalar dependencias
# pip install requests


# =========================================
# PYPROJECT + DEPENDENCIAS (IDEA)
# =========================================

# Archivo pyproject.toml (ejemplo mínimo):
"""
[project]
name = "mi_app"
version = "0.1.0"
dependencies = ["requests"]
"""


# =========================================
# MODULARIZACIÓN
# =========================================

# archivo: utils.py
# def helper():
#     pass

# archivo: main.py
# from utils import helper


# =========================================
# ENUMERATE
# =========================================

lista = ["a", "b", "c"]

for indice, valor in enumerate(lista):
    print(indice, valor)


# =========================================
# FILTER
# =========================================

numeros = [1, 2, 3, 4, 5]

pares = list(filter(lambda x: x % 2 == 0, numeros))


# =========================================
# MAP
# =========================================

# Convertir a cuadrados
cuadrados = list(map(lambda x: x**2, numeros))


# =========================================
# VARIABLES DE ENTORNO (API KEY)
# =========================================

import os

# Definir en terminal:
# export API_KEY="tu_api_key"  (Mac/Linux)
# setx API_KEY "tu_api_key"   (Windows)

api_key = os.getenv("API_KEY")

if not api_key:
    print("API_KEY no definida")


# =========================================
# EJEMPLO SIMPLE INTEGRADO (MINI APP)
# =========================================

def obtener_noticias_mock(categoria: str) -> list:
    """
    Simula obtención de noticias.
    """
    noticias = [
        {"titulo": "IA revoluciona el mundo", "categoria": "technology"},
        {"titulo": "Deportes hoy", "categoria": "sports"},
    ]
    
    return [n for n in noticias if n["categoria"] == categoria]


def imprimir_noticias(noticias: list):
    for i, noticia in enumerate(noticias, start=1):
        print(f"{i}. {noticia['titulo']}")


if __name__ == "__main__":
    try:
        categoria = "technology"
        noticias = obtener_noticias_mock(categoria)
        
        if not noticias:
            raise ValueError("No hay noticias")
        
        imprimir_noticias(noticias)
    
    except Exception as e:
        print(f"Error: {e}")