Producción_fábrica = [
    [15,10,22,6],
    [23,22,18,14],
    [8,12,15,16]
]

print("Producción de la fábrica (unidades producidas por cada línea de producción):")
for fila in Producción_fábrica:
    print(fila)
    
for i in range(len(Producción_fábrica)):
    total_dia = sum(Producción_fábrica[i])
    print(f"Total producido por la línea de producción {i+1}: {total_dia} unidades")
    
print ("Total producido por cada máquina en la semana:")
for j in range(len(Producción_fábrica[0])):
    total_maquina = sum(Producción_fábrica[i][j] for i in range(len(Producción_fábrica)))
    print(f"Máquina {j+1}: {total_maquina} unidades")
