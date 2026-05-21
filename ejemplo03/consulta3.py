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

# * consulta3.py: Listar las inscripciones del departamento de Ciencias de la Computación. Por cada inscripción, presentar el nombre del estudiante, el nombre del curso y el nombre del profesor

ins = session.query(Inscripcion).join(Curso).join(Departamento).join(Instructor).\
    filter(Departamento.nombre.like("Ciencias de la Computación")).all()

print("DEPARTAMENTO DE COMPUTACION")
for i in ins:
    print(f"NOMBRE ESTUDIANTE: {i.estudiante.nombre} NOMBRE DEL CURSO: {i.curso.titulo} NOMBRE PROFESOR: {i.curso.instructor.nombre}")
    print("////////////////////////////")