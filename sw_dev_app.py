# import libaries
import streamlit as st
import pandas as pd
import plotly.express as px

# load *.csv file into dataframes from my GitHub repository 
#try:
#    vehicles_df = pd.read_csv('vehicles_us.csv')
#except:
#    #vehicles_df = pd.read_csv('https://practicum-content.s3.us-west-1.amazonaws.com/datasets/vehicles_us.csv')
#    vehicles_df = pd.read_csv('https://github.com/MelvicTN/SW_Development_Tool.git')


# load *.csv file from GitHub repository


vehicles_df = pd.read('cleaned_vehicles_us.csv')