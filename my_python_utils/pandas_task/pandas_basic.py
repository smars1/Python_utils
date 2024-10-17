import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


"""
Ejercicio 1: Exploración Básica de Datos
Carga los archivos ventas.csv y productos.csv en DataFrames de pandas.
Muestra las primeras y últimas 5 filas de cada DataFrame.
Muestra un resumen estadístico (count, mean, std, min, max, etc.) para las columnas numéricas de cada DataFrame.
"""
df_ventas = pd.read_csv("./ventas.csv")
print("\t\t Ventas \n")
print("\t\t \n primeras 5 filas")
print(df_ventas.head())
print("\t\t \n utilmas 5 filas")
print(df_ventas.tail())

print("\n")

print("\t\t productos \n")
df_productos = pd.read_csv("./productos.csv")
print("\t\t \n primeras 5 filas")
print(df_productos.head())
print("\t\t \n utilmas 5 filas")
print(df_productos.tail())

print("\nresumen estadístico (count, mean, std, min, max, etc.)")
print(df_ventas.describe())# toma todas las columnas de tipo numerico por defecto, pero se puede especificar las clumnas requeridas

"""
Ejercicio 2: Filtración y Ordenamiento
En df_ventas, filtra las filas donde la Cantidad vendida es mayor a 10.
Ordena df_ventas por la columna Fecha de manera descendente.
Ordena df_productos por Precio de manera ascendente.
"""

print("\t\t \n ventas mayores a 10: \n")
try:
    
    # Intenta realizar la operación de filtrado
    df_ventas_M10 = df_ventas[df_ventas['Cantidad'] > 10]
    print(df_ventas_M10)
    
    # ordenar fechas de forma descendente
    print(df_ventas_M10.sort_values(["Fecha"], ascending=False))

    # ordenar Precios de forma ascendente
    print(df_productos.sort_values(["Precio"], ascending=True))
except KeyError as e:
    # Manejo específico para cuando la columna no existe
    print(f"Error: La columna {e} no se encuentra en el DataFrame.")
except Exception as e:
    # Manejo de cualquier otro tipo de error no anticipado
    print(f"Ha ocurrido un error: {e}")

"""
Ejercicio 3: Agrupación y Agregación
Agrupa df_ventas por Producto y calcula la suma total de Cantidad vendida para cada producto.
Agrupa df_productos por Categoría y calcula el precio promedio de los productos en cada categoría.
"""

try: 

    # Agrupa df_ventas por Producto y calcula la suma total de Cantidad vendida para cada producto.
    print("\t\t\n Cantidad de ventas por producto")
    print(df_ventas.groupby("Producto").sum())
   
    # Agrupa df_productos por Categoría y calcula el precio promedio de los productos en cada categoría.
    print("\t\t\n Precio promedio por categoria")
    # Convierte la columna 'Precio' a numérica si no lo es
    df_productos['Precio'] = pd.to_numeric(df_productos['Precio'], errors='coerce')

    
    # Asegúrate de que el nombre de la columna 'Categoría' sea correcto
    # Reemplaza 'Categoria' con el nombre exacto de tu columna si es diferente
    # Aplicando la función mean() en la columna 'Precio' agrupada por 'Categoría'
    
    resultado = df_productos.groupby('Categoria')['Precio'].mean()
    print(resultado)

    
    #print(df_productos['Precio'].plot(kind='hist'))
    # Crear un histograma para la columna 'Precio'
    # plt.hist(df_productos['Precio'], bins=20, edgecolor='black')
    # plt.title('Distribución de Precios de Productos')
    # plt.xlabel('Precio')
    # plt.ylabel('Frecuencia')
    # plt.show()


except KeyError as e:
    # Manejo específico para cuando la columna no existe
    print(f"Error: La columna {e} no se encuentra en el DataFrame.")
except Exception as e:
    # Manejo de cualquier otro tipo de error no anticipado
    print(f"Ha ocurrido un error: {e}")


""")
Ejercicio 4: Merge y Concatenación
Realiza un merge entre df_ventas y df_productos para asociar el precio y la categoría con cada venta.
 Utiliza un left join sobre la columna Producto.
Crea un nuevo DataFrame que concatene df_ventas y df_productos por columnas (usa pd.concat con axis=1).
 Nota que este DataFrame no tendrá mucho sentido desde el punto de vista de los datos, pero es útil para practicar la concatenación.
"""
merge_df = pd.merge(df_ventas, df_productos, on = "Producto", how="left")
print(merge_df.head(10))

concat_df = pd.concat([df_ventas, df_productos], axis=1)
print("\t\t\n Concat DF \n")
print(concat_df.head(10))

"""
Ejercicio 5: Trabajo con Fechas
Convierte la columna Fecha en df_ventas a tipo datetime si no lo está ya.
Crea una nueva columna en df_ventas que contenga solo el año de cada venta.
Filtra las ventas que hayan ocurrido en un año específico.
"""

try:
    print(df_ventas.dtypes)
    if df_ventas['Fecha'].dtype is not 'datetime64[ns]':
        df_ventas["Fecha"] = pd.to_datetime(df_ventas["Fecha"])
        print(df_ventas.head(10))
        # 2. Crear una nueva columna con solo el año de cada venta
        df_ventas['Año'] = df_ventas['Fecha'].dt.year
        print(df_ventas)
        
        

    else:
        print(f"Tu columna es tipo: {df_ventas['Fecha'].dtype }")


except Exception as e : 
    print("Error code: ",e)

"""
Ejercicio 6: Exportación de Datos
Una vez realizadas algunas operaciones sobre df_ventas, exporta el DataFrame modificado a un nuevo archivo CSV.

"""