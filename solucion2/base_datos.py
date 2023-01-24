"""
"""
from sqlalchemy import create_engine
# se genera en enlace al gestor de base de
# datos para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///base_solucion2.db')
