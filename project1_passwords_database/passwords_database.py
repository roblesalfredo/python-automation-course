"""
Como administrador de una base de datos de un sitio web e-commerce deberás construir una interfaz que pueda ser utilizada por el usuario para que pueda gestionar su contraseña de acceso al mismo. La base de datos consistirá en un fichero CSV que será almacenado en el que servidor y que constará únicamente de dos columnas: el usuario y el valor hash de la contraseña. El programa principal deberá mostrar al usuario un menú con varias opciones posibles:

    1. Generar contraseña aleatoria. Al seleccionar esta opción, se le preguntará al usuario en primer lugar, de cuántos caracteres quiere generar la contraseña. A continuación, se le preguntará al usuario cuántos números como mínimo deberá contener la contraseña e igualmente se realizará para los caracteres especiales. Se deberá mostrar por pantalla la contraseña generada y preguntar al usuario si quiere generar otra o no. Por último, el usuario será preguntado si se desea copiar la contraseña al portapapeles.
    Puede ser de ayuda conocer las funciones chr() y ord().
    
    2. Login en sitio web. El usuario deberá introducir sus credenciales de acceso para el sitio web. El programa deberá comparar si el hash de la contraseña introducida corresponde con el valor hash almacenado en la base de datos. El programa devolverá si el login ha sido correcto o si los credenciales no son los correctos.
    
    3. Cambio de contraseña. El usuario deberá introducir la contraseña actual y, a continuación, ser preguntado por la nueva contraseña. Finalmente, el hash de la nueva contraseña será actualizado en la base de datos y se deberá informar al usuario.

El usuario será continuamente preguntado para introducir una de las opciones anteriores hasta que decida salir del programa.
"""