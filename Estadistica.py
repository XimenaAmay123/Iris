import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

URL = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
dfIris = pd.read_csv(URL)

st.title("Analisis estadistico Iris Dataset")

components.html(
                """<hr style="height: 3px;border:none; color:#333;background-color:#333;" />""")

st.dataframe(dfIris.head())

st.header("Estadisticas")
st.write("Filas, columnas:")
st.write(dfIris.shape)

st.write("Describe:")
st.dataframe(dfIris.describe())

st.write("clases")
st.write(dfIris["variety"].value_counts())
