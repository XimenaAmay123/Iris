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
import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import streamlit.components.v1 as components
URL = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
dfIris = pd.read_csv(URL)

st.title("Visualizacion")

components.html(
        """<hr style="height:3px;border:none;color:#333;background-color:#333;" />""")
st.subheader(dfIris.columns[0])
fig = px.box(dfIris, y = dfIris.columns[0])
st.plotly_chart(fig, use_container_width=True)

st.subheader(dfIris.columns[1])
fig = px.box(dfIris, y = dfIris.columns[1])
st.plotly_chart(fig, use_container_width=True)

st.subheader(dfIris.columns[2])
fig = px.box(dfIris, y = dfIris.columns[2])
st.plotly_chart(fig, use_container_width=True)

st. subheader(dfIris. columns[3])
fig = px.box(dfIris, y = dfIris.columns[3])
st.plotly_chart(fig, use_container_width=True)
#dfiris.plot(kind='box',)

#import plotly.graph_objects as go

fig = go.Figure()

for col in dfIris:
    fig.add_trace(go.Box(y=dfIris[col].values, name=dfIris[col].name))
st.plotly_chart(fig, use_container_width=True)
st.subheader("Histogramas")
for i in range(0,len(dfIris.columns)):
     fig= px.histogram(dfIris, x=dfIris.columns[i])
     st.plotly_chart(fig,use_container_width=True)

st.subheader("Grafica de correlacion")

fig = px.scatter_matrix(dfIris,
                    dimensions= dfIris.columns[0:4],
                    color="variety")
st.plotly_chart(fig,use_container_width=True)
