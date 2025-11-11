# Notas de un estudiante en 4 materias
notas = [85, 90, 78, 92]

# Promedio
print("Notas del estudiante:", notas)
print("Promedio:", sum(notas)/len(notas))

# Nota más alta y más baja
print("Nota más alta:", max(notas))     
print("Nota más baja:", min(notas))

# Materias aprobadas (nota >= 60)
aprobadas = [i+1 for i, nota in enumerate(notas) if nota >= 60]
print("Materias aprobadas (número de materia):", aprobadas)

# Materias reprobadas (nota < 60)
reprobadas = [i+1 for i, nota in enumerate(notas) if nota   < 60]
print("Materias reprobadas (número de materia):", reprobadas)

# Verificar si el estudiante aprobó todas las materias
if len(reprobadas) == 0:
    print("El estudiante aprobó todas las materias.")       
else:
    print("El estudiante no aprobó todas las materias.")        
# Verificar si el estudiante reprobó alguna materia
if len(reprobadas) > 0:         
    print("El estudiante reprobó alguna materia.")
else:
    print("El estudiante no reprobó ninguna materia.")
       
    
       