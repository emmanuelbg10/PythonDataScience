import numpy as np
import pandas as pd


# 1º Cargar el dataset y convertirlo a array NumPy (con solo las columnas numericas)
path = "./ejercicios_practicos/numpy/datasets/ej04/student/student-mat.csv"

# Cargar CSV
df = pd.read_csv(path, sep=";")  # el CSV usa ';' como separador

# Seleccionar solo columnas que ya son numéricas
df_numeric = df.select_dtypes(include=[np.number])

# Convertir a array NumPy
array_numerico = df_numeric.to_numpy()

print("Ejercicio1:")
print("Columnas numéricas detectadas:", df_numeric.columns.tolist())
print("Forma del array:", array_numerico.shape)
print("Primeras filas:")
print(array_numerico[:5])

# 2º Seleccionar estudiantes con nota final (G3) mayor a 15
print("\nEjercicio2:")
df_estudiantes_filtrados = df_numeric[df_numeric["G3"] > 15]
array_numerico2 = df_estudiantes_filtrados.to_numpy()
print("Total con G3 > 15:", array_numerico2.shape[0])
print(array_numerico2[:5])

# 3º Encontrar mejora de notas de G1 a G3
print("\nEjercicio3:")
df_mejora = df_numeric[df_numeric["G3"] > df_numeric["G1"]]
array_numerico3 = df_mejora.to_numpy()
print("Total con mejora de G1 a G3:", array_numerico3.shape[0])
print(array_numerico3[:5])


print("\nEjercicio4: Análisis por tercios de la clase")

# Número total de estudiantes
n = array_numerico.shape[0]
tercio = n // 3

# Slicing de cada tercio
primer_tercio = array_numerico[:tercio]
segundo_tercio = array_numerico[tercio : 2 * tercio]
tercer_tercio = array_numerico[2 * tercio :]

print("Cantidad de personas en cada tercio:")
print("Primer tercio:", primer_tercio.shape[0])
print("Segundo tercio:", segundo_tercio.shape[0])
print("Tercer tercio:", tercer_tercio.shape[0])
