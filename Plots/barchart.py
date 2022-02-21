import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

df = df.sort_values(by=['Total'], ascending=[False]).head(20).reset_index()

# Preparing data
trace1 = go.Bar(x=df['NOC'], y=df['Total'], name='Medals', marker={'color': '#CD7F32'})
data = [trace1]
layout = go.Layout(title='Total Medals in 2016 Olympics', xaxis_title='Countries', yaxis_title='Medals')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchart.html')