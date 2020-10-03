# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 20:12:10 2020

@author: Dibyaranjan
"""


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 


from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("Classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

def Predict_BMI(gender,height,weight):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: gender
        in: query
        type: number
        required: true
      - name: height
        in: query
        type: number
        required: true
      - name: weight
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[gender,height,weight]])
    print(prediction)
    return prediction
def main():
    #st.title("BMI Predictor")
    
    #st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)
    html_temp = """
    <div style="background-color:#9d65c9;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit BMI ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    option = st.selectbox( 'Please select your Gender', ('Male', 'Female'))
    if option == 'Male':
        option = 1
    else:
        option = 0
    height = st.text_input("Height in Cm","")
    weight = st.text_input("Weight in Kg","")
    result=""
    
    if st.button("Predict"):
        result=Predict_BMI(option,height,weight)
        
        if result==1:
            st.success('You are weak') 
        elif result==2:
            st.success('You are Normal') 
        elif result==3:
            st.success('You are Overweight') 
        elif result==4:
            st.success('You are Obesse') 
        elif result==5:
            st.success('You are Extremly Obesse') 
        else:
            st.success('You are Very weak') 

    #st.markdown("<h1 style='text-align: left; color: red; padding : 20px 0 0 0'>Some title</h1>", unsafe_allow_html=True)
    
    
if __name__=='__main__':
    main()
    
    
    
    