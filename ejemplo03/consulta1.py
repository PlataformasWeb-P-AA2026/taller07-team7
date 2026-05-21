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

# consulta1.py: Listas las entregas, presentar por cada entrega: nombre del estudiantes, titulo, nombre del profesor

entrega = session.query(Entrega).all()

for e in entrega:
    print(f"NOMBRE ESTUDIANTE: {e.estudiante.nombre} TITULO: {e.tarea.titulo} NOMBRE DEL PROFESOR: {e.tarea.curso.instructor.nombre}")
    print("////////////////////////////")