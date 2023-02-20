import dash
from dash import dcc, html
import plotly.express as px
from statistics import mean
import pandas as pd

dash.register_page(__name__)

df = px.data.tips()

avocado = pd.read_excel('data/Test.xlsx')
x1 = mean(avocado['Value'])
line_fig = px.line(avocado,x='Date/Time', y='Value')
box1 = px.box(avocado,  y="Value")

avocado2 = pd.read_excel('data/Control_Test.xlsx')
x2 = mean(avocado2['Value'])
line_fig2 = px.line(avocado2,x='Date/Time', y='Value')
box2 = px.box(avocado2, y="Value")

layout = html.Div(
    [
        dcc.RadioItems(["Mudbrick", "Tin"], id='day-choice'),
        html.H3(children=f'Average RH Value Intervention: {x1}'),
        dcc.Graph(figure=line_fig),
        dcc.Graph(figure=box1),
        html.H3(children=f'Average RH Value Control: {x2}'),
        dcc.Graph(figure=line_fig2),
        dcc.Graph(figure=box2)
        
    ]
)