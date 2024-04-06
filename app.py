import pandas as pd
import plotly.express as px
import streamlit as st

# leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear las casillas de verificación
histograma = st.checkbox('Mostrar histograma')
grafico_dispersion = st.checkbox('Mostrar gráfico de dispersión')
grafico_pastel = st.checkbox('Mostrar gráfico de pastel')

# Contamos el tipo de vehiculo para el gráfico de pastel
tipo_vehiculo = car_data['type'].value_counts()

# Casilla de histograma
if histograma:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla de grafico de dispersión
if grafico_dispersion:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Casilla de grafico de pastel
if grafico_pastel:
    st.write('Distribución de tipos de vehículos')
    fig = px.pie(names=tipo_vehiculo.index, values=tipo_vehiculo.values,
                 title='Distribución de tipos de vehículos')
    st.plotly_chart(fig)
