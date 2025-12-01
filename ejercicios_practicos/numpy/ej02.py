import numpy as np

miarray = np.random.uniform(15, 35, (5, 24))

medias_filas = np.mean(miarray, axis=1)
medias_filas = np.round(medias_filas, 2)

print("Media de filas:", medias_filas, "\n")
sensor = np.argmax(medias_filas)
print("La temperatura mas alta está en el sensor:", (sensor + 1))
print()

horas_criticas = np.where(np.any(miarray > 30, axis=0))[0]
print(horas_criticas)
