"""
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

text = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
"""

from collections import Counter


def frecuencia_palabras_counter(texto):
    c = Counter(texto.split())
    return dict(c)


def palabra_mas_repetida_counter(diccionario_palabras):
    c = Counter(diccionario_palabras)
    return c.most_common(1)[0]


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


def palabra_mas_repetida(diccionario_palabras):
    frecuencia_max = 0
    for t in diccionario_palabras.items():
        if t[1] > frecuencia_max:
            tupla_max = t
            frecuencia_max = t[1]
    return tupla_max


# Main
mi_diccionario = frecuencia_palabras("Como quieres quieres mesa quieres")
tupla_max = palabra_mas_repetida(mi_diccionario)
print(f"La palabra más repetida es '{tupla_max[0]}' con frecuencia {tupla_max[1]}.")

print("\nUsando Counter")
mi_diccionario = frecuencia_palabras_counter("Como quieres quieres mesa quieres")
tupla_max = palabra_mas_repetida_counter(mi_diccionario)
print(f"La palabra más repetida es '{tupla_max[0]}' con frecuencia {tupla_max[1]}.")