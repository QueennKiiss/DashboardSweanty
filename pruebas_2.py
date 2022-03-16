import dash
from dash import dcc
from dash import html

from dash.dependencies import Input, Output

# import plotly.express as px


# Data
# df = px.data.iris()

# Build App
app = dash.Dash(__name__)

app.layout = html.Div(
    className="body2",
    children=[
        html.Div(className="header2", children=html.H1("Header line")),
        html.Div(
            className="contentbody",
            children=[
                html.Div(
                    className="leftside",
                    children=[
                        html.A(children="Link", className="a"),
                        html.A(children="Link", className="a"),
                        html.A(children="Link", className="a")
                        ],
                    ),
                html.Div(
                    html.P("Right content"),
                    className="rightside"
                    )]
            )
        ]
    )

if __name__ == "__main__":
    app.run_server(debug=True)
