"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from base_datos import client

# se obtiene la colección general (base de datos)

db = client.solucion03
# se obtiene la colección que almacenará la información, para el ejemplo
# se llama equipos
coleccion = db.equipos

# conjunto de datos a guardar en la colección
# importante, aquí se usa la estructura de Python denominada diccionario
# proceso que agrega un solo documento

lista_equipos = []
bandera = True
while bandera:
    nombre = input("Ingrese el nombre del equipo:   ")
    siglas = input("Ingrese las siglas del equipo:  ")
    seguidores = int(input("Ingrese el número de seguidores:    "))
    campeonatos = int(input("Ingrese el número de campeonatos:  "))
    estadio = input("Ingrese el nombre del estadio: ")
    # con la información ingresada por teclado
    # se crea un diccionario
    equipo = {"nombre": nombre, "siglas": siglas, "seguidores": seguidores, \
    "campeonatos": campeonatos, "nombre_estadio": estadio}
    # se lo agrega a la lista
    lista_equipos.append(equipo)
    salida = input("Desea salir del ciclo, ingres la letra (f): ")
    if salida == 'f':
        bandera = False

print("fin de ingreso de información\n")
# proceso que agrega una lista de documentos
coleccion.insert_many(lista_equipos)

# se usa método find, a partir de la colección
print("Presentación de información de la base de datos")
informacion = coleccion.find()
for registro in informacion:
    print("Nombre: %s - Siglas:%s - Seguidores: %d - Campeonatos: %d"
    "- Estadio: %s" % (registro['nombre'], registro['siglas'],
    registro['seguidores'], registro['campeonatos'], registro['nombre_estadio']))
