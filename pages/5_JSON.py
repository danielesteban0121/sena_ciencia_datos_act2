import streamlit as st
import pandas as pd

st.title("Carga de datos: Archivos JSON")

st.markdown("""
### Ejercicio
JSON es el formato preferido en el desarrollo web para intercambiar información. 

1. Crea manualmente en la carpeta de tu proyecto un pequeño archivo llamado `catalogo_juegos.json`. 
   El archivo debe contener una lista (arreglo) de diccionarios, donde cada diccionario represente un videojuego con claves como `"Titulo"`, `"Año"`, y `"Consola"`. Añade al menos 3 videojuegos a la lista.
2. Lee este archivo utilizando Pandas y almacénalo en un DataFrame llamado `df_json`.
3. Muestra el DataFrame en la aplicación usando `st.dataframe()`.
""")

st.subheader("Tu resultado:")
# ESTUDIANTE: Escribe tu código a continuación

json_path = "catalogo_juegos.json"

try:
   df_json = pd.read_json(json_path)
   st.dataframe(df_json)
except FileNotFoundError:
   st.error(f"No se encontró el archivo {json_path}. Crea el archivo con una lista de diccionarios JSON en la carpeta del proyecto.")
except ValueError as e:
   st.error(f"Error al interpretar el JSON: {e}")
except Exception as e:
   st.error(f"Ocurrió un error leyendo el JSON: {e}")


# st.dataframe(...)
