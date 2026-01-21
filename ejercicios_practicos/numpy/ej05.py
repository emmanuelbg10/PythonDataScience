import numpy as np
import pandas as pd

# Configuración para mostrar números
np.set_printoptions(
    suppress=True,
    formatter={"float_kind": lambda x: str(int(x)) if x.is_integer() else str(x)},
)

# Cargar dataset
path = "./ejercicios_practicos/numpy/datasets/ej05/winequality-white.csv"
df = pd.read_csv(path, sep=";")

# Seleccionar solo columnas numéricas
df_numeric = df.select_dtypes(include=["number"])
data = df_numeric.to_numpy()

# Información inicial
print("Columnas numéricas detectadas:", df_numeric.columns.tolist())
print("Forma del array:", data.shape)

# Normalización Min-Max
normalizacion = (data - data.min(axis=0)) / (data.max(axis=0) - data.min(axis=0))

# Estandarización Z-score
estandarizacion = (data - data.mean(axis=0)) / data.std(axis=0)

# Estadísticas originales
print("\nEstadísticas originales:")
print("Media:", np.round(data.mean(axis=0), 2))
print("Desviación estándar:", np.round(data.std(axis=0), 2))
print("Mínimo:", np.round(data.min(axis=0), 2))
print("Máximo:", np.round(data.max(axis=0), 2))

# Estadísticas después de normalización
print("\nEstadísticas después de Normalización Min-Max:")
print("Media:", np.round(normalizacion.mean(axis=0), 2))
print("Desviación estándar:", np.round(normalizacion.std(axis=0), 2))
print("Mínimo:", np.round(normalizacion.min(axis=0), 2))
print("Máximo:", np.round(normalizacion.max(axis=0), 2))

# Estadísticas después de estandarización
print("\nEstadísticas después de Estandarización Z-score:")
print("Media:", np.round(estandarizacion.mean(axis=0), 2))
print("Desviación estándar:", np.round(estandarizacion.std(axis=0), 2))
print("Mínimo:", np.round(estandarizacion.min(axis=0), 2))
print("Máximo:", np.round(estandarizacion.max(axis=0), 2))
