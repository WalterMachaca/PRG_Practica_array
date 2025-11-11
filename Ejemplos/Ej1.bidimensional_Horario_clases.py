# Horario de clases de una semana (Lunes a Viernes)
horario = [
    ["Taller de sistemas operativos", "Hardware de computadoras"],  # Lunes
    ["Programación I", "Ofimática y tecnología multimedia"],   # Martes
    ["Programación I", "Hardware de computadoras"], # Jueves
    ["Diseño y programación web I", "Inglés Técnico"], # Viernes
]

# Horario de clases completo
print("Horario de clases:")
dias = ["Lunes", "Martes", "Jueves", "Viernes"]

for i in range(len(horario)):
    print(f"{dias[i]}: {horario[i]}")
    
# Ver el horario por horas 
print("Horario por horas:")
for hora in range(len(horario[0])):
    materias_hora = [horario[dia][hora] for dia in range(len(horario))]
    print(f"Hora {hora+1}: {materias_hora}")
    
# Materias únicas en la semana
materias_unicas = set(i for fila in horario for i in fila)
print("Materias únicas de la semana:", materias_unicas)

# Materias que se repiten en la semana
materia = "Matemáticas"
contador = sum(fila.count(materia) for fila in horario)
print(f"La materia {materia} aparece {contador} veces en la semana")