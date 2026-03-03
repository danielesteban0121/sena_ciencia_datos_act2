import streamlit as st
import pandas as pd

st.title("Bases de Datos en la Nube: Firebase Firestore")

st.markdown("""
### Ejercicio
Firebase es otra opción excelente adoptada por múltiples startups para almacenar datos en tiempo real.

**Instrucciones:**
1. Asume que se te proporcionó un archivo de credenciales de servicio `llave_secreta.json`.
2. Escribe el **código teórico (usando st.code() o conectándote si tienes tu propia bd)** que emplearías con `firebase_admin` para arrancar la aplicación y obtener el cliente de la base de datos.
3. El objetivo sería conectarse a la colección `vehiculos` de tu Firestore y traer todos los documentos.
4. Indica cómo convertirías la respuesta iterando los documentos para extraer su `to_dict()`.
5. Convierte esa lista a un DataFrame `df_firebase` final.
""")

st.subheader("Tu resultado:")
st.markdown("Escribe en la parte de abajo el código que usarías para lograr el objetivo. Si usas código comentado/teórico, compártelo adentro de `st.code()`.")

# ESTUDIANTE: Escribe tu código a continuación

st.code("""
# Importar librerías necesarias
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# 1 Cargar archivo de credenciales
cred = credentials.Certificate("llave_secreta.json")

# 2 Inicializar la app de Firebase
firebase_admin.initialize_app(cred)

# 3 Obtener cliente de Firestore
db = firestore.client()

# 4 Acceder a la colección 'vehiculos'
coleccion = db.collection("vehiculos")

# 5 Obtener todos los documentos
docs = coleccion.stream()

# 6 Convertir documentos a lista de diccionarios
lista_documentos = []
for doc in docs:
    data = doc.to_dict()
    data["id"] = doc.id  # opcional: guardar el ID del documento
    lista_documentos.append(data)

# 7 Convertir a DataFrame
df_firebase = pd.DataFrame(lista_documentos)

# 8 Mostrar resultados
print(df_firebase.head())
""")