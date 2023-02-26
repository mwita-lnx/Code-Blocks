# create a streamlit app that will take input for the model in te hackathon.ipynb file
# and display the output

import streamlit as st
import pandas as pd
import numpy as np
import pickle

#load the model from the pickle file
model = pickle.load(open('model6.pkl','rb'))


# create a function that will take the inputs from the user
def predict_default(Year,Country,Item,Rainfall,Temperature,Pestisides):
    
    if Country =='Angola':
        Country= 1
    elif Country == 'Botswana':
            Country  = 2
    elif Country == 'Burundi':
            Country  = 3      
    elif Country == 'Cameroon':
            Country  = 4
    elif Country == 'Sudan':
            Country  = 23
    elif Country == 'Egypt':
            Country  = 6
    elif Country == 'Mali':
            Country = 18

    elif Country == 'Malawi':
           Country = 16

    elif Country == 'Libya':
           Country  = 15
    elif Country == 'Niger':
            Country  = 20
    elif Country == 'Uganda':
           Country  = 27
    elif Country == 'Senegal':
            Country  = 21
    elif Country == 'Turkey':
            Country = 26
    elif Country == 'Eritrea':
            Country  = 7
    elif Country == 'Kenya':
            Country  = 13
    else:
       Country = 0
    if Item == 'Carots':
           Item = 2
    elif Item == 'Cauliflowers':
           Item = 3
    elif Item == 'Barley':
           Item = 0
    elif Item == 'Onions':
           Item = 9
    elif Item == 'Wheat':
           Item = 13
    elif Item == 'Sweet Potatoes':
           Item = 10
    elif Item == 'Maize':
           Item = 7
    elif Item == 'Ginger':
           Item = 5
    else:
       item = 0

    

 
    # Making predictions 
    prediction = model.predict( [Year,Country,Item, Rainfall,Temperature,Pestisides])

    # set prediction whole number integer
    prediction = int(prediction)

    return prediction

# main function
def main():
    st.title('''CROP YIELD PREDICTOR FOR SUB SAHARAN COUNTRIES''')
    Year = st.number_input('Input Year')
    Rainfall = st.number_input('Input amount of rainfall per year in mm ')
    Item = st.selectbox("choose the appropriae temparature",("Maize","Wheat","Ginger", "Sweet Potatoes", "Onions", "Carots","Cauliflowers","Barley"))
    Temperature = st.number_input('Insert Temperature in Celsius')
    Pesticides = st.number_input('Input amount of pestisides in tonnes per ha ')
    Country = st.selectbox("choose the appropriae type",('Kenya','Eritrea', 'Sudan', 'Niger', 'Nigeria', 'Burundi','Libya', 'Malawi', 'Angola','Egypt','Botswana'))
    button = st.button('Predict Yield')
    if button:
        prediction = predict_default(Year,Country,Item, Rainfall,Temperature,Pesticides)
        st.success('The total yield predicted is(tonnes):{}'.format(prediction))

if __name__ == '__main__':
    main()
