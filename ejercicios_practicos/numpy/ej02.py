import numpy as np
import matplotlib.pyplot as plt

# 1º Imagen sintética de 100x100 píxeles entre 0 y 255 aleatorios
image = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
plt.imshow(image, cmap="gray", vmin=0, vmax=255)
plt.savefig("./ejercicios_practicos/numpy/imagenes/imagen.png")
# -------------------------------------------------------------------

# 2º Filtro de inversion de colores
filtro_inverso = 255 - image

plt.imshow(filtro_inverso, cmap="gray", vmin=0, vmax=255)
plt.savefig("./ejercicios_practicos/numpy/imagenes/imagen_inverso.png")
# ---------------------------------------------------------------------

# 3º Aumentar brillo un 20%
image_brillo = np.clip(image * 1.2, 0, 255).astype(np.uint8)
plt.imshow(image_brillo, cmap="gray", vmin=0, vmax=255)
plt.savefig("./ejercicios_practicos/numpy/imagenes/imagen_brillo.png")
# ---------------------------------------------------------------------

# 4º Extraer cuadrante superior izquierdo (50x50)
cuadrante = image[:50, :50]
plt.imshow(cuadrante, cmap="gray", vmin=0, vmax=255)
plt.savefig("./ejercicios_practicos/numpy/imagenes/imagen_cuadrante.png")
# -------------------------------------------------------------------------

# 5º Mascara que identifica pixeles muy oscuros
mask = image < 50

# los pixeles oscuros los muestra en blanco y los demas en negro
plt.imshow(mask.astype(np.uint8) * 255, cmap="gray")
plt.savefig("./ejercicios_practicos/numpy/imagenes/imagen_mascara.png")
# ----------------------------------------------------------------------
