# import libaries
import streamlit as st
import pandas as pd
import plotly.express as px

# header
st.header('Web App: Vehicle Sales')

# cache the loaded data: reuse data across runs
#@st.cache_data

df = pd.read_csv('vehicles_cleaned.csv')


# load *.csv file into dataframes from my GitHub repository 
#try:
#    df = pd.read_csv('vehicles_cleaned.csv')
#except:
#    df = pd.read_csv('https://practicum-content.s3.us-west-1.amazonaws.com/datasets/vehicles_us.csv')
#    df = pd.read_csv('https://github.com/MelvicTN/SW_Development_Tool.git')







# DATA VISUALIZATION-Histogram-1: Vehicles Sale Days Posted by Condition
fig_histogram_1 = px.histogram(df, x="days_listed", nbins=90, color='condition', title='Vehicles Sale Days Posted by Condition', hover_data=['model_year', 'make', 'model_name'])

# Display the plot using streamlit
st.title('Histogram-1: Vehicles Sale Days Posted by Condition')
st.plotly_chart(fig_histogram_1)



# checkbox task/create
show_histogram = st.checkbox('Show Histogram')

# x = x-axos, labels = checkbox options, yaxis
if show_histogram:
    fig_histogram_1 = px.histogram(df, x='days_listed', title='Vehicle Condition', labels={'conditions':'Car Type'})
    #fig.update_layout(yaxis_title="Amount in Stock")
    st.plotly_chart(fig_histogram_1)





# DATA VISUALIZATION-Histogram: Manufactuer Breakdown by Vehicle Type
fig_histogram_2 = px.histogram(df, x="make", color="type", title='Manufacturer Breakdown by Vehicle Type').update_xaxes(categoryorder='total descending')

# Display the plot using streamlit
st.title('Histogram-2: Vehicles Sale Days Posted by Condition')
st.plotly_chart(fig_histogram_2)





# DATA VISUALIZATION-Scatter Plot-1: Vehicle Condition by Price
fig_scatter_1 = px.scatter(df, x="date_posted", y="price", color="condition", log_y=True,
                 size='days_listed', title='Vehicle Condition by Price', 
                 hover_data=['model_year', 'model_name', 'price', 'type', 'odometer'])

# Display the plot using streamlit
st.title('Scatter Plot-1: Vehicle Condition by Price')
st.plotly_chart(fig_scatter_1)





# DATA VISUALIZATION-Scatter Plot-2: Vehicle Sales Price by Milage and Transmission
fig_scatter_2 = px.scatter(df, x="odometer", y="price", color="transmission",
                 size='odometer', title='Scatter Plot: Vehicle Sales Price by Milage and Transmission', hover_data=['model_year', 'model_name', 'price', 'type', 'odometer'])

# Display the plot using streamlit
st.title('Scatter Plot-2: Vehicle Sales Price by Milage and Transmission')
st.plotly_chart(fig_scatter_2)


# Creating a st.checkbox is_4wd = Y/N
#st.checkbox('Vehicle is 4 Wheel Drvie')
is_4wd = st.checkbox('Vehicle is 4 Wheel Drvie')

# filter data set for vehicles that 4WD
y_4wd_filter = vehicles_df.query("is_4wd == 1")[['model_year', 'model_name', 'price', 'type', 'odometer', 'transmission']]

# new scatter/histogram plot when checked = update plot
if is_4wd:
    fig = px.scatter(y_4wd_filter, x="odometer", y="price", color="transmission", log_y=True,
                 size='odometer', 
                 title='Scatter Plot: Vehicle Sales Price by Milage and Transmission', 
                 hover_data=['model_year', 'model_name', 'price', 'type', 'odometer'])
    fig.show()

# original scatter/histogram plot when unchecked (default setting)
else:
    fig = px.scatter(df, x="odometer", y="price", color="transmission", log_y=True,
                 size='odometer', 
                 title='Scatter Plot: Vehicle Sales Price by Milage and Transmission', 
                 hover_data=['model_year', 'model_name', 'price', 'type', 'odometer'])
    fig.show()




# REFERENCE CODE: for checkbox
#show_histogram = st.checkbox('Show Histogram')

#if show_histogram:
#    fig = px.histogram(df, x='type', title='Stock of Car Type', labels={'type':'Car Type'})
#    fig.update_layout(yaxis_title="Amount in Stock")
#    st.plotly_chart(fig)