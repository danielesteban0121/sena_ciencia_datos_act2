import streamlit as st
import pandas as pd

st.title("Método 1: Juntando varias Series")

st.markdown("""
### Ejercicio
En este ejercicio debes crear un DataFrame agrupando información sobre **películas favoritas**.

1. Crea tres Series de Pandas diferentes:
    - Una serie llamada `titulos` con al menos 4 nombres de películas.
    - Una serie llamada `directores` con los directores de esas películas.
    - Una serie llamada `años` con el año de estreno.
2. Une estas tres series en un único DataFrame llamado `df_peliculas`, asignando nombres descriptivos a las columnas (por ejemplo: `Título`, `Director`, `Año de Estreno`).
3. Muestra el DataFrame en la aplicación usando `st.dataframe()`.
""")

st.subheader("Tu resultado:")
# ESTUDIANTE: Escribe tu código a continuación

titulos = pd.Series(["la bella y bestia", "pinocho", "avatar", "wakanda"])

directores = pd.Series(["ricardo dicaprio", "pitochico", "alma marlo goza", "pedro"])

años = pd.Series([2020, 2003, 2010, 2025])

df_peliculas = pd.DataFrame ({
    "Nombre de pelicula" : titulos,
    "Directores" : directores,
    "Años" : años
})

st.dataframe(df_peliculas)
