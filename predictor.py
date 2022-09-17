import streamlit as st
import pickle

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind
#import statsmodels.formula.api as smf

model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))

st.title("Selling Price Predictor ")
st.markdown("##### If you are a potential car seller\n##### Try evaluating the price you can get on your car here! ")
st.image("sellcar.png")

st.write('')
st.write('')

years = st.number_input('Year of Purchase', 1990, 2020, step=1, key='year')
Years_old = 2020 - years

Present_Price = st.number_input('Current ex-showroom price (In lakhs)', 0.00, 50.00,
                                step=0.5, key='present_price')

Kms_Driven = st.number_input('Distance driven (In Kilometers)', 0.00, 500000.00, step=500.00,
                                key='drived')

Owner = st.radio("Number of previous owners", (0, 1), key='owner')

Fuel_Type_Petrol = st.selectbox('Fuel type of the car ?', ('Petrol', 'Diesel', 'CNG'), key='fuel')
if (Fuel_Type_Petrol == 'Petrol'):
    Fuel_Type_Petrol = 1
    Fuel_Type_Diesel = 0
elif (Fuel_Type_Petrol == 'Diesel'):
    Fuel_Type_Petrol = 0
    Fuel_Type_Diesel = 1
else:
    Fuel_Type_Petrol = 0
    Fuel_Type_Diesel = 0

Seller_Type_Individual = st.selectbox('Are you a dealer or an individual ?', ('Dealer', 'Individual'), key='dealer')
if (Seller_Type_Individual == 'Individual'):
    Seller_Type_Individual = 1
else:
    Seller_Type_Individual = 0

Transmission_mode = st.selectbox('Transmission Type', ('Manual', 'Automatic'), key='Manual')
if (Transmission_mode == 'Manual'):
    Transmission_mode = 1
else:
    Transmission_mode = 0

if st.button("Estimated Selling Price", key='predict'):
    try:
        Model = model  # get_model()
        prediction = Model.predict([[Present_Price, Kms_Driven, Owner, Years_old, Fuel_Type_Diesel,
                                        Fuel_Type_Petrol, Seller_Type_Individual, Transmission_mode]])
        output = round(prediction[0], 2)
        if output < 0:
            st.warning("This car cannot be sold")
        else:
            st.success("This car can be sold for Rs. {} lakhs".format(output))
    except:
        st.warning("Something went wrong\n Please try again")
