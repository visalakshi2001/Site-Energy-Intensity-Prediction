import pickle
import streamlit as st
import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
from prediction import get_prediction



st.set_page_config(page_title='Site Energy Intensity Prediction', page_icon="⚡", 
                   layout="wide", initial_sidebar_state='expanded')

pickle_in = open('cb_model.pkl', 'rb') 
cb_model = pickle.load(pickle_in)


#creating option list for dropdown menu  

features = ['floor_area','year_built','energy_star_rating','ELEVATION','january_min_temp','january_max_temp','february_min_temp','february_max_temp',' march_min_temp','march_max_temp',
            'april_min_temp','april_max_temp','may_min_temp','may_max_temp','june_min_temp','june_max_temp',' july_min_temp',' july_max_temp',' august_min_temp','august_max_temp','september_min_temp',
            'september_max_temp','october_min_temp','october_max_temp','november_min_temp','november_max_temp','december_min_temp','december_max_temp',' cooling_degree_days',
            'heating_degree_days','snowfall_inches','days_below_20F','days_above_80F','direction_max_wind_speed','direction_peak_wind_speed','days_with_fog']


st.markdown("<h1 style='text-align: center;'>Site Energy Intensity Prediction App ⚡ </h1>", unsafe_allow_html=True)
def main():

    with st.form('prediction_form'):

        st.header("Enter the input for following features:")


        floor_area = st.slider('floor_area', 3000.0, 280000.0, value=3000.0, format="%f")
        year_built = st.slider('year_built', 1924.0, 2014.0, value=1924.0, format="%f")
        energy_star_rating = st.slider('energy_star_rating', 11.0, 100.0, value=11.0, format="%f")
        ELEVATION = st.slider('ELEVATION',1.0, 130.0, value=1.0, format="%f")
        january_min_temp = st.slider('january_min_temp', 1.0, 50.0, value=1.0, format="%f")
        january_max_temp = st.slider('january_max_temp',40.0, 100.0, value=40.0, format="%f")
        february_min_temp = st.slider('february_min_temp',1.0, 50.0, value=1.0, format="%f" )
        february_max_temp = st.slider('february_max_temp',30.0, 85.0, value=30.0, format="%f" )
        march_min_temp = st.slider('march_min_temp', 1.0, 15.0, value=1.0, format="%f")
        march_max_temp = st.slider('march_max_temp',50.0, 100.0, value=50.0, format="%f")
        april_min_temp = st.slider('april_min_temp', 10.0, 55.0, value=10.0, format="%f")
        april_max_temp = st.slider('april_max_temp',60.0, 105.0, value=60.0, format="%f")
        may_min_temp = st.slider('may_min_temp',20.0, 60.0, value=20.0, format="%f")
        may_max_temp = st.slider('may_max_temp',60.0, 115.0, value=60.0, format="%f")
        june_min_temp = st.slider('june_min_temp', 30.0, 70.0, value=30.0, format="%f")
        june_max_temp = st.slider('june_max_temp', 60.0, 120.0, value=60.0, format="%f")
        july_min_temp =  st.slider('july_min_temp',40.0, 75.0, value=40.0, format="%f")
        july_max_temp =  st.slider('july_max_temp',60.0, 120.0, value=60.0, format="%f")
        august_min_temp = st.slider('august_min_temp',30.0, 80.0, value=30.0, format="%f")
        august_max_temp =  st.slider('august_max_temp',60.0, 120.0, value=60.0, format="%f")
        september_min_temp = st.slider('september_min_temp',20.0, 70.0, value=20.0, format="%f")
        september_max_temp = st.slider('september_max_temp',60.0, 110.0, value=60.0, format="%f")
        october_min_temp = st.slider('october_min_temp',10.0, 75.0, value=10.0, format="%f")
        october_max_temp = st.slider('october_max_temp',60.0, 110.0, value=60.0, format="%f")
        november_min_temp = st.slider( 'november_min_temp',1.0, 60.0, value=1.0, format="%f")
        november_max_temp =  st.slider('november_max_temp',50.0, 100.0, value=50.0, format="%f")
        cooling_degree_days = st.slider('cooling_degree_days',500.0, 4000.0, value=500.0, format="%f")
        heating_degree_days = st.slider('heating_degree_days',300.0, 5000.0, value=300.0, format="%f")
        snowfall_inches = st.slider('snowfall_inches',0.0, 60.0, value=0.0, format="%f")
        days_below_20F = st.slider('days_below_20F',0.0, 100.0, value=0.0, format="%f")
        days_above_80F = st.slider('days_above_80F',1.0, 200.0, value=1.0, format="%f")
        direction_max_wind_speed = st.slider ('direction_max_wind_speed',200.0, 360.0, value=200.0, format="%f")
        direction_peak_wind_speed = st.slider ('direction_peak_wind_speed',200.0, 360.0, value=200.0, format="%f") 
        days_with_fog = st.slider('days_with_fog',30.0, 200.0, value=30.0, format="%f")










        submit_values = st.form_submit_button("Predict")

    if submit_values:    

        data = np.array(['floor_area','year_built','energy_star_rating','ELEVATION','january_min_temp','january_max_temp','february_min_temp','february_max_temp',' march_min_temp','march_max_temp',
            'april_min_temp','april_max_temp','may_min_temp','may_max_temp','june_min_temp','june_max_temp',' july_min_temp',' july_max_temp',' august_min_temp','august_max_temp','september_min_temp',
            'september_max_temp','october_min_temp','october_max_temp','november_min_temp','november_max_temp','december_min_temp','december_max_temp',' cooling_degree_days',
            'heating_degree_days','snowfall_inches','days_below_20F','days_above_80F','direction_max_wind_speed','direction_peak_wind_speed','days_with_fog']).reshape(1,-1)
              
 
       
         
        pred = get_prediction(data=data, model=cb_model)

        st.write(f"The predicted Site Energy Intensity is:  {pred}")


if __name__ == '__main__':
  main() 

        


