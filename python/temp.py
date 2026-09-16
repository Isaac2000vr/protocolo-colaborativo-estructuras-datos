# -*- coding: utf-8 -*-
import random

# ============================================================
# 1. ARREGLOS (ARRAYS) - En Python se usan listas
# ============================================================

# --- 1. Declaración y creación de un arreglo ---
# Python es de tipado dinámico: no se declara el tipo, y las listas
# no tienen tamaño fijo (pueden crecer o achicarse).
arreglo = [random.randint(1, 100) for _ in range(10)]
print("Arreglo inicial:", arreglo)

# --- 2. Recorrido e impresión ---

# a) Usando bucle for clásico (con índice, similar a un for de C/Java)
print("\nRecorrido con for clásico (por índice):")
for i in range(len(arreglo)):
    print(f"Posición {i}: {arreglo[i]}")

# b) Usando for-each (en Python el for ya recorre directamente los elementos)
print("\nRecorrido con for-each:")
for valor in arreglo:
    print(valor)

# --- 3. Modificación ---

# a) Cambiar todos los valores impares por cero
for i in range(len(arreglo)):
    if arreglo[i] % 2 != 0:
        arreglo[i] = 0
print("\nArreglo tras cambiar impares por 0:", arreglo)

# b) Multiplicar todos los valores por su índice
for i in range(len(arreglo)):
    arreglo[i] = arreglo[i] * i
print("Arreglo tras multiplicar por su índice:", arreglo)

# --- 4. Búsqueda lineal ---
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # retorna la posición donde se encontró
    return -1  # no encontrado

valor_buscado = arreglo[3] if len(arreglo) > 3 else 0
posicion = busqueda_lineal(arreglo, valor_buscado)
print(f"\nBuscando el valor {valor_buscado} -> encontrado en posición: {posicion}")


# ============================================================
# 2. MATRICES (ARRAYS BIDIMENSIONALES) - lista de listas
# ============================================================

# --- 1. Declaración e inicialización ---
# Matriz 3x3 con valores del 1 al 9
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# --- 2. Recorrido ---

# a) Imprimir en forma de tabla
print("\nMatriz en forma de tabla:")
for fila in matriz:
    for valor in fila:
        print(valor, end="\t")
    print()

# b) Recorrer por columnas
print("\nRecorrido por columnas:")
filas = len(matriz)
columnas = len(matriz[0])
for c in range(columnas):
    for f in range(filas):
        print(matriz[f][c], end="\t")
    print()

# --- 3. Operaciones ---

# a) Sumar todos los elementos
suma_total = 0
for fila in matriz:
    for valor in fila:
        suma_total += valor
print(f"\nSuma de todos los elementos: {suma_total}")

# b) Intercambiar la primera fila con la última
matriz[0], matriz[-1] = matriz[-1], matriz[0]
print("\nMatriz con primera y última fila intercambiadas:")
for fila in matriz:
    print(fila)
