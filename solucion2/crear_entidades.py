from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
# se importa el engine
from base_datos import engine

# se crea la clase llamada Base que permite definir las clases bajo las
# características de SQLAlchemy
Base = declarative_base()

# Se crea la una entidad llamada Equipo
class Equipo(Base):
    __tablename__ = 'miequipo' # El nombre de la entidad en sqlite
    # Se definen los atributos
    id = Column(Integer, primary_key=True) # este atributo es entero y
                                        # se lo considera como llave
                                        # primaria
    nombre = Column(String) # atributo de tipo String
    siglas = Column(String)
    seguidores = Column(Integer)
    campeonatos = Column(Integer)
    nombre_estadio = Column(String)

    def __str__(self):
        return ("Nombre: %s/ Siglas: %s/ Seguidores: %d/ Campeonatos:%d"
        "Estadio: %s") % (self.nombre, self.siglas, self.seguidores,
        self.campeonatos, self.nombre_estadio)

# Sentencia que permite crear o migrar las clases en Python al
# gestor de base de datos, expresado en el engine.
Base.metadata.create_all(engine)
