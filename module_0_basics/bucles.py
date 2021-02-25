"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""

try:
    n = abs(int(input("Introduce un número entero positivo: ")))
except:
    print("El número no es entero positivo.")

output = ""
for i in range(n, -1, -1):
    output = output + str(i) + ", "

print("Primera solución: ",output)


print("\nSegunda solución:")

for i in range(n, -1, -1):
    print(i, end=', ')


"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
"""

frase = input("\n\nIntroduce una frase: ")
letra = input("Introduce una letra: ")

contador = 0
for i in frase.lower():
    if letra.lower() == i:
        contador += 1

print(f"El número de veces que aparece '{letra.lower()}' en la frase '{frase}' es {contador}.")