"""
Escribir un programa para gestionar las citas de una consulta médica. La base de datos de citas debe estar en un fichero de nombre citas.csv. Cada cita contendrá los campos dni, mes, dia, hora y especialidad. No es necesario que la primera fila del csv contenga los nombres de los campos. El programa debe incluir las siguientes funciones:

    - Una función que permita generar el fichero y añadir una cita a la base de datos.
    - Una función que reciba un dni y devuelva una lista con las citas de ese paciente.
    - Una función para eliminar las citas anteriores a una fecha dada.
"""

import os


DATABASE_FILEPATH = "citas.csv"


def añadir_cita(dni, mes, dia, hora, especialidad, database_filepath=DATABASE_FILEPATH):
    """Añadir cita a la agenda

    Parámetros:
        dni: string
        mes: string con el número del mes
        dia: string con el día en formato numérico
        hora: string con formato hh:mm
        especialidad: string
    """
    # Comprobar que la base de datos existe
    if not os.path.isfile(database_filepath):
        f = open(database_filepath, 'x')
        f.close()

    with open(database_filepath, 'a', encoding='utf-8') as f:
        cita = dni + "," + mes + "," + dia + "," + hora + "," + especialidad + "\n"
        f.write(cita)


def listar_citas(dni, database_filepath=DATABASE_FILEPATH):
    with open(database_filepath, 'r', encoding='utf-8') as f:
        citas = f.readlines()
        listado = []
        for cita in citas:
            dni_cita = cita.split(",")[0]
            if dni_cita == dni:
                listado.append(cita)
    return listado


def eliminar_citas(mes, dia, database_filepath=DATABASE_FILEPATH):
    with open(database_filepath, 'r', encoding='utf-8') as f:
        citas = f.readlines()

    listado = []
    for cita in citas:
        mes_dia_cita = cita.split(",")[1] + cita.split(",")[2]
        if mes_dia_cita > mes + dia:
            listado.append(cita)

    with open(database_filepath, 'w', encoding='utf-8') as f:
        f.write("".join(listado))


# Main
# añadir_cita("01234567", "3", "20", "15:00", "Traumatólogo")
listado_citas = listar_citas("345345354")
print(listado_citas)
eliminar_citas("3", "2")