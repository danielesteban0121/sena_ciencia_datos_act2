import streamlit as st
import pandas as pd

st.title("Carga de datos: Archivos de Excel")

st.markdown("""
### Ejercicio
Es muy habitual recibir reportes corporativos en Excel (`.xlsx`).

1. Para leer Excel, es posible que necesites tener instalada la librería extra: `pip install openpyxl`.
2. Crea en tu computador un archivo Excel llamado `reporte_financiero.xlsx` con un par de registros de ingresos y gastos mensuales. Colócalo en la misma carpeta donde tienes tu proyecto.
3. Carga el archivo en un DataFrame llamado `df_excel`.
4. Muestra la tabla completa o al menos las columnas principales mediante `st.dataframe()`.
""")

st.info("💡 Nota: Asegúrate de tener el archivo Excel en la misma ruta antes de ejecutar, y si tienes problemas de lectura, prueba instalando openpyxl.")

st.subheader("Tu resultado:")
# ESTUDIANTE: Escribe tu código a continuación

excelArchi = "reporte_financiero.xlsx"

try:
    df_excel = pd.read_excel(excelArchi)
    st.dataframe(df_excel)
except FileNotFoundError:
    st.error(f"No se encontró el archivo {excelArchi}. Crea el archivo en la carpeta del proyecto.")
except Exception as e:
    st.error(f"Ocurrió un error leyendo el Excel: {e}")


# st.dataframe(...)
