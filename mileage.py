

import pickle
import streamlit as st
import numpy as np

def model_load():
    with open("mt.pkl","rb") as file:
        data = pickle.load(file)
    return data

data = model_load()

def app():
    st.title(""" Car Mileage Calculator """)
    st.image("miles.jpg")
    st.header("Please provide the following details to calculate the mileage of your car")
    
    cylinder = ("4","6","8")
    vs = ("V - Shaped"," Straight")
    am = ("Automatic Transmission","Manual Transmission")
    gear = ("3","4","5")
    carb = ("1","2","3","4","6","8")

    cylinders = st.selectbox("Number of Cylinders",cylinder)
    shape = st.selectbox("Engine Shape",vs)
    transmission = st.selectbox("Transmission Type",am)
    gears = st.selectbox("Number of Gears",gear)
    carbs = st.selectbox("Number of Carburators",carb)
    wt = st.slider("Weight of Car",1.51,5.42,2.0,step = 0.001,format = "%.2f")
    hp = st.number_input("Horse Power(in watts)",52,335,52)

    transmission = 0 if transmission == "Automatic Transmission" else 1
    shape = 0 if shape == "V - Shaped" else 1
    
    ok = st.button("Calculate Mileage")

    if ok:
        x = np.array([[cylinders,hp,wt,shape,transmission,gears,carbs]])
        x.astype(float)
        mileage = data.predict(x)
        st.subheader(f"Estimated Mileage in miles per gallon is {mileage[0]:.2f}")
        kmpl = mileage[0] * 0.425143707
        st.subheader(f"Estimated Mileage in kilometers per litre is {kmpl:.2f}")
app()