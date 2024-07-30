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
df = pd.read('vehicles_cleaned.csv')







# DATA VISUALIZATION: create a histogram using plotly express
#df = clean_VEH_df

fig = px.histogram(df, x="days_listed", nbins=90, color='condition', title='Histogram Days Listed', hover_data=['model_year', 'make', 'model_name'])
fig.show()






# DATA VISUALIZATION: create a histogram using plotly express
#df = clean_VEH_df
fig = px.histogram(df, x="make", color="type", title='Histogram: Make Breakdown by Vehicle Type').update_xaxes(categoryorder='total descending')
fig.show()





# DATA VISUALIZATION: create a scatter plot using plotly express
# Setting size and color with column names
#df = clean_VEH_df
fig = px.scatter(df, x="date_posted", y="price", color="condition",
                 size='days_listed', title='Scatter Plot: Vehicle Condition and Price by Vehicle Condition', hover_data=['model_year', 'model_name', 'price', 'type', 'odometer'])
fig.show()






# DATA VISUALIZATION: create a scatter plot using plotly express
# Setting size and color with column names
#df = clean_VEH_df
fig = px.scatter(df, x="odometer", y="price", color="transmission",
                 size='odometer', title='Scatter Plot: Vehicle Sales Price by Milage and Transmission', hover_data=['model_year', 'model_name', 'price', 'type', 'odometer'])

fig.show()