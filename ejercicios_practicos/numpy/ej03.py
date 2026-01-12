import numpy as np
from datetime import date

# 1º Crear la matriz 365x4
n_dias = 365

temp_max = np.random.uniform(15, 40, n_dias)
temp_min = np.random.uniform(low=-5, high=temp_max)

# Precipitación: 70% días sin lluvia, 30% con lluvia (0–50 mm)
precipitacion = np.random.choice([0, 1], size=n_dias, p=[0.7, 0.3])
precipitacion = np.array(
    [np.random.uniform(0.1, 50) if p == 1 else 0 for p in precipitacion]
)

humedad = np.random.uniform(0, 100, n_dias)

# Temperatura maxima, temperatura minima, precipitacion y humedad
matriz = np.column_stack((temp_max, temp_min, precipitacion, humedad))

print("Matriz completa (primeros 10 días para ver variedad):")
print(np.round(matriz[:10], 1))

# 2º Seleccionar los dias donde llovió
mask = precipitacion > 0
lluvia = np.where(mask)[0] + 1
print("\nDias donde hay lluvia:")
print(lluvia)

# 3º Encontrar dias de verano
mask = (temp_max > 30) & (humedad < 60)
verano = np.where(mask)[0] + 1
print("\nDias donde hay calor y humedad:")
print(verano)

# 4º Extraer datos del primer dia de cada mes de forma automática
# Comprobar si es bisiesto
anio = date.today().year

bisiesto = anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)
dias_por_mes = np.array(
    [31, 29 if bisiesto else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
)

# Índices del primer día de cada mes
primer_dia_mes = np.cumsum(np.concatenate(([0], dias_por_mes[:-1])))
primer_dia_mes_datos = matriz[primer_dia_mes]

print("\nExtraer datos del primer dia de cada mes")
print(np.round(primer_dia_mes_datos, 1))
