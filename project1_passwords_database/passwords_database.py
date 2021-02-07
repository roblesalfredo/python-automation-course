"""
Como administrador de una base de datos de un sitio web e-commerce deberás construir una interfaz que pueda ser utilizada por el usuario para que pueda gestionar su contraseña de acceso al mismo. La base de datos consistirá en un fichero CSV que será almacenado en el que servidor y que constará únicamente de dos columnas: el usuario y el valor hash de la contraseña. El programa principal deberá mostrar al usuario un menú con varias opciones posibles:

    1. Generar contraseña aleatoria. Al seleccionar esta opción, se le preguntará al usuario en primer lugar, de cuántos caracteres quiere generar la contraseña. A continuación, se le preguntará al usuario cuántos números como mínimo deberá contener la contraseña e igualmente se realizará para los caracteres especiales. Se deberá mostrar por pantalla la contraseña generada y preguntar al usuario si quiere generar otra o no. Por último, el usuario será preguntado si se desea copiar la contraseña al portapapeles.
    Puede ser de ayuda conocer las funciones chr() y ord().
    
    2. Login en sitio web. El usuario deberá introducir sus credenciales de acceso para el sitio web. El programa deberá comparar si el hash de la contraseña introducida corresponde con el valor hash almacenado en la base de datos. El programa devolverá si el login ha sido correcto o si los credenciales no son los correctos.
    
    3. Cambio de contraseña. El usuario deberá introducir la contraseña actual y, a continuación, ser preguntado por la nueva contraseña. Finalmente, el hash de la nueva contraseña será actualizado en la base de datos y se deberá informar al usuario.

    4. Registrarse en el sitio web. El usuario será preguntado por el usuario y la contraseña que querrá utilizar en el sitio web. El resultado será escrito en la base de datos.

El usuario será continuamente preguntado para introducir una de las opciones anteriores hasta que decida salir del programa.
"""
import os
import random
import hashlib

MENU_LENGTH = 75
DATABASE_FILEPATH = "database.csv"

def generar_contraseña(n, nc, nn):
    password = ["" for i in range(n)]
    # Generar caracteres
    # Rango ASCII: 33 a 47, 58 a 64 y 91 a 95
    rango_caracteres = [i for i in range(33, 48)] + [i for i in range(58, 65)] + [i for i in range(91, 96)]
    caracteres_completados = 0
    while caracteres_completados < nc:
        pos = random.randint(0, n - 1)
        if password[pos] == "":
            aleatorio = chr(random.choice(rango_caracteres))
            password[pos] = aleatorio
            caracteres_completados += 1
    # Generar números
    # Rango ASCII: 48 a 57
    rango_caracteres = [i for i in range(48, 58)]
    numeros_completados = 0
    while numeros_completados < nn:
        pos = random.randint(0, n - 1)
        if password[pos] == "":
            aleatorio = chr(random.choice(rango_caracteres))
            password[pos] = aleatorio
            numeros_completados += 1
    # Generar resto de caracteres
    # Rango ASCII: 65 a 90 y 97 a 122
    rango_caracteres = [i for i in range(65, 90)] + [i for i in range(97, 122)]
    for i in range(n):
        if password[i] == "":
            aleatorio = chr(random.choice(rango_caracteres))
            password[i] = aleatorio
    return "".join(password)

def leer_database(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        database_raw = f.read()
    database_split = [tuple(i.split(",")) for i in database_raw.split("\n") if len(i) > 0]
    database = {database_split[r][0]: database_split[r][1] for r in range(1, len(database_split))}
    return database

def escribir_database(filepath, database_json):
    database_raw = "usuario,contraseña\n"
    for k, v in database_json.items():
        database_raw += k + "," + v + "\n"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(database_raw)


# Main
if __name__ == '__main__':
    while True:
        print("\n")
        print("*" * MENU_LENGTH)
        print("MENÚ".center(MENU_LENGTH))
        print("*" * MENU_LENGTH)
        print("Seleccione una de las opciones disponibles:\n1. Generar contraseña aleatoria\n2. Iniciar sesión\n3. Cambiar la contraseña\n4. Crear nuevo registro\n5. Salir")
        print("*" * MENU_LENGTH)
        option = input("Opción: ")

        if option == "1":
            try:
                n = int(input("Introduce la longitud de la contraseña: "))
            except:
                print("Valor no válido. Inténtelo otra vez")
            else:
                try:
                    n_char = int(input("Introduce el número mínimo de caracteres: "))
                except:
                    print("Valor no válido. Inténtelo otra vez")
                else:
                    try:
                        n_num = int(input("Introduce el número mínimo de caracteres numéricos: "))
                    except:
                        print("Valor no válido. Inténtelo otra vez")
                    else:
                        if n_char + n_num <= n:
                            print("Contraseña:", generar_contraseña(n, n_char, n_num))
                            ans = input("¿Desea hacer otra operación? (s/n): ")
                            if ans.lower() == 'n':
                                break
                        else:
                            print("No se puede generar la contraseña deseada. Inténtelo otra vez")
        
        elif option == "2":
            usuario = input("Introduce el usuario: ")
            database = leer_database(DATABASE_FILEPATH)
            if usuario in database:
                password = input("Introduce la contraseña: ")
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                if hashed_password == database[usuario]:
                    print("Sesión iniciada correctamente\n")
                else:
                    print("Los credenciales no son correctos. Inténtelo otra vez")
                ans = input("¿Desea hacer otra operación? (s/n): ")
                if ans.lower() == 'n':
                    break
            else:
                print("El usuario no se encuentra en la base de datos. Cree un nuevo registro.")

        elif option == "3":
            usuario = input("Introduce el usuario: ")
            database = leer_database(DATABASE_FILEPATH)
            if usuario in database:
                password = input("Introduce la contraseña: ")
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                if hashed_password == database[usuario]:
                    new_password = input("Introduce la nueva contraseña: ")
                    hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()
                    database[usuario] = hashed_new_password
                    escribir_database(DATABASE_FILEPATH, database)
                    print("La contraseña fue cambiada correctamente")
                else:
                    print("Los credenciales no son correctos. Inténtelo otra vez")
                ans = input("¿Desea hacer otra operación? (s/n): ")
                if ans.lower() == 'n':
                    break
            else:
                print("El usuario no se encuentra en la base de datos. Cree un nuevo registro.")
                
        elif option == "4":
            usuario = input("Introduce el nuevo usuario: ")
            database = leer_database(DATABASE_FILEPATH)
            if usuario not in database:
                password = input("Introduce la contraseña: ")
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                database[usuario] = hashed_password
                escribir_database(DATABASE_FILEPATH, database)
                print("El registro fue creado correctamente")
                ans = input("¿Desea hacer otra operación? (s/n): ")
                if ans.lower() == 'n':
                    break
            else:
                print("El usuario ya se encuentra en la base de datos")

        elif option == "5":
            break