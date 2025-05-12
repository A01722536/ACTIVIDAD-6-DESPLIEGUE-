# Cada que hagamos un cambio en el dashboard debo de cargar esta celda
# Es importante hacer cada modificación en esta misma celda
######################################################################
# Importamos librerías
import streamlit as st 
import plotly.express as px
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
######################################################################
# Definimos la instancia
@st.cache_resource
def load_data():
    # Lectura de archivo csv
    df = pd.read_csv('DataAnalytics (1).csv')
    # Eliminamos 'fecha' de las variables categóricas
    Lista = ['color presionado', 'mini juego', 'dificultad', 'Juego']
    Usuario = ['ADRIAN', 'ALEIDA', 'ARLETT', 'ASHLEY', 'AUSTIN']
    return df, Lista, Usuario

######################################################################
# Cargo los datos de la función "load_data"
df, Lista, Usuario = load_data()
######################################################################
#Mostrar una imagen en la parte superior del DF
#st.sidebar.image("Wuppi", width=200)

# CREACIÓN DEL DASHBOARD
# Generamos las páginas que generaremos en el diseño
######################################################################
st.sidebar.title("ANÁLISIS UNIVARIADO WUPPI")

# Widget 1: Selectbox para seleccionar la página
View = st.sidebar.selectbox(
    label="Tipo de Análisis", 
    options=["Extracción de Características", "Regresión Lineal", "Regresión No Lineal", "Regresión Logistica", "ANOVA"]
)

# Contenido de la Vista 1: Extracción de características
if View == "Extracción de Características":
    # Selectbox para elegir variable categórica
    Variable_Cat = st.sidebar.selectbox(label="Variables", options=Lista)
    # Selectbox para elegir usuario
    Usuario_sel = st.sidebar.selectbox(label="Usuario", options=Usuario)

    # Filtrar por usuario seleccionado
    df_usuario = df[df['Usuario'] == Usuario_sel]

    # Obtener la frecuencia de las categorías de la variable seleccionada
    Tabla_frecuencias = df_usuario[Variable_Cat].value_counts().reset_index()
    Tabla_frecuencias.columns = ['categorias', 'frecuencia']

    # Encabezado principal
    st.title("Extracción de Características")

    # Layout con dos columnas
    Contenedor_A, Contenedor_B = st.columns(2)

    # Gráfico de Barras
    with Contenedor_A:
        st.write("Gráfico de Barras")
        figure1 = px.bar(
            data_frame=Tabla_frecuencias, 
            x='categorias', 
            y='frecuencia', 
            title='Frecuencia por categoría'
        )
        figure1.update_xaxes(automargin=True)
        figure1.update_layout(height=300)
        st.plotly_chart(figure1, use_container_width=True)

    # Gráfico de Pastel
    with Contenedor_B:
        st.write("Gráfico de Pastel")
        figure2 = px.pie(
            data_frame=Tabla_frecuencias, 
            names='categorias', 
            values='frecuencia', 
            title='Frecuencia por categoría'
        )
        figure2.update_layout(height=300)
        st.plotly_chart(figure2, use_container_width=True)



        #Fila 2
    Contenedor_C, Contenedor_D = st.columns(2)
    with Contenedor_C:
        st.write("Gráfico de anillo o dona")
        #GRAPH 3: DONUT PLOT
        #Despliegue de un donut plot, definiendo las variables "x categorias" y "Y numericas"
        figure3=px.pie(data_frame=Tabla_frecuencias, names='categorias', values='frecuencia', hole=0.4, title=str('Frecuencia por categoria'))
        figure3.update_layout(height=300)
        st.plotly_chart(figure3, use_container_width=True)
    
    with Contenedor_D:
        st.write("Gráfico de área")
        #GRAPH 4: AREA PLOT
        #Despliegue de un donut plot, definiendo las variables "x categorias" y "Y numericas"
        figure4= px.area(data_frame=Tabla_frecuencias, x='categorias', y='frecuencia', title= str('Frecuencia por categoría'))
        figure4.update_layout(height=300)
        st.plotly_chart(figure4, use_container_width=True)
    
        # Fila 3
    Contenedor_E, Contenedor_F = st.columns(2)

    with Contenedor_E:
        st.write("Mapa de calor (Heatmap)")
        df_numericas = df_usuario.select_dtypes(include='number')
        if len(df_numericas) > 0:
            fig5, ax = plt.subplots(figsize=(6, 4))
            sns.heatmap(df_numericas.corr(), annot=True, cmap="YlGnBu", ax=ax)
            st.pyplot(fig5)

    with Contenedor_F:
        st.write("Visualizar tabla numérica")
        if st.checkbox("¿Mostrar tabla con variables numéricas?"):
            st.dataframe(df_numericas)