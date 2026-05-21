from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from clases import Departamento, Instructor,Curso,Estudiante,Inscripcion, Tarea, Entrega

# se importa información del archivo configuracion
from config import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#* consulta4.py: Por cada curso, presentar sus tareas asociadas.

cur = session.query(Curso).join(Tarea).all()

for c in cur:
    print(f"NOMBRE CURSO: {c.titulo}" )
    for t in c.tareas:
        print(f"TAREA: {t.titulo} FECHA ENTREGA: {t.fecha_entrega}")
        print("----------------------")