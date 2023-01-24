from sqlalchemy.orm import sessionmaker
# se importa la clase(s) del
# archivo crear_entidades
from crear_entidades import Equipo
# se importa el engine
from base_datos import engine

# Se crea una clase llamada Sessión,
# desde el generador de clases de SQLAlchemy
# sessionmaker.
Session = sessionmaker(bind=engine) # Se usa el engine
# Importante, se crea un objeto llamado session
# de tipo Session, que permite: permitir guardar, eliminar,
# actualizar y generar consultas a la base de datos.
session = Session()

lista_equipos = []
bandera = True
while bandera:
    nombre = input("Ingrese el nombre del equipo:   ")
    siglas = input("Ingrese las siglas del equipo:  ")
    seguidores = int(input("Ingrese el número de seguidores:    "))
    campeonatos = int(input("Ingrese el número de campeonatos:  "))
    estadio = input("Ingrese el nombre del estadio: ")
    # con la información ingresada por teclado
    # se crea un objeto de tipo equipo
    equipo = Equipo(nombre=nombre, siglas=siglas, seguidores=seguidores, \
    campeonatos=campeonatos, nombre_estadio=estadio)
    # se lo agrega a la lista
    lista_equipos.append(equipo)
    salida = input("Desea salir del ciclo, ingres la letra (f): ")
    if salida == 'f':
        bandera = False

print("fin de ingreso de información\n")

for l in lista_equipos:
    # cada objeto que se itera de la lista equipos
    # se lo agrega a la sesión
    session.add(l)

# se necesita confirmar los cambios que existan en la sessión
# se usar commit
session.commit()

# Obtener todos los registros de la entidad Equipo.
# Se hace uso del método query.
# all, significa que se obtiene todos los registros
informacion = session.query(Equipo).all()
# La variable informacion, tendrá un listado de objetos de tipo Equipo

# se realiza un proceso iterativo para presentar la información
# de cada objeto.
print("Presentación de información de la base de datos")
for l in informacion:
    print(l)
