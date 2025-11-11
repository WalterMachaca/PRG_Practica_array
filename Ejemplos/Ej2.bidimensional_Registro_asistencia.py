# Asistencia de estudiantes
# "P" = Presente, "F" = Falta, "L" = Licencia
asistencia = [
    ["P", "P", "F", "L", "P"],  # Estudiante 1
    ["P", "F", "L", "P", "F"],  # Estudiante 2
    ["F", "P", "P", "F", "P"],  # Estudiante 3
]

estudiantes = ["Ana", "Luis", "María"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# Mostrar asistencia en forma de tabla
print("Registro de asistencia:")
for i in range(len(asistencia)):
    print(estudiantes[i], ":", asistencia[i])
    
# Calcular y mostrar el total de asistencias, faltas y licencias por estudiante
for i in range(len(asistencia)):
    total_presente = asistencia[i].count("P")
    total_falta = asistencia[i].count("F")
    total_licencia = asistencia[i].count("L")
    print(f"{estudiantes[i]} - Presente: {total_presente}, Faltas: {total_falta}, Licencias: {total_licencia}")
    
# Calcular y mostrar el total de asistencias, faltas y licencias por día
print("Total por día:") 
for j in range(len(dias)):
    total_presente_dia = sum(1 for i in range(len(asistencia)) if asistencia[i][j] == "P")
    total_falta_dia = sum(1 for i in range(len(asistencia)) if asistencia[i][j] == "F")
    total_licencia_dia = sum(1 for i in range(len(asistencia)) if asistencia[i][j] == "L")
    print(f"{dias[j]} - Presente: {total_presente_dia}, Faltas: {total_falta_dia}, Licencias: {total_licencia_dia}") 
    
# Calcular el porcentaje de asistencia por estudiante
for i in range(len(asistencia)):
    porcentaje_asistencia = (asistencia[i].count("P") / len(asistencia[i])) * 100
    print(f"{estudiantes[i]} - Porcentaje de asistencia: {porcentaje_asistencia:.2f}%") 