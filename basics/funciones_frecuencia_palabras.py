"""
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

text = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
"""

def frecuencia_palabras(texto):
    dic_frec = {}
    print(texto.split())
    for palabra in texto.split():
        print(palabra)
        if palabra in dic_frec.keys():
            dic_frec[palabra] += 1
            print("Frecuencia +1")
        else:
            dic_frec[palabra] = 1
            print("Añadida nueva palabra al diccionario")
        print(dic_frec)
    return dic_frec

frecuencia_palabras("Como quieres quieres")