"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (nombre, edad (opcional), teléfono, correo electrónico) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
[
    {
        "nombre": "usuario 1"
        "email": "user1@gmail.com"
    },
    {
        "nombre":
        "email":
    }
]
"""

#Funciones
def iniciar_agenda():
    return []


def iniciar_datos_personales(agenda):
    datos_usuario = {}
    nombre = input("Introduce el nombre del usuario: ")
    datos_usuario["nombre"] = nombre
    telefono = input("Introduce el teléfono: ")
    datos_usuario["tlf"] = telefono
    email = input("Introduce el email: ")
    datos_usuario["email"] = email
    agenda.append(datos_usuario)
    print(datos_usuario)
    

#Main
mi_agenda = iniciar_agenda()
flag_condicion = 0
while not flag_condicion:
    iniciar_datos_personales(mi_agenda)
    condicion = input("¿Quieres continuar (s/n)?")
    if condicion.lower() == 'n':
        flag_condicion = 1

print(mi_agenda)