import numpy as np
import matplotlib.pyplot as plt

# Generar 365 días de precios con tendencia y ruido
dias = 365
precio_inicial = 100
tendencia_diaria = 0.05
ruido_diario = 2

np.random.seed(0)
ruido = np.random.normal(0, ruido_diario, dias)
tendencia = np.arange(dias) * tendencia_diaria
precios = precio_inicial + tendencia + ruido

# Visualizar y guardar la imagen
plt.figure(figsize=(10, 6))  # Ajustar tamaño si es necesario
plt.plot(precios)
plt.title("Evolución de Precios con Tendencia y Ruido")
plt.xlabel("Día")
plt.ylabel("Precio")
plt.savefig(
    "./ejercicios_practicos/matplotlib/precios_simulados.png"
)  # Guardar como PNG
plt.close()  # Cerrar la figura para liberar memoria

print("Imagen 'precios_simulados.png' generada con éxito.")
