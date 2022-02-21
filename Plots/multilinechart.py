import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['Date'] = pd.to_datetime(df['date'])

# Preparing data
df = df.groupby(['month']).agg(
    {'actual_max_temp': 'max', 'actual_min_temp': 'min', 'actual_mean_temp': 'mean'}).reset_index()

trace1 = go.Scatter(x=df['month'], y=df['actual_max_temp'], mode='lines', name='Max Temp')
trace2 = go.Scatter(x=df['month'], y=df['actual_min_temp'], mode='lines', name='Min Temp')
trace3 = go.Scatter(x=df['month'], y=df['actual_mean_temp'], mode='lines', name='Mean Temp')
data=[trace1,trace2,trace3]

# Preparing layout
layout = go.Layout(title='Max Temp each Month', xaxis_title="Month", yaxis_title="Lines")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilinechart.html')