calificaciones = [
    [67, 78, 90],  # Calificaciones del estudiante 1
    [88, 92, 79],  # Calificaciones del estudiante 2
    [45, 55, 70],  # Calificaciones del estudiante 3
]
print("Calificaciones de los estudiantes:")
for fila in calificaciones:
    print(fila)

promedios_estudiantes=[]
for i in range(len(calificaciones)):
    promedio_estudiante = sum(calificaciones[i]) / len(calificaciones[i])
    promedios_estudiantes.append(promedio_estudiante)
    print(f"Promedio del estudiante {i+1}: {promedio_estudiante:.2f}")

mejor= max(promedios_estudiantes)
estudiante=promedios_estudiantes.index(mejor)+1
print(f"El estudiante con el mejor promedio es el estudiante numero {estudiante} con un promedio de {mejor:.2f}")