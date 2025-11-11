# Lista que simula una "base de datos" de cursos
cursos = []

# Crear
def crear_curso(nombre, docente):
    curso = {"nombre": nombre, "docente": docente}
    cursos.append(curso)
    print(f" Curso '{nombre}' agregado.")

# Leer
def leer_cursos():
    print("\n Lista de cursos:")
    if not cursos:
        print("No hay cursos registrados.")
    for i, curso in enumerate(cursos, 1):
        print(f"{i}. {curso['nombre']} - Docente: {curso['docente']}")

# Actualizar
def actualizar_curso(indice, nuevo_nombre, nuevo_docente):
    if 0 <= indice < len(cursos):
        cursos[indice]["nombre"] = nuevo_nombre
        cursos[indice]["docente"] = nuevo_docente
        print("Curso actualizado.")
    else:
        print("Curso no encontrado.")

# Eliminar
def eliminar_curso(indice):
    if 0 <= indice < len(cursos):
        eliminado = cursos.pop(indice)
        print(f"Curso '{eliminado['nombre']}' eliminado.")
    else:
        print("Curso no encontrado.")


# EJEMPLO
crear_curso("Matemáticas", "Prof. García")
crear_curso("Biología", "Prof. Pérez")
crear_curso("Historia", "Prof. Ramírez")
leer_cursos()

actualizar_curso(1, "Biología", "Prof. Pérez López")
leer_cursos()

eliminar_curso(0)  # Elimina "Matemáticas"
leer_cursos()

