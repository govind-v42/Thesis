from statistics import mean
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc


# Load the dataset
avocado = pd.read_excel('data/Test.xlsx')
x1 = mean(avocado['Value'])
avocado2 = pd.read_excel('data/Control_Test.xlsx')
x2 = mean(avocado2['Value'])
avocado3 = pd.read_excel("C:/Users/govin/Downloads/P5QuestionnaireChefMenage_version1.xls")

# Create the Dash app
app = Dash()

# Set up the app layout
geo_dropdown = dcc.Dropdown(options=avocado['Unit'].unique(),
                            value='%RH')

app.layout = html.Div(children=[dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Page 1", href="/page1")),
                dbc.NavItem(dbc.NavLink("Page 2", href="/page2")),
            ] ,
            brand="Multipage Dash App",
            brand_href="/page1",
            color="dark",
            dark=True,
        ), 
    html.H1(children='Timeseries Dashboard'),
    html.H2(children=f'Average RH Value Intervention: {x1}'),
    geo_dropdown,
    dcc.Graph(id='price-graph'),
    
    html.Div(children = [
        html.H1(children = 'Control Group'),
        html.H2(children=f'Average RH Value Control: {x2}'),
        dcc.Graph(id='price-graph2'), 
        
        html.Div(children = [
            html.H1(children = 'Geodis'),
            # html.H2(children=f'Average RH Value Control: {x2}'),
            dcc.Graph(id='gofig')
        ])
    ])
    
])
    
# ])

# app.layout = html.Div(children=[  
#         html.H1(children='Hello Dash'),
#         html.Div(children='Dash: A web application framework for your data.')
#                     ])


# Set up the callback function
@app.callback(
    Output(component_id='price-graph', component_property='figure'),
    Output(component_id='price-graph2', component_property='figure'),
    Output(component_id='gofig', component_property='figure'),
    Input(component_id=geo_dropdown, component_property='value')
)
def update_graph(selected_geography):
    filtered_avocado = avocado[avocado['Unit'] == selected_geography]
    line_fig = px.line(filtered_avocado,
                       x='Date/Time', y='Value',
                    #    color='type',
                       title=f'Intervention series in {selected_geography}')
    filtered2 = avocado2[avocado2['Unit'] == selected_geography]
    line_fig2 = px.line(filtered2,
                       x='Date/Time', y='Value',
                    #    color='type',
                       title=f'Control series in {selected_geography}')
    
    fig = go.Figure(data=go.Scattergeo(
        lon = avocado3['gps__Longitude'],
        lat = avocado3['gps__Latitude']
        # text = df['text'],
        # mode = 'markers',
        # marker_color = df['cnt'],
        ))
    fig.update_layout(
        title = 'Plot of Houses',
        # resolution=110,
        geo_scope='africa',
    )
    
    return line_fig, line_fig2, fig


# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)
    
