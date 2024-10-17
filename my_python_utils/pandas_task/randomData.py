import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configuración para la generación de datos ficticios
np.random.seed(0)  # Para reproducibilidad
n_rows = 100
fechas = [datetime.now() - timedelta(days=i) for i in range(n_rows)]
productos = ['Producto_A', 'Producto_B', 'Producto_C']
cantidades = np.random.randint(1, 20, size=n_rows)
precios = np.random.uniform(10, 100, size=len(productos))
categorias = ['Categoría 1', 'Categoría 2', 'Categoría 3']

# Creación del DataFrame de Ventas
df_ventas = pd.DataFrame({
    'Fecha': np.random.choice(fechas, size=n_rows),
    'Producto': np.random.choice(productos, size=n_rows),
    'Cantidad': cantidades
})

# Creación del DataFrame de Productos
df_productos = pd.DataFrame({
    'Producto': productos,
    'Precio': precios,
    'Categoría': categorias
})

# Guardar DataFrames en archivos
df_ventas.to_csv('ventas.csv', index=False)
df_productos.to_csv('productos.csv', index=False)

# Opcionalmente, guardar en Excel
df_ventas.to_excel('ventas.xlsx', index=False)
df_productos.to_excel('productos.xlsx', index=False)
