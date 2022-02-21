import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

data = [go.Heatmap(x=df['day'], y=df['month'],z=df['record_max_temp'].values.tolist(),
                   colorscale='Jet')]

# Preparing layout
layout = go.Layout(title='Recorded Max Temperature', xaxis_title="Day of Week", yaxis_title="Month of Year")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmap.html')