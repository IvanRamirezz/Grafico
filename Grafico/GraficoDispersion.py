import matplotlib.pyplot as plt
import random

def grafico_dispersion_4_datos(x1, y1, x2, y2, x3, y3, x4, y4, titulo, etiqueta_x, etiqueta_y):
    # Crear un gráfico de dispersión con cuatro conjuntos de datos
    plt.scatter(x1, y1, c='red', marker='o', label='Datos 1')
    plt.scatter(x2, y2, c='green', marker='o', label='Datos 2')
    plt.scatter(x3, y3, c='blue', marker='o', label='Datos 3')
    plt.scatter(x4, y4, c='purple', marker='o', label='Datos 4')

    # Agregar etiquetas y título
    plt.title(titulo)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)

    # Mostrar la leyenda
    plt.legend()

    # Mostrar el gráfico
    plt.show()

# Generar 15 datos para cada conjunto en el rango de 5 a 30
datos_x1 = [17, 22, 19, 11, 10]
datos_y1 = [20, 23, 17, 14, 11]

datos_x2 = [17, 12, 13, 24, 15]
datos_y2 = [19, 24, 19, 16, 25]

datos_x3 = [18, 26, 23, 24, 15]
datos_y3 = [24, 24, 26, 18, 10]

datos_x4 = [21, 12, 23, 24, 25]
datos_y4 = [11, 23, 25, 27, 29]

# Llamar a la función para crear el gráfico de dispersión con cuatro conjuntos de datos
grafico_dispersion_4_datos(datos_x1, datos_y1, datos_x2, datos_y2, datos_x3, datos_y3, datos_x4, datos_y4,
                           'Gráfico de Dispersión (4 conjuntos de datos)', 'Eje X', 'Eje Y')
