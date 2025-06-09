# Evaluación Pandas y Numpy
### Materia: 
### Extracción de Conocimiento en Bases de Datos
### Alumnos: 
### Citlali Hernández Pérez, Gustavo Del Razo Rivera, Said Isaac León Lara y Fernando Antonio Vargas Velazquez

# 1.- Carga de datos
### 1.1 Cargar archivos csv:
### Permite al usuario importar archivos CSV para su análisis. El archivo se convierte en un DataFrame, que es una estructura tabular proporcionada por Pandas, adecuada para manipular datos estructurados.

# 2.- Preparación de datos
### 2.1 Mostrar primeras N líneas:
* Muestra las primeras N filas del dataset utilizando head(n), útil para tener una vista rápida de los datos al inicio.
### 2.2 Mostrar las últimas N líneas:
### Permite visualizar las últimas N filas con tail(n), útil para revisar registros al final del dataset.
### 2.3 Información básica del csv:
### Muestra detalles como tipo de datos, número de valores no nulos y uso de memoria con el método info().
### 2.4 Lista de columnas:
### Muestra todos los nombres de columnas presentes en el DataFrame.
### 2.5 Forma del dataset:
### Indica cuántas filas y columnas tiene el dataset con .shape, lo cual ayuda a conocer la dimensión general de los datos.
### 2.6 Descripción del dataset:
### Utiliza describe() para mostrar estadísticas descriptivas como media, desviación estándar, mínimo, máximo y percentiles de columnas numéricas.

# 3.- Selección de datos
### 3.1 Seleccionar 1 columna:
### Extrae una sola columna del DataFrame, devolviendo una Serie.
### 3.2 Seleccionar N columnas:
### Permite seleccionar múltiples columnas específicas, devolviendo un nuevo DataFrame con solo esas columnas.

# 4.- Filtrar filas
### 4.1 Filtrar filas con condición >, <, == :
### Filtra los datos aplicando condiciones lógicas sobre una o varias columnas.
