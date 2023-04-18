<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>

# <h1 align=center>**`Por JAVIER HORACIO VILCA MARTINEZ`**</h1>





## **Descripción del problema (Contexto y rol a desarrollar)**

## Contexto

En el proyecto  se nos pide desarrollar una interfaz que permita que dos aplicaciones se comuniquen entre si por medio de una Api para la cual se nos recomendó utilizar el framework FastApi que permite construir Apis de alto rendimiento con Python para lo cual a los datos brindados se tendrán que aplicar transformaciones para luego los datos estén disponibles para su uso median la Api.
<p align=center>
<img src = 'https://camillovisini.com/assets/d8BwM0o5tE-600.ef9c55f8.jpeg' height=300><p>





## **Procesamiento de los Datos **

Comenzando con la limpieza de los datos creamos las variables necesarias para poder cargar de forma iterativa los datos  de la carpeta Datasets y de la misma empezar con la limpieza con los requerimientos que se nos pidió.


+ Creamos la columna ID con los requerimientos pedidos

+ Reemplazamos valores nulos de la columna rating por G

+ Cambiamos el formato de los datos de la columna date_added que es de tipo datetime

+ Los campos de tipo texto se transformaron en **minúsculas**, en todas las columnas

+ Separamos la columna duration en dos columnas duration_int donde ingresaremos los valores numéricos y duration_type su tipo de duración

<p align=center>
<<img src = 'https://learn.microsoft.com/es-es/azure/architecture/data-guide/images/etl.png' height=300><p>


<br/>

**`Desarrollo API`**:  A continuación, pasamos a crear la Api mediante el uso de fastapi primero creamos el entorno virtual creamos el archivo main.py que es el archivo principal donde realizaremos las consultas
dentro del archivo importamos las librerías necesarias para poder realizar las consultas
fastapi que es el framework, pandas que utilizaremos para trabajar con dataframes, RedirectResponse que usamos para redireccionar
Creamos el objeto y a continuación creamos las rutas y las funciones que responden a las rutas solicitadas dentro de las mismas tenemos:

+ Pelicula con mayor duracion

+ Obtener la cantidad de películas que tengan un puntaje, plataforma y año especifico

+ Cantidad de peliculas por plataforma

+ Actor que más se repite según plataforma y año.

<p align=center><<img src = 'https://amalgjose.files.wordpress.com/2021/02/fast_api_ppt.png' height=300><p>
<br/>





## **Análisis exploratorio de los datos: (Exploratory Data Analysis-EDA) **

<a href="plataformas_data_report.html.html">Informe generado por pandas profiling</a>

Podemos observar el informe que obtenemos al usar la herramienta pandas profiling del cual podemos sacar las siguientes conclusiones.


+ Muchos valores nulos

+ Mejorando el Dataset podriamos saber mas acerca de los actores mas populares dependiedo las series y peliculas

+ Con el score y duration_int se puede tener un parametro del tiempo mas recomendable para una serie o pelicula

+ Con Score y rating obtendriamos un parametro de que tipo rating es mas popular.



<br/>

<p align=center><<img src = 'https://editor.analyticsvidhya.com/uploads/74223Pandas%20Profiling.png' height=300><p>
<br/>




<br/>

## **Sistema de recomendación:**

Para el sistema de recomendacion se utilizo el modelo de aprendizaje SGD que es de los mas utilizados en el uso de modelos para recomendacion y gradio para su visualizacion.


<br/>

<p align=center><<img src = 'https://i.ytimg.com/vi/RiCQzBluTxU/maxresdefault.jpg' height=300><p>
<br/>


