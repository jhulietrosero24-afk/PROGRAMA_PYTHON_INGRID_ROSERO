# Problema 5: Cálculo de Horas Trabajadas
# Universidad Nacional Abierta y a Distancia
# Curso: Fundamentos de Programación
# Estudiante: Ingrid Yuliet Rosero Robles
# Datos Iniciales: Matriz con 4 recursos
# Estructura: [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]
# --------------------------
recursos = [
    ["Ana Ruiz", 8, 9, 8, 10, 7],
    ["Luis Gómez", 7, 8, 7, 8, 7],
    ["Carlos Mora", 9, 9, 8, 9, 9],
    ["Sofía León", 8, 7, 8, 7, 8]
]

# --------------------------
# Módulo: Función para calcular total y clasificar jornada
# --------------------------
def calcular_y_clasificar(horas):
    """
    Recibe una lista de horas diarias, calcula el total semanal
    y devuelve el total y su clasificación.
    """
    total = sum(horas)  # Suma todas las horas de la semana
    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar o inferior"
    return total, clasificacion

# --------------------------
# Procesamiento y Salida de Resultados
# --------------------------
print("=== INFORME DE HORAS TRABAJADAS SEMANALES ===")
print("-" * 55)
print(f"{'Nombre del Recurso':<20} | {'Total Horas':<12} | {'Clasificación'}")
print("-" * 55)

# Recorrer cada recurso de la matriz
for registro in recursos:
    nombre = registro[0]
    horas_semana = registro[1:]  # Extrae solo las horas diarias
    total_horas, tipo_jornada = calcular_y_clasificar(horas_semana)
    # Imprimir resultado formateado
    print(f"{nombre:<20} | {total_horas:<12} | {tipo_jornada}")

print("-" * 55)
print("=== FIN DEL INFORME ===")
