import csv
import os

ruta_script = os.path.dirname(__file__)
ruta_peliculas = os.path.join(ruta_script, "peliculas.csv")

from datetime import datetime
anio_actual = datetime.now().year

class Pelicula:
    def __init__(self, nombre, año, genero, duracion, puntaje):
        self.nombre = nombre
        self.año = año
        self.genero = genero
        self.duracion = duracion
        self.puntaje = puntaje

    def __str__(self):
        return self.nombre

# Leemos las películas desde un CSV y las agregamos a la lista películas.
peliculas = []
with open(ruta_peliculas, encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        p = Pelicula(
            fila["nombre"],
            int(fila["año"]),
            fila["genero"],
            int(fila["duracion"]),
            int(fila["puntaje"])
        )
        peliculas.append(p)

#Todas las películas ordenadas según su puntaje y la duración como segundo parámetro.
top_totales = sorted(peliculas, key=lambda x: (x.puntaje, x.duracion), reverse=True)

#Lista de las primeras 10 películas
top_10 = list(top_totales[0:10])

#Muestra todas las películas de la lista top_totales.
def mostrar_peliculas():
    for i, p in enumerate(peliculas, start=1):
        print(f"{i}. {p}")

def agregar_pelicula():
    print("Por favor, ingrese los siguientes datos:\n")
    nombre = input("Nombre: ")
    while True:
        try: 
            anio = int(input("Año: ").strip())
            if 1894 < anio < datetime.now().year:
                break
            else:
                print("Ese no es un año válido. Escríbalo nuevamente.\n")
        except ValueError:
            print("Eso no es un número válido. Inténtelo nuevamente.\n")
    genero = input("Género: ")
    while True:
        try: 
            duracion = int(input("Duración (en minutos): "))
            break
        except ValueError:
            print("Eso no es un número válido. Inténtelo nuevamente.\n")
    while True:
        try:
            puntaje = int(input("Puntaje (del 1 al 10): "))
            if 1 <= puntaje <= 10:
                break
            else:
                print("Debe ingresar un número del 1 al 10. Inténtelo nuevamente.\n")
        except ValueError:
            print("Eso no es un número válido. Inténtelo nuevamente.\n")

    peli = Pelicula(nombre, anio, genero, duracion, puntaje)
    peliculas.append(peli)

def borrar_pelicula():
        peli = input("Escriba el nombre de la película que desea borrar: ").lower().strip()
        for p in peliculas:
            if p.nombre.lower() == peli:
                peliculas.remove(p)
                print("La película fue borrada correctamente")
                break
        else:
            print("La película ingresada no se encuentra en la lista")

#Imprime los detalles de una película definida por el usuario.
def mostrar_detalles():
    peli = input("Escriba el nombre de la película para ver sus detalles: ").lower().strip()
    for p in peliculas:
        encontrada = False
        if p.nombre.lower() == peli:
            encontrada = True
            print()
            print(f"Año: {p.año} ")
            print(f"Género: {p.genero}")
            print(f"Duración: {p.duracion}")
            print(f"Puntaje: {p.puntaje}")
            break
    if not encontrada:
        print("La película ingresada no se encuentra en la lista")

def mostrar_top10():
    for i, p in enumerate(top_10, start=1):
        print(f"{i}. {p}")

#Hace el conteo de los géneros de cada película del top 10 e imprime el/los más repetido/s.
def contar_generos():
    conteo_generos = {}
    for pelicula in top_10:
        if pelicula.genero in conteo_generos:
            conteo_generos[pelicula.genero] += 1
        else:
            conteo_generos[pelicula.genero] = 1

    genero_mas_repetido = max(conteo_generos, key=conteo_generos.get)

    generos_ganadores = []

    numero_maximo_genero = max(conteo_generos.values())

    for genero, cantidad in conteo_generos.items():
        if cantidad == numero_maximo_genero:
            generos_ganadores.append(genero)
        
    if len(generos_ganadores) == 1:
        print("Tu género preferido es:")
        print(genero_mas_repetido)
    else:
        print("Tus géneros preferidos son:")
        for g in generos_ganadores:
          print(g)


#Imprime el promedio de las duraciones de las películas del top 10.
def promediar_duracion():
    suma = 0
    for p in top_10:
        suma += p.duracion
    promedio_duracion = int(suma / len(top_10))

    print("El promedio de duraciones de tus películas favoritas es:")
    print(f"{promedio_duracion} minutos")

#Imprime el promedio de la antigüedad de las películas del top 10.
def promediar_antiguedad():
    restos_año = 0
    for p in top_10:
        restos_año += (2025 - p.año)
    promedio_antiguedad = int(restos_año / len(top_10))
    print(f"El promedio de años de antiguedad de las películas de tu top 10 es: {promedio_antiguedad} años")

def guardar_en_csv():
    with open(ruta_peliculas, "w", newline="", encoding="utf-8") as p:
        campos = ["nombre", "año", "genero", "duracion", "puntaje"]
        escritor = csv.DictWriter(p, fieldnames=campos)
        escritor.writeheader()
        for p in peliculas:
            escritor.writerow({
                "nombre": p.nombre,
                "año": str(p.año),
                "genero": p.genero,
                "duracion": str(p.duracion),
                "puntaje": str(p.puntaje)
            })        

#Menú principal
while True:
    print("Escriba el número de la opción deseada:\n")
    print("1. Ver el listado completo de películas")
    print("2. Agregar una película")
    print("3. Borrar una película")
    print("4. Ver detalles de una película")
    print("5. Ver el top 10 de tus películas favoritas y sus estadísticas")
    print("6. Guardar los cambios y salir del programa")
    print("7. Salir del programa sin guardar los cambios")
    opcion = input()

    match opcion:
        case "1":
            print()
            mostrar_peliculas()
            print()
            print("-----------------------------")
            print()
            input("Presione Enter para volver al menú principal")
        case "2":
            agregar_pelicula()
            print()
            print("La película fue agregada correctamente")
            input("Presione Enter para volver al menú principal\n\n")
        case "3":
            borrar_pelicula()
            print()
            input("Presione Enter para volver al menú principal\n\n")
        case "4":
            print()
            mostrar_detalles()
            print()
            print("--------------------")
            print()
            input("Presione Enter para volver al menú principal.\n\n")
        case "5":
            print()
            print("Tus 10 películas favoritas son:\n\n")
            mostrar_top10()
            print()
            contar_generos()
            print()
            promediar_duracion()
            print()
            promediar_antiguedad()
            print()
            input("Presione Enter para volver al menú principal.")
        case "6":
            print()
            guardar_en_csv()
            print("Los cambios fueron guardados correctamente.")
            input("Presione Enter para salir")
            break

        case "7":
            print()
            input("Presione Enter para salir.")
            break
        case _:
            print()
            print("Debe ingresar un número del 1 al 7\n")     
