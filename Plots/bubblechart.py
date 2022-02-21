import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

new_df = df.groupby(['month']).agg({'average_max_temp': 'max', 'average_min_temp': 'min'}).reset_index()

data = [
    go.Scatter(x=new_df['month'],y=new_df['average_max_temp'], text=new_df['average_max_temp'], mode='markers', marker=dict(size=new_df['average_max_temp'], color=new_df['average_max_temp'], showscale=True)),
    go.Scatter(x=new_df['month'],y=new_df['average_min_temp'], text=new_df['average_min_temp'], mode='markers', marker=dict(size=new_df['average_min_temp'], color=new_df['average_min_temp'], showscale=True))
]

# Preparing layout
layout = go.Layout(title="Corona Virus Confirmed Cases", xaxis_title="Recovered Cases", yaxis_title="Unrecovered Cases", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')