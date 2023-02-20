import dash
from dash import dcc, html, dash_table, Dash, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go



dash.register_page(__name__, path='/')

df = pd.read_excel("C:/Users/govin/Downloads/baselineTable.xlsx")
avocado3 = pd.read_excel("C:/Users/govin/Downloads/P5QuestionnaireChefMenage_version1.xls")
fig = go.Figure(data=go.Scattergeo(lon = avocado3['gps__Longitude'], lat = avocado3['gps__Latitude']))
fig.update_layout(
    title = 'Plot of Houses',
    # resolution=110,
    geo_scope='africa',
)
    


layout = html.Div(
    [   dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns]),
        html.H1(children = 'Geodis'),
        dcc.Graph(figure=fig)
        
        # dcc.Dropdown([x for x in df.continent.unique()], id='cont-choice', style={'width':'50%'}),
        # dcc.Graph(id='line-fig',
        #           figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg'))
    ]
    
)


