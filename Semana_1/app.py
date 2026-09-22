# Archivo base para el despliegue del Agente en Streamlit

#Importar librerias
import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

#En streamlist vamos a aagregar un titulo para la pagina web
st.title("Configuracion inicial")
#Agregamos un textbox en la pagina web
st.write("Primera prueba de uso de streamlit y ambiente de MA2026")

#El slider de streamlist me permite ingresar por un slider el parametro inversion 
gasto=st.slider("Seleccine nivel de gasto en publicicdad", 10,200,50)

#Variables del modelo
variable_x = np.array([[10], [20], [30], [40],[50]])
variable_y = np.array([15,25,35,45,55])

#Entrenamiento del modelo
modelo_lr = LinearRegression()
modelo_lr.fit(variable_x,variable_y)

#Crea boton que dice Predecir, al dar click ejecuta las lineas del IF
if st.button("Predecir"):
 resultado = modelo_lr.predict([[gasto]])
    #Muestra mensaje de exito
    st.success(f"Las ventas proyectadas para una inversion de ${gasto} son: ${resultado[0]}")
