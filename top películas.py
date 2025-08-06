class Pelicula:
    def __init__(self, nombre, año, genero, duracion, puntaje):
        self.nombre = nombre
        self.año = año
        self.genero = genero
        self.duracion = duracion
        self.puntaje = puntaje
    def __str__(self):
        return self.nombre

P1 = Pelicula("Pequeña miss Sunshine", 2006, "Comedia", 101, 8)
P2 = Pelicula("El bebé de Rosemary", 1968, "Terror", 136, 9)
P3 = Pelicula("El aprendiz", 2024, "Drama", 122, 7)
P4 = Pelicula("El sutil arte de que te importe un carajo", 2022, "Documental", 97, 8)
P5 = Pelicula("Juventud", 2015, "Drama", 118, 7)
P6 = Pelicula("Fue la mano de dios", 2021, "Drama", 130, 8)
P7 = Pelicula("Animales Nocturnos", 2016, "Thriller", 115, 7)
P8 = Pelicula("Los infiltrados", 2006, "Thriller", 149, 6)
P9 = Pelicula("Anatomía de una caída", 2023, "Drama", 150, 9)
P10 = Pelicula("Todo sobre mi madre", 1999, "Drama", 105, 6)
P11 = Pelicula("Vidas pasadas", 2023, "Romance", 105, 8)
P12 = Pelicula("La mejor oferta", 2013, "Intriga", 131, 7)
P13 = Pelicula("Poderosa afrodita", 1995, "Comedia", 95, 6)
P14 = Pelicula("Retrato de una mujer en llamas", 2019, "Drama", 120, 8)
P15 = Pelicula("Mujeres al borde de un ataque de nervios", 1988, "Comedia", 89, 8)
P16 = Pelicula("Aftersun", 2022, "Drama", 98, 7)
P17 = Pelicula("Atracción fatal", 1987, "Intriga", 119, 7)
P18 = Pelicula("El observador", 2018, "Intriga", 91, 4)
P19 = Pelicula("América X", 1998, "Drama", 119, 9)
P20 = Pelicula("Vicky Cristina Barcelona", 2008, "Comedia", 96, 8)
P21 = Pelicula("La última noche de Boris Grushenko", 1975, "Comedia", 82, 9)
P22 = Pelicula("Alien: Romulus", 2024, "Ciencia ficción", 119, 7)
P23 = Pelicula("Sueños de libertad", 1994, "Drama", 142, 9)
P24 = Pelicula("La asistente", 2019, "Drama", 87, 5)
P25 = Pelicula("Godzilla y Kong: El nuevo imperio", 2024, "Acción", 115, 4)
P26 = Pelicula("La langosta", 2015, "Ciencia ficción", 118, 6)
P27 = Pelicula("El artista", 2011, "Comedia", 100, 7)
P28 = Pelicula("La Sociedad de la nieve", 2023, "Aventuras", 144, 8)
P29 = Pelicula("El exorcista", 1973, "Terror", 121, 7)
P30 = Pelicula("Ha vuelto", 2015, "Comedia", 116, 8)
P31 = Pelicula("Magnolia", 1999, "Drama", 188, 10)
P32 = Pelicula("Después del casamiento", 2006, "Drama", 122, 8)
P33 = Pelicula("Tráfico", 2000, "Thriller", 142, 7)
P34 = Pelicula("Argo", 2012, "Thriller", 120, 7)
P35 = Pelicula("Dune", 2021, "Ciencia ficción", 155, 6)
P36 = Pelicula("Batman inicia", 2005, "Thriller", 140, 5)
P37 = Pelicula("Amarcord", 1973, "Comedia", 127, 5)
P38 = Pelicula("Oppenheimer", 2023, "Drama", 180, 8)
P39 = Pelicula("Todo en todas partes al mismo tiempo", 2022, "Comedia",139, 6)
P40 = Pelicula("El triángulo de la tristeza", 2022, "Comedia", 147, 9)
P41 = Pelicula("Niños del hombre", 2006, "Ciencia ficción", 105, 7)
P42 = Pelicula("Volver al futuro II", 1989, "Ciencia ficción", 105, 7)
P43 = Pelicula("Atrápame si puedes", 2002, "Drama", 140, 8)
P44 = Pelicula("Perfume de mujer", 1992, "Drama", 157, 7)
P45 = Pelicula("Hombre mirando al sudeste", 1986, "Drama", 104, 7)
P46 = Pelicula("Misery", 1990, "Terror", 104, 8)
P47 = Pelicula("Fuego contra fuego", 1995, "Thriller", 172, 6)
P48 = Pelicula("Paris, Texas", 1984, "Drama", 144, 7)
P49 = Pelicula("Algo que pasó en año nuevo", 2022, "Comedia", 90, 8)
P50 = Pelicula("No miren arriba", 2021, "Comedia", 138, 7)



puntuadas = [globals()[f'P{i}'] for i in range(1, 51)]

top_totales = sorted(puntuadas, key=lambda x: (x.puntaje, x.duracion), reverse=True)

top_10 = list(top_totales[0:10])

print("Tu top 10 de películas favoritas es:")
print()
for i, p in enumerate(top_10, start=1):
    print(f"{i}. {p}")

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

print()
if len(generos_ganadores) == 1:
    print("Tu género preferido es:")
    print(genero_mas_repetido)
else:
    print("Tus géneros preferidos son:")
    for g in generos_ganadores:
        print(g)

suma = 0
for p in top_10:
    suma += p.duracion
promedio_duracion = int(suma / len(top_10))

print()
print("El promedio de duraciones de tus películas favoritas es:")
print(f"{promedio_duracion} minutos")

restos_año = 0
for p in top_10:
    restos_año += (2025 - p.año)
promedio_antiguedad = int(restos_año / len(top_10))
print()
print("El promedio de años de antiguedad de las películas de tu top 10 es:")
print(f"{promedio_antiguedad} años")

