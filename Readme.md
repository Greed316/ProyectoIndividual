<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`"MLOps Engineer" (Data Engineer & Machine Learning)`**</h1>

# <h1 align=center>**`Por JAVIER HORACIO VILCA MARTINEZ`**</h1>







## **Procesamiento de los Datos **

Comenzando con la limpieza de los datos creamos las variables necesarias para poder cargar de forma iterativa los datos  de la carpeta Datasets y de la misma empezar con la limpieza con los requerimientos que se nos pidió.


+ Creamos la columna ID con los requerimientos pedidos

<p align=center>
<<img src = 'img/1.png' ><p>


<br/>

+ Reemplazamos valores nulos de la columna rating por G

<p align=center>
<<img src = 'img/2.png' ><p>


<br/>

+ Cambiamos el formato de los datos de la columna date_added que es de tipo datetime

<p align=center>
<<img src = 'img/3.png' ><p>


<br/>

+ Los campos de tipo texto se transformaron en **minúsculas**, en todas las columnas

<p align=center>
<<img src = 'img/4.png' ><p>


<br/>

+ Separamos la columna duration en dos columnas duration_int donde ingresaremos los valores numéricos y duration_type su tipo de duración

<p align=center>
<<img src = 'img/5.png' ><p>


<br/>

<p align=center>
<<img src = 'https://learn.microsoft.com/es-es/azure/architecture/data-guide/images/etl.png' height=300><p>


<br/>

**`Desarrollo API`**:  A continuación, pasamos a crear la Api mediante el uso de fastapi primero creamos el entorno virtual creamos el archivo main.py que es el archivo principal donde realizaremos las consultas
dentro del archivo importamos las librerías necesarias para poder realizar las consultas
fastapi que es el framework, pandas que utilizaremos para trabajar con dataframes, RedirectResponse que usamos para redireccionar
Creamos el objeto y a continuación creamos las rutas y las funciones que responden a las rutas solicitadas dentro de las mismas tenemos:

+ Película (sólo película, no serie, etc) con mayor duración según año, plataforma y tipo de duración

<p align=center>
<<img src = 'img/6.png' ><p>


<br/>

+ Cantidad de películas  según plataforma, con un puntaje mayor a XX en determinado año

<p align=center>
<<img src = 'img/7.png' ><p>


<br/>

+ Cantidad de películas según plataforma

<p align=center>
<<img src = 'img/8.png' ><p>


<br/>

+ Actor que más se repite según plataforma y año.

<p align=center>
<<img src = 'img/9.png' ><p>


<br/>

+ La cantidad de contenidos/productos que se publicó por país y año.

<p align=center>
<<img src = 'img/10.png' ><p>


<br/>

+ La cantidad total de contenidos/productos según el rating de audiencia .

<p align=center>
<<img src = 'img/11.png' ><p>


<br/>

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

Cargar el dataset que contiene información sobre las películas y las puntuaciones de los usuarios.
<p align=center>
<<img src = 'img/12.png' ><p>

<br/>
<p align=center>
<<img src = 'img/13.png' ><p>

<br/>
<p align=center>
<<img src = 'img/14.png' ><p>

<br/>

Calcular la matriz de similitud entre las películas basándose en las puntuaciones de los usuarios. Para ello, se puede utilizar una técnica como el cosine similarity.

<p align=center>
<<img src = 'img/15.png' ><p>

<br/>
<p align=center>
<<img src = 'img/16.png' ><p>

<br/>
<p align=center>
<<img src = 'img/17.png' ><p>

<br/>

<br/>
<p align=center>
<<img src = 'img/18.png' ><p>

<br/>

Definir la función get_recommendation(titulo: str) que tomará como entrada el título de la película y devolverá una lista con las 5 películas más recomendadas.




<br/>

<p align=center><<img src = 'img/19.png'><p>
<br/>


______
La parte de ML tuve problemas con el render y para que la api funcionara de la mejor manera esta el codigo sin implementacion
______
