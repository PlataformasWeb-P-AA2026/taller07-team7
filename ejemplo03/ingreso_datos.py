# -*- coding: utf-8 -*-
import csv
from datetime import datetime
from decimal import Decimal
from sqlalchemy.orm import sessionmaker
# Importa tus clases y el engine desde el archivo donde definiste las tablas
from clases import engine, Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega

Session = sessionmaker(bind=engine)
session = Session()

# Lista de archivos en el orden correcto de carga para respetar las FK
archivos = [
    ('01_departamento.csv', Departamento),
    ('02_instructor.csv', Instructor),
    ('04_estudiante.csv', Estudiante),
    ('03_curso.csv', Curso),
    ('05_inscripcion.csv', Inscripcion),
    ('06_tarea.csv', Tarea),
    ('07_entrega.csv', Entrega)
]

def cargar_datos():
    for archivo, modelo in archivos:
        print(f"Cargando {archivo}...")
        with open(archivo, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)  # Saltar encabezados
            
            for row in reader:
                if modelo == Departamento:
                    registro = Departamento(id=int(row[0]), nombre=row[1])
                elif modelo == Instructor:
                    registro = Instructor(id=int(row[0]), nombre=row[1])
                elif modelo == Estudiante:
                    registro = Estudiante(id=int(row[0]), nombre=row[1])
                elif modelo == Curso:
                    registro = Curso(id=int(row[0]), titulo=row[1], departamento_id=int(row[2]), instructor_id=int(row[3]))
                elif modelo == Inscripcion:
                    registro = Inscripcion(estudiante_id=int(row[0]), curso_id=int(row[1]), fecha_inscripcion=datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S'))
                elif modelo == Tarea:
                    registro = Tarea(id=int(row[0]), curso_id=int(row[1]), titulo=row[2], fecha_entrega=datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S'))
                elif modelo == Entrega:
                    registro = Entrega(id=int(row[0]), tarea_id=int(row[1]), estudiante_id=int(row[2]), fecha_envio=datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S'), calificacion=Decimal(row[4]))
                
                session.add(registro)
        print(f"Finalizado: {modelo.__tablename__}")

    session.commit()
    print("¡Base de datos poblada exitosamente!")
    session.close()

if __name__ == "__main__":
    cargar_datos()