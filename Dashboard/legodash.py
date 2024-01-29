from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import os.path
import os

data_lego = os.path.join(os.pardir, 'LEGOSETS', r'lego_sets.csv')
data_dictionary = os.path.join(
    os.getcwd(), 'LEGOSETS', r'lego_sets_data_dictionary.csv')

df = pd.read_csv(data_lego)
df.columns = ['ID', 'Name', 'Year', 'Theme', 'Subtheme', 'Grouptheme',
              'Category', 'Pieces', 'Minifigs', 'Agerange_min',
              'Retail Price', 'Set url', 'Thumbnail url', 'Image url']

app = Dash(__name__)

# setting the colors for the dashboard
colors = {
    'background': '#DA291C',  # Lego: Red
    'offGrey': '#f8f9fa',  # off grey color
    'border': '#FFD700',  # Lego: Yellow
    'text': '#000000',  # Lego: Black
}

# style args of the sidebar
sidebar_style = {
    "position": "fixed",
    "border": "10px solid #FFD700",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": colors['offGrey'],
}

# style of the content to display
content_style = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Control Panel", className="display-4", style={
            'fontSize': '32px',
            'textAlign': 'center',
        }
        ),
        html.Hr(),
        html.P(
            "Lego Dashboard for Maven Analylitcs' Lego Challenge!",
            className="Lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                html.Br(),
                dbc.NavLink("Page One", href="/page-1", active="exact"),
                html.Br(),
                dbc.NavLink("Page Two", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=sidebar_style
)

content = html.Div(id="page-content", style=content_style)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the content of the home page!")
    elif pathname == "/page-1":
        return html.P("This is the content of page 1.")
    elif pathname == "/page-2":
        return html.P("This is the content of page 2.")

    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3"
    )


if __name__ == '__main__':
    app.run_server(debug=True)
