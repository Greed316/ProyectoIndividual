from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from starlette.responses import RedirectResponse
import pandas as pd


## cargamos el 
def cargardf(valor):   

    amazon='csv/amazon_prime_titles'
    netflix ='csv/netflix_titles'
    disney='csv/disney_plus_titles'
    hulu='csv/hulu_titles'
    archivos = [amazon,netflix,disney,hulu]
    df = pd.read_csv(netflix+".csv")
    if valor == "amazon":
      df = pd.read_csv(amazon+".csv")
    if valor == "hulu":
      df = pd.read_csv(hulu+".csv")
    if valor == "todos":
       lista_df = []
       for archivo in archivos:
            df1 = pd.read_csv(archivo+".csv")
            lista_df.append(df1)

       df = pd.concat(lista_df)

    return df

def cargarratings():
  ac1='ratings/1'
  ac2='ratings/2'
  ac3='ratings/3'
  ac4='ratings/4'
  ac5='ratings/5'
  ac6='ratings/6'
  ac7='ratings/7'
  archivos = [ac1,ac2,ac3,ac4,ac5,ac6,ac7]
  lista_df = []
  for archivo in archivos:
              df1 = pd.read_csv(archivo+".csv")
              lista_df.append(df1)

  df = pd.concat(lista_df)
  df = df.rename(columns={'movieId': 'id'})
  df = df.rename(columns={'rating': 'score'})
  return df

app = FastAPI()

@app.get("/",tags=["Menu"])
async def menu():
    return RedirectResponse(url="/docs/")


#Pelicula con mayor duracion segun año, plataforma y tipo de duracion

@app.get('/getmax_duration/{anio}/{plataforma}/{dtype}', 
          tags=["Pelicula con mayor duracion"])
def get_max_duration(anio: int,plataforma: str,dtype:str):
   
  df=cargardf(plataforma)
  year=anio
  df = df[df["type"] == "movie"]
  df = df[df["release_year"]==year]
  df['duration_type'] = df['duration_type'].str.strip()
  df['duration_type'] = df['duration_type'].astype(str)
  df = df[df["duration_type"]== dtype]
  df = df.sort_values('duration_int', ascending=False)
  pelicula=df['title'].iloc[0]

  return{
     'pelicula':pelicula
  }


#Candad de peliculas segun plataforma

@app.get('/get_score_count/{plataforma}/{scored}/{anio}',
          tags=["Cantidad de Peliculas mayores a Score:"])
def get_score_count(plataforma:str, score: float, anio:int):
    dfplataforma=cargardf(plataforma)
    year=anio
    puntaje=score
    dfplataforma = dfplataforma[dfplataforma["type"] == "movie"]
    dfplataforma = dfplataforma[(dfplataforma["score"] > puntaje) & (dfplataforma["release_year"] == year)] 
    respuesta = len(dfplataforma["title"])
    return {
            'plataforma': plataforma,
            'cantidad': respuesta,
            'anio': anio,
            'score': puntaje
        }


#Cantidad peliculas por plataforma
@app.get("/get_count_platform/{plataforma}",
         tags=["Cantidad de películas por plataforma"])
def get_count_platform(plataforma:str):
    df = cargardf(plataforma) 
    df = df[df["type"] == "movie"]
    peli_unicas= df["title"].nunique()
    
    return{
        "plataforma": plataforma,
        "peliculas": int(peli_unicas)
    }

#Actor que mas se repite segun plataforma y año

@app.get("/get_actor/{plataforma}/{anio}",
         tags=["Actor que más se repite según plataforma y año."])
async def get_actor(plataforma:str,anio:int):
    df=cargardf(plataforma)
    df = df[df["release_year"] == anio]
    df = df.dropna(subset=['cast'])
    actor_count=df["cast"].str.split(', ')
    lista_completa = actor_count.explode().tolist()
    conteo = pd.Series(lista_completa).value_counts()
    actor_mas_repetido=conteo.index[0]
    numero_de_veces=conteo.iloc[0]
   
    return{
        
        "Plataforma":plataforma,
        "anio":anio,
        "Actor": str(actor_mas_repetido),
        "Apariciones": int(numero_de_veces)
        
    }


#Cantidad de Contenido/Productos por tipo de rating

@app.get('/get_contents/{rating}',
            tags=["Cantidad de Contenido/Productos por rating"])
async def get_contents(rating: str):
    df=cargardf("todos") 
    df = df[df["rating"] == rating]
    productos=df["title"].nunique()

    return {'rating': rating, 'contenido': productos}

#Cantidad contenido/productos por año

@app.get('/prod_per_coutry/{tipo}/{pais}/{anio}',
          tags=["Cantidad de Contenido/Productos por año"])

async def prod_per_country(tipo: str, pais: str, anio: int):
    df=cargardf("todos")
    df = df[df["type"] == tipo]
    df = df[df["release_year"]==anio]
    df = df[df["country"]==pais]
    peliculas=df["title"].nunique()
    return {
        
        'pais': pais, 
        'anio': anio, 
        'peliculas': peliculas
    }


