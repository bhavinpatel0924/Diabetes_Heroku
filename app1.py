#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:00:39 2021

@author: bhavinpatel
"""
from sklearn.ensemble import RandomForestClassifier
import streamlit as st
import pickle


from PIL import Image

pickle_in = open("rfc.pkl","rb")
rfc = pickle.load(pickle_in)

#def home():
    #return "Welcome to Diabetes Predictor"


def predict_diabetes(Pregnancies,Glucose,
                     BloodPressure
                     ,SkinThickness,
                     Insulin,BMI,DiabetesPedigreeFunction,
                     Age):
    
    """Use This For Diabetes Prediction
    This is using docstrings for specifications.
    
    ---
    
    parameters:
        - name: Pregnancies
            in: query
            type: number
            required: true
        - name: Glucose
            in: query
            type: float
            required: true
        - name: BloodPressure
            in: query
            type: float
            required: true
        - name: SkinThickness
            in: query
            type: float
            required: true
        - name: Insulin
            in: query
            type: float
            required: true
        - name: BMI
            in: query
            type: float
            required: true
        - name: DiabetesPedigreeFunction
            in: query
            type: float
            required: true
        - name: Age
            in: query
            type: number
            required: true
    responses:
        200:
            description: Predicted Value
            
    """
    
    pred = rfc.predict([[Pregnancies,Glucose,
                     BloodPressure
                     ,SkinThickness,
                     Insulin,BMI,DiabetesPedigreeFunction,
                     Age]])
    print(pred)
    return pred



def main():
    st.title("Diabetes Predictor")
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Diabetes Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Pregnancies = st.text_input("Pregnancies","Type Here")
    Glucose = st.text_input("Glucose","Type Here")
    BloodPressure = st.text_input("BloodPressure","Type Here")
    SkinThickness = st.text_input("SkinThickness","Type Here")
    Insulin = st.text_input("Insulin","Type Here")
    BMI = st.text_input("BMI","Type Here")
    DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction","Type Here")
    Age = st.text_input("Age","Type Here")
    result=""
    if st.button("Predict"):
        result = predict_diabetes(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        if result == 0:
            result = 'No Diabetes'
        else:
            result = 'You Have Diabetes'
    st.success('Diabetes Prediction: {}'.format(result))
    
if __name__=='__main__':
    main()
        
