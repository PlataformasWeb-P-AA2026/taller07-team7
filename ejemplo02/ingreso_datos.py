# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
from genera_tablas import engine, Club, Jugador

Session = sessionmaker(bind=engine)
session = Session()

print("Iniciando la carga de datos (usando ID de club)...")

# 1. Procesar Clubes


# 2. Procesar Jugadores (Usando ID de club)
# Se asume formato: ID_Club;Posicion;Dorsal;NombreJugador
try:
    with open('data/datos_jugadores.txt', 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if not linea: continue
            
            partes = linea.split(';')
            nombre_club_txt = partes[0].strip() # 'Barcelona'
            posicion = partes[1].strip()
            dorsal = int(partes[2].strip())
            nombre_jugador = partes[3].strip()
            
            # Buscamos el objeto Club cuyo nombre coincida
            club_bd = session.query(Club).filter_by(nombre=nombre_club_txt).first()
            
            if club_bd:
                # Usamos el ID del club encontrado (club_bd.id)
                nuevo_jugador = Jugador(
                    nombre=nombre_jugador,
                    dorsal=dorsal,
                    posicion=posicion,
                    club_id=club_bd.id
                )
                session.add(nuevo_jugador)
                print(f"Insertado: {nombre_jugador} con ID Club: {club_bd.id}")
            else:
                print(f"Error: No se encontró el club '{nombre_club_txt}' en la base de datos.")
        
        session.commit()
        print("Carga exitosa.")

except ValueError as ve:
    print(f"Error de formato en el archivo: {ve}")
    session.rollback()
except Exception as e:
    print(f"Error inesperado: {e}")
    session.rollback()
finally:
    session.close()