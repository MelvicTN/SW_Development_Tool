# import libaries
import streamlit as st
import pandas as pd
import plotly.express as px

# header
st.header('Web App: Vehicle Sales')

# cache the loaded data: reuse data across runs
@st.cache_data
def load_data(rows):
    df = pd.read('vehicles_cleaned.csv')
    return df

# load *.csv file into dataframes from my GitHub repository 
#try:
#    df = pd.read_csv('vehicles_cleaned.csv')
#except:
#    df = pd.read_csv('https://practicum-content.s3.us-west-1.amazonaws.com/datasets/vehicles_us.csv')
#    df = pd.read_csv('https://github.com/MelvicTN/SW_Development_Tool.git')






# DATA VISUALIZATION-Histogram-1: Vehicles Sale Days Posted by Condition
#df = clean_VEH_df
fig_histogram_1 = px.histogram(df, x="days_listed", nbins=90, color='condition', title='Vehicles Sale Days Posted by Condition', hover_data=['model_year', 'make', 'model_name'])

#fig.show()
# Display the plot using streamlit
st.plotly_chart(fig_histogram_1)
st.title('Histogram-1: Vehicles Sale Days Posted by Condition')




# DATA VISUALIZATION-Histogram: Manufactuer Breakdown by Vehicle Type
#df = clean_VEH_df
fig_histogram_2 = px.histogram(df, x="make", color="type", title='Manufacturer Breakdown by Vehicle Type').update_xaxes(categoryorder='total descending')

#fig.show()
# Display the plot using streamlit
st.plotly_chart(fig_histogram_2)
st.title('Histogram-2: Vehicles Sale Days Posted by Condition')



# DATA VISUALIZATION-Scatter Plot-1: Vehicle Condition by Price
#df = clean_VEH_df
fig_scatter_1 = px.scatter(df, x="date_posted", y="price", color="condition", log_y=True,
                 size='days_listed', title='Vehicle Condition by Price', 
                 hover_data=['model_year', 'model_name', 'price', 'type', 'odometer'])

#fig.show()
# Display the plot using streamlit
st.plotly_chart(fig_scatter_1)
st.title('Scatter Plot-1: Vehicle Condition by Price')




# DATA VISUALIZATION-Scatter Plot-2: Vehicle Sales Price by Milage and Transmission
#df = clean_VEH_df
fig_scatter_2 = px.scatter(df, x="odometer", y="price", color="transmission",
                 size='odometer', title='Scatter Plot: Vehicle Sales Price by Milage and Transmission', hover_data=['model_year', 'model_name', 'price', 'type', 'odometer'])

#fig.show()
# Display the plot using streamlit
st.plotly_chart(fig_scatter_2)
st.title('Scatter Plot-2: Vehicle Sales Price by Milage and Transmission')



# REFERENCE CODE: for checkbox
st.checkbox