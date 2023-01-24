"""
    Guardar y presentar información en las entidades en la base de datos
"""
from base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute
# Se crea un proceso repetitivo para ingresar información por teclado,
# de acuerdo a las caracteríticas de la entidad Equipo
lista_equipos = []
bandera = True
while bandera:
    nombre = input("Ingrese el nombre del equipo:   ")
    siglas = input("Ingrese las siglas del equipo:  ")
    seguidores = int(input("Ingrese el número de seguidores:    "))
    campeonatos = int(input("Ingrese el número de campeonatos:  "))
    estadio = input("Ingrese el nombre del estadio: ")
    lista_equipos.append((nombre, siglas, seguidores, campeonatos, estadio))
    salida = input("Desea salir del ciclo, ingres la letra (f): ")
    if salida == 'f':
        bandera = False

print("fin de ingreso de información\n")
for l in lista_equipos:
    cadena_sql = """INSERT INTO Equipo (nombre, siglas, seguidores, \
    campeonatos, nombre_estadio) VALUES ('%s', '%s', %d, %d, '%s');""" % \
    (l[0], l[1], l[2], l[3], l[4])
    # ejecutar el SQL
    cursor.execute(cadena_sql)
    # confirmar los cambios
    conn.commit()

# hacer la consulta a la base de datos
cadena_consulta_sql = "SELECT * from Equipo"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()

# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante
print("Presentación de información de la base de datos")
for d in informacion:
    print("Nombre: %s - Siglas:%s - Seguidores: %d - Campeonatos: %d"
    "- Estadio: %s" % (d[0], d[1], d[2], d[3], d[4]))
# cerrar el enlace a la base de datos (recomendado)
cursor.close()
