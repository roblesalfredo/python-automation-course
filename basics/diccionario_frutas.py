"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70
"""

# Imports
import os
import sys


# Funciones
def iniciar_tabla_precios():
    tabla_precios = {}
    frutas = ["Plátano", "Manzana", "Pera", "Naranja"]
    precios = [1.35, 0.8, 0.85, 0.7]
    for key, value in zip(frutas, precios):
        tabla_precios[key] = value

    return tabla_precios

    
def incluir_fruta(fruta, kilos):
    precio = precios_frutas[fruta]
    precio_total = precio * kilos
    print(f"El precio total de {kilos} kg de {fruta.lower()}s es: {precio_total} €.")


# Main
precios_frutas = iniciar_tabla_precios()
print(precios_frutas)
fruta = input("Introduce el nombre de la fruta: ").capitalize()
if fruta in list(precios_frutas.keys()):
    kilos = float(input("Introduce el número de kilos: "))
    incluir_fruta(fruta, kilos)
else:
    print("La fruta no se encuentra en el diccionario")
