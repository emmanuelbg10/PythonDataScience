import numpy as np

# Crear una matriz 5x24 con temperaturas aleatorias entre 15ºC y 35ºC
temperaturas = np.random.uniform(15, 35, (5, 24))
print("Temperaturas:\n", np.round(temperaturas, 2))

# -------------------------------------------------------------------

# Calcular la temperatura media de cada sensor
medias_filas = np.mean(temperaturas, axis=1)
medias_filas = np.round(medias_filas, 2)
print("1º Media de filas:", medias_filas, "\n")
# ---------------------------------------------

# Identificar el sensor con mayor temperatura promedio
sensor = np.argmax(medias_filas)
print("2º La temperatura mas alta está en el sensor:", (sensor + 1))
print()
# ---------------------------------------------------------------

# Encontrar las horas donde algun sensor superó los 30ºC
horas_criticas = np.where(np.any(temperaturas > 30, axis=0))[0]
print(horas_criticas.shape)
print("3º Las horas donde algun sensor supero los 30 grados:", horas_criticas)
# --------------------------------------------------------

# Calcular la desviación estandar de cada sensor
print("4º Desviación estandar de cada sensor:\n", np.std(temperaturas, axis=1))
# -----------------------------------------------
