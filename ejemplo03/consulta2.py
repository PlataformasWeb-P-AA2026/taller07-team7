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

#* consulta2.py: Listar los cursos, obtener los cursos profesores en su nombre tengan la cadena "Zam"

curso = session.query(Curso).join(Instructor).filter(Instructor.nombre.like("%Zam%")).all()

for c in curso:
    print(f"TITULO DEL CURSO: {c.titulo} NOMBRE DEL INSTRUCTOR: {c.instructor.nombre}")