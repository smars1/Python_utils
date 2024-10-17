# Python 

| Galeria |
| ------- |
| [Python Utils]() |
| [Pandas Utils](https://github.com/smars1/Python/tree/main/PYTHON_DS/python_utils#pandas-utils) |

# Python Utils


| Galeria basic |
| ------- |
| [ Manejo de string ](https://github.com/smars1/Python/tree/main/PYTHON_DS/python_utils#mayuscula-y-minusculas) |
| [ Mayuscula y minusculas ]() |
| [ Metodos de Busqueda y Reemplazo ]() |
| [ Metodos de limpieza de espacios en blanco ]() |
| [ Metodo de formateo de string ]() |
| []() |
| []() |
| []() |
| []() |
| []() |
| []() |
| []() |
| []() |

| Galeria advance|
| ------- |
| [**kwargs](https://github.com/smars1/Python/tree/main/PYTHON_DS/python_utils#kwargs) |
| [Expression list]() |
| [Expresiones lambda]() |
| []() |
| []() |
| []() |
| []() |
| []() |


# Manejo de strings 


```py
len(string)#  Retorna la longitud de la string.

str[índice] # Accede al carácter en la posición dada.

str[inicio:fin] # Extrae una subcadena desde el índice de inicio hasta el índice final - 1.

+ # Concatena strings.

* #  Repite la string un número de veces.
```
## Mayuscula y minusculas
```py
str.upper()# Convierte todos los caracteres a mayúsculas.
str.lower()# Convierte todos los caracteres a minúsculas.
str.capitalize()# Capitaliza la primera letra de la string.
str.title()# Capitaliza la primera letra de cada palabra.

```

## Metodos de Busqueda y Reemplazo

```py
str.find(sub)# Retorna el índice más bajo donde se encuentra la subcadena (o -1 si no la encuentra).
str.replace(old, new)# Reemplaza todas las ocurrencias de una subcadena por otra.
```

## Metodos de limpieza de espacios en blanco
```py
str.strip()# Elimina espacios en blanco al inicio y al final.
str.rstrip()# Elimina espacios en blanco al final.
str.lstrip()# Elimina espacios en blanco al inicio.
```

## Metodo de formateo de string
```py
str.format()# Formatea la string usando un estilo de formato específico.

# Ejemplo de formateo de string con el método format
nombre = "Juan"
edad = 30
ciudad = "Madrid"

mensaje = "Hola, mi nombre es {}. Tengo {} años y vivo en {}."
print(mensaje.format(nombre, edad, ciudad))

```
Este método es muy útil porque te permite controlar dónde y cómo se insertan los datos en la string, y también facilita la lectura y mantenimiento del código. Además, puedes reutilizar la misma string mensaje con diferentes valores.

# Python Regex o expresiones regulares

Expresiones Regulares (Regex)
Primero, debes importar el módulo re.


## Funciones Básicas

```py
re.search(pattern, string)# Busca el patrón dentro de la string; retorna un objeto de coincidencia si lo encuentra.
re.match(pattern, string)# Busca el patrón al inicio de la string.
re.findall(pattern, string)# Encuentra todas las coincidencias del patrón en la string y las retorna en una lista.
re.sub(pattern, repl, string)# Reemplaza las ocurrencias del patrón en la string.
```

## Metacaracteres

```py
. # Cualquier carácter excepto nueva línea.
^ # Inicio de la string.
$ #Final de la string.
* # Cero o más repeticiones.
+ # Una o más repeticiones.
? #Cero o una repetición.
{n} # Exactamente n repeticiones.
{n,} # n o más repeticiones.
{,m} # Hasta m repeticiones.
{n,m} # Entre n y m repeticiones.
[] #` Conjunto de caracteres.
| # Operador OR.
() # Grupo.

```
En estos ejemplos, utilizamos ```re.search()``` que busca un patrón en una string y retorna un objeto de coincidencia si lo encuentra. La función print se utiliza para imprimir el resultado. Si la expresión regular coincide con alguna parte de la string, se imprimirá un objeto Match; de lo contrario, se imprimirá None.

```py
import re

# Ejemplo con '.'
print(re.search(r"a.b", "acb"))  # Coincidirá

# Ejemplo con '^'
print(re.search(r"^Hola", "Hola Mundo"))  # Coincidirá

# Ejemplo con '$'
print(re.search(r"fin$", "El final fin"))  # Coincidirá

# Ejemplo con '*'
print(re.search(r"ho*la", "hoooooola"))  # Coincidirá

# Ejemplo con '+'
print(re.search(r"ho+la", "hola"))  # Coincidirá

# Ejemplo con '?'
print(re.search(r"ho?la", "hla"))  # Coincidirá

# Ejemplo con '{n}'
print(re.search(r"ho{2}la", "hoola"))  # Coincidirá

# Ejemplo con '{n,}'
print(re.search(r"ho{2,}la", "hoooooooola"))  # Coincidirá

# Ejemplo con '{,m}'
print(re.search(r"ho{,2}la", "hoola"))  # Coincidirá

# Ejemplo con '{n,m}'
print(re.search(r"ho{1,3}la", "hoooola"))  # Coincidirá

# Ejemplo con '[]'
print(re.search(r"[abc]", "bravo"))  # Coincidirá

# Ejemplo con '|'
print(re.search(r"perro|gato", "tengo un gato"))  # Coincidirá

# Ejemplo con '()'
print(re.search(r"(ho)+", "hohohoho"))  # Coincidirá

```

```.``` - Coincide con cualquier carácter excepto una nueva línea.

Ejemplo: a.b coincidirá con 'acb', 'arb', 'a3b', pero no con 'a\nb'.

```^``` - Coincide con el inicio de la string.

Ejemplo: ^Hola coincidirá con cualquier string que comience con 'Hola'.

```$``` - Coincide con el final de la string.

Ejemplo: fin$ coincidirá con cualquier string que termine en 'fin'.

```*``` - Coincide con 0 o más repeticiones del patrón precedente.

Ejemplo: ho*la coincidirá con 'hla', 'hola', 'hoooola', etc.

```+``` - Coincide con 1 o más repeticiones del patrón precedente.

Ejemplo: ho+la coincidirá con 'hola', 'hoola', 'hoooola', pero no con 'hla'.

```?``` - Coincide con 0 o 1 repetición del patrón precedente.

Ejemplo: ho?la coincidirá con 'hla' y 'hola', pero no con 'hoola'.

```{n}``` - Coincide con exactamente n repeticiones del patrón precedente.

Ejemplo: ho{2}la coincidirá solo con 'hoola'.

```{n,}``` - Coincide con n o más repeticiones del patrón precedente.

Ejemplo: ho{2,}la coincidirá con 'hoola', 'hoooola', etc.

```{,m}``` - Coincide con hasta m repeticiones del patrón precedente.

Ejemplo: ho{,2}la coincidirá con 'hla', 'hola', y 'hoola'.

```{n,m}``` - Coincide con entre n y m repeticiones del patrón precedente.

Ejemplo: ho{1,3}la coincidirá con 'hola', 'hoola', y 'hoooola'.

```[]``` - Denota un conjunto de caracteres. Coincide con cualquier carácter dentro de los corchetes.

Ejemplo: [abc] coincidirá con 'a', 'b', o 'c'.

```|``` - Operador OR, coincide con patrones a su izquierda o derecha.

Ejemplo: perro|gato coincidirá con 'perro' o 'gato'.

```()```- Grupos de patrones. Se utiliza para agrupar parte de una expresión regular.

Ejemplo: (ho)+ coincidirá con 'ho', 'hoho', 'hohoho', etc.



## Secuencias especiales

```py
"\d" # Cualquier dígito (equivalente a [0-9]).
"\D" # Cualquier no dígito (equivalente a [^0-9]).
"\s" # Cualquier espacio en blanco.
"\S" # Cualquier no espacio en blanco.
"\w" # Cualquier carácter alfanumérico (equivalente a [a-zA-Z0-9_]).
"\W" # Cualquier no carácter alfanumérico.
```
### Expresiones regulares

```py
# Ejemplo con '\d'
print(re.search(r"\d", "Número 5"))  # Coincidirá

# Ejemplo con '\D'
print(re.search(r"\D", "123a456"))  # Coincidirá

# Ejemplo con '\s'
print(re.search(r"Hola\sMundo", "Hola Mundo"))  # Coincidirá

# Ejemplo con '\S'
print(re.search(r"\S", " a b "))  # Coincidirá

# Ejemplo con '\w'
print(re.search(r"\w-\w", "A-2"))  # Coincidirá

# Ejemplo con '\W'
print(re.search(r"\W", "Palabra!"))  # Coincidirá
```


### \d - Coincide con cualquier dígito [0-9].

Ejemplo: \d coincidirá con '2', '3', '9', etc.

### \D - Coincide con cualquier cosa que no sea un dígito.

Ejemplo: \D coincidirá con 'a', '!', pero no con '3'.

### \s - Coincide con cualquier espacio en blanco (espacios, tabs, nuevas líneas).

Ejemplo: Hola\sMundo coincidirá con 'Hola Mundo'.

### \S - Coincide con cualquier carácter que no sea un espacio en blanco.

Ejemplo: \S coincidirá con 'a', '1', '!', etc., pero no con ' '.

### \w - Coincide con cualquier carácter alfanumérico [a-zA-Z0-9_].

Ejemplo: \w-\w coincidirá con 'a-a', '1-3', 'Z_2', etc.

### \W - Coincide con cualquier cosa que no sea un carácter alfanumérico.

Ejemplo: \W coincidirá con '!', '@', '#', pero no con 'a' o '1'.


# **kwargs

Los **kwargs en Python son una manera de pasar argumentos de longitud variable a una función, donde los argumentos se manejan como un diccionario. La palabra kwargs significa "keyword arguments" o "argumentos de palabra clave". Esta característica es útil cuando quieres que tu función pueda manejar un número variable de argumentos con palabras clave.

## Cómo se usan:
Para usar **kwargs en una función, simplemente lo pones en la definición de la función. Los argumentos que se pasan a la función se convertirán en un diccionario dentro de la función, donde cada clave es el nombre del argumento y cada valor es el valor del argumento.

## Buenas prácticas:
Usar nombres claros y descriptivos: Al igual que con cualquier variable en Python, es importante usar nombres que hagan que el código sea fácil de leer y entender.

No abusar de **kwargs: Aunque son útiles, pueden hacer que el código sea más difícil de entender si se usan en exceso o en situaciones innecesarias.

Combinar con argumentos regulares y *args con cuidado: Si una función usa argumentos regulares, *args, y **kwargs, debes tener cuidado con el orden en que los pasas.

Documentar qué se espera en **kwargs: Como **kwargs puede aceptar cualquier número de argumentos de palabras clave, es importante documentar qué se espera o se admite en una función.

## Ejemplo de Código:
Vamos a definir una función que usa **kwargs para personalizar un saludo:

```py
def saludo_personalizado(**kwargs):
    saludo = kwargs.get('saludo', 'Hola')
    nombre = kwargs.get('nombre', 'amigo')
    puntuacion = kwargs.get('puntuacion', '!')
    
    return f"{saludo}, {nombre}{puntuacion}"

# Uso de la función
print(saludo_personalizado(nombre="Carlos", saludo="Buen día", puntuacion="."))

```
En este ejemplo, la función saludo_personalizado puede tomar cualquier número de argumentos de palabras clave. Usamos el método .get() para obtener valores de estos argumentos, proporcionando valores por defecto en caso de que no se pasen ciertos argumentos.

## Manejo de excepciones

```py
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("¡División por cero!")
finally:
    print("Este bloque se ejecuta siempre")

```

## Trabajo con Archivos
```py
# Leer un archivo
with open("archivo.txt", "r") as f:
    contenido = f.read()

# Escribir en un archivo
with open("archivo.txt", "w") as f:
    f.write("Hola Python")

```

## Clases y objetos

```py
class MiClase:
    def __init__(self, valor):
        self.valor = valor

    def muestra_valor(self):
        print(self.valor)

obj = MiClase(10)
obj.muestra_valor()

```
## Expression list

Las comprensiones de listas son una característica única y poderosa de Python para crear listas de manera concisa y eficiente.

### Sintaxis basica
```py
[expresion for item in iterable]
```

### Buenas practicas
- Mantén las comprensiones de listas simples y directas; evita demasiada complejidad.
- Prefiere bucles normales cuando las comprensiones de listas se vuelvan difíciles de leer.
- Utiliza comprensiones de listas para reemplazar map y filter donde sea lógico.

### Ejemplos:

### Crear una lista de cuadrados:

```py
cuadrados = [x**2 for x in range(10)]
```

### Filtrar elementos que cumplen una condición:

```py
pares = [x for x in range(10) if x % 2 == 0]
```

### Aplicar una función a cada elemento:
```py
import math
raices = [math.sqrt(x) for x in range(1, 11)]
```

### Lista de comprensión con múltiples bucles:
```py
combinaciones = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
```



## Expresiones lambda

Las expresiones lambda son una forma de crear funciones anónimas, es decir, funciones sin nombre. Son útiles para operaciones cortas y sencillas.

### Sintaxis Básica
```py
lambda argumentos: expresion
```

### Buenas practicas
- Usa expresiones lambda para funciones simples; para funciones más complejas, define una función regular.
- Evita el uso excesivo de lambdas, ya que puede hacer que el código sea difícil de entender.
- Las lambdas son útiles para funciones de orden superior como map(), filter(), y sorted().

### Ejemplos:

### Suma de dos números:
```py
suma = lambda x, y: x + y
print(suma(5, 3))
```

### Ordenar una lista de tuplas por el segundo elemento:
```py
lista = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
lista.sort(key=lambda x: x[1])
print(lista)
```

### Aplicar función lambda a elementos de una lista:
```py
cuadrados = list(map(lambda x: x**2, range(10)))
```

# Pandas Utils

| Galeria |
| ------- |
| [Metodos utiles de pandas](https://github.com/smars1/Python/tree/main/PYTHON_DS/python_utils#metodos-utiles-de-pandas) |
| [Control de errores](https://github.com/smars1/Python/tree/main/PYTHON_DS/python_utils#control-de-errores)|
| [Pandas utils: excel](https://github.com/smars1/Python/tree/main/PYTHON_DS/python_utils#pandas-utils-excel) |


# Metodos utiles de pandas

| Metodos Utiles de pandas |
| ------------------------ |
| --- [Leer datos de un archivo CSV/Excel]()                 --- |
| --- [Escribir datos a un archivo excel ]()                 --- |
| --- [Ver las primeras/últimas filas de un DataFrame]()                 --- |
| --- [Información general del DataFrame]()                 --- |
| --- [Estadisticas basicas de las columnas numericas]()                 --- |
| --- [Seleccionar una columna en especifica o multimples columnas]()                 --- |
| --- [Filtrar filas por condicionales]()                 --- |
| --- [Ordenar un dataframe]()                 --- |
| --- [Agrupacion y agregacion de datos]()                 --- |
| --- [Combinar dataframes]()                 --- |
| --- [Merge]()                 --- |
| --- [Join]()                 --- |
| --- [ Ejemplos Adicionales y Consideraciones: Merges]()                 --- |
| --- [Manejo de valores nulos]()                 --- |
| --- [Aplicar una función a las columnas o filas]()                 --- |
| --- [Cambio de tipo de datos de una columna]()                 --- |
| --- [Filtrado por indice]()                 --- |
| --- []()                 --- |
| --- []()                 --- |
| --- []()                 --- |
| --- []()                 --- |
| --- []()                 --- |
| --- []()                 --- |


## Instalacion e importacion pandas
```sh
pip install pandas
```
```py
import pandas as pd
```

## Leer datos de un archivo CSV/Excel

```py
df = pd.read_csv('archivo.csv')
df = pd.read_excel('archivo.xlsx', sheet_name='hoja1')
```

## Escribir datos a un archivo excel 

```py
df.to_csv('salida.csv', index=False)
df.to_excel('salida.xlsx', sheet_name='mi_hoja', index=False)

```

## Ver las primeras/últimas filas de un DataFrame

```py
df.head()  # Primeras 5 filas
df.tail()  # Últimas 5 filas
```

## Información general del DataFrame

```py
df.info()
```

## Estadisticas basicas de las columnas numericas

```py
df.describe()
```

## Seleccionar una columna en especifica o multimples columnas
```py
# Selecciona una columna
columna = df['nombre_columna']

# Seleccciona multiples columnas
subconjunto = df[['columna1', 'columna2']]
```

## Filtrar filas por condicionales

```py
filas_filtradas = df[df['columna'] > valor]
```

## Ordenar un dataframe

```py
df.sort_values(by='columna', ascending=True)
```
Es importante señalar que para que este ordenamiento funcione correctamente, la columna Fecha debe estar en un formato reconocible como fecha por Pandas (generalmente datetime64[ns] en Pandas). Si no está en un formato de fecha, es posible que debas convertirla antes de realizar el ordenamiento.

## Agrupacion y agregacion de datos
```py
df.groupby('columna').sum()  # Otras funciones: mean(), count(), etc.
```

## Concat dataframes
concat se usa para concatenar DataFrames a lo largo de un eje particular.
```py
# Concatenar DataFrames
pd.concat([df1, df2]) 

# Concatenar por filas (verticalmente)
concatenado_df = pd.concat([df1, df2], axis=0)

# Concatenar por columnas (horizontalmente)
concatenado_df = pd.concat([df1, df2], axis=1)

# Unir DataFrames usando una columna comun
df1.merge(df2, on='columna') 
```
axis=0 indica que la concatenación es vertical (añadiendo filas), mientras que axis=1 indica una concatenación horizontal (añadiendo columnas)

## Merge
El método merge se utiliza para combinar DataFrames basándose en valores comunes de columnas (llaves).

```py
# Sintaxis básica
merged_df = pd.merge(df1, df2, on='columna_común', how='tipo_de_unión')

```
how puede ser:

- 'inner': Devuelve solo las filas que tienen valores coincidentes en ambos DataFrames.
- 'outer': Devuelve todas las filas de ambos DataFrames, con coincidencias de uno u otro DataFrame donde estén disponibles y NaN en otros lugares.
- 'left': Devuelve todas las filas del DataFrame izquierdo y las filas coincidentes del derecho, con NaN en los lugares donde no hay coincidencia.
- 'right': Devuelve todas las filas del DataFrame derecho y las filas coincidentes del izquierdo, con NaN donde no hay coincidencia.

## Join
join es un método para combinar DataFrames basado en índices o en una columna clave.

```py
# Sintaxis básica
joined_df = df1.join(df2, how='tipo_de_unión')

```

Los tipos de unión (how) son los mismos que en merge

## Ejemplos Adicionales y Consideraciones: Merges
- Claves Múltiples: Puedes unir usando múltiples columnas con on=['col1', 'col2'].
- Unión con Índices: Para unir usando índices en lugar de columnas, usa left_index=True o right_index=True.
- Sufijos: Si hay columnas con el mismo nombre en diferentes DataFrames, puedes usar suffixes para diferenciarlas después de la unión.

```py
merged_df = pd.merge(df1, df2, on='columna_común', how='inner', suffixes=('_left', '_right'))
```

### Manejo de Columnas con Nombres Diferentes:
Si las columnas clave tienen diferentes nombres en diferentes DataFrames, usa left_on y right_on para especificarlos.

```py
merged_df = pd.merge(df1, df2, left_on='columna_df1', right_on='columna_df2', how='inner')
```

## Manejo de valores nulos
```py
df.dropna()     # Eliminar filas con valores nulos
df.fillna(valor) # Reemplazar valores nulos por un valor específico
```

## Aplicar una función a las columnas o filas
```py
df['nueva_columna'] = df['columna'].apply(lambda x: x * 2)  # Ejemplo con lambda
```

## Cambio de tipo de datos de una columna

```py
df['columna'] = df['columna'].astype(tipo)
```

## Filtrado por indice

```py
df.iloc[5]     # Fila en la posición 5
df.iloc[0:5]   # Filas de la posición 0 a 4

```
# Control de errores

```py
try:
    # Intenta realizar la operación de filtrado
    df_ventas_M10 = df_ventas[df_ventas['cantidad'] > 10]
except KeyError:
    # Manejo específico para cuando la columna no existe
    print("Error: La columna 'Cantidad' no se encuentra en el DataFrame.")
except Exception as e:
    # Manejo de cualquier otro tipo de error no anticipado
    print(f"Ha ocurrido un error: {e}")
```



# Pandas utils: excel

## Leer archivos excel
```py
# Leer un archivo Excel completo
df = pd.read_excel('archivo.xlsx')

# Leer una hoja específica
df = pd.read_excel('archivo.xlsx', sheet_name='nombre_hoja')

# Leer un archivo .xlsb (requiere la biblioteca 'pyxlsb')
df = pd.read_excel('archivo.xlsb', sheet_name='nombre_hoja', engine='pyxlsb')

```

## Filtrar y Seleccionar Datos

```py
# Filtrar filas donde la columna es igual a un valor
df_filtrado = df[df['columna'] == valor]

# Filtrar filas donde la columna está en una lista de valores
df_filtrado = df[df['columna'].isin([valor1, valor2, valor3])]

# Seleccionar una columna específica
serie = df['columna']

# Seleccionar múltiples columnas
df_seleccionado = df[['columna1', 'columna2']]

```

## Ordenar datos

```py
# Ordenar el DataFrame por una columna
df_ordenado = df.sort_values(by='columna')

# Ordenar en orden descendente
df_ordenado_desc = df.sort_values(by='columna', ascending=False)

```

## Guardar datos en un archivo

```py
# Guardar DataFrame en un archivo CSV
df.to_csv('archivo_salida.csv', index=False)

# Guardar con encabezados de columna
df.to_csv('archivo_salida.csv', index=False, header=True)

# Guardar DataFrame en un archivo Excel
df.to_excel('archivo_salida.xlsx', index=False)

# Guardar en una hoja específica
df.to_excel('archivo_salida.xlsx', sheet_name='nombre_hoja', index=False)

```