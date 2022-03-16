import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objects as go

# ====================================================
# CSS Styling
# ====================================================
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

header_text_md = '''
### Athlete studies: Know your sweat id(dentity) [SWEANTY](http://sweanty.tech)


Analyze the behavior of avocado prices
and the number of avocados sold in the US
between 2015 and 2018"
'''
# ====================================================
# Get data from csv file and treat them for displaying
# ====================================================
data = pd.read_csv("sweat_registers.csv")


# ====================================================
# Graphs
# ====================================================
def sweat_id_figure():
    fig = go.Figure(go.Indicator(
        align='left',
        mode="number+gauge+delta",
        gauge={'shape': "bullet",
               'bordercolor': 'saddlebrown',
               'borderwidth': 1,
               'bgcolor': colors['text']},
        value=220,
        delta={'reference': 300},
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "SWEAT ID", 'align': 'center'}))
    fig.update_layout(height=250)
    fig.update_layout(paper_bgcolor="black", font={'color': "darkblue", 'family': "Arial"})

    return fig


def bar_figure():
    fig = {
              "data": [
                  {
                      "x": data["user_name"],
                      "y": data["base_cond"],
                      "type": "bar",
                      "hovertemplate": "$%{y:.2f}" "<extra></extra>",
                  },
              ],
              "layout": {
                  "title": {
                      "text": "Base conductivity",
                      "align": "center"
                      # "x": 0.05,
                      # "xanchor": "left"
                  },
                  # "xaxis": {"fixedrange": True},
                  "yaxis": {
                      "tickprefix": "$",
                      "fixedrange": True,
                  },
                  "colorway": ["#17B897"],
              },
          },
    return fig


def salt_loss_figure():
    fig = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=100,
        mode="number+delta+gauge",
        title={'text': "Tendency to lose salt"},
        delta={'reference': 0},
        gauge={'axis': {'range': [None, 600]},
               'bar': {'color': 'lightgray'},
               'steps': [
                   {'range': [0, 200], 'color': "white"},
                   {'range': [200, 400], 'color': "lightblue"},
                   {'range': [400, 600], 'color': "blue"}]}))
    fig.update_layout(paper_bgcolor="gray", font={'color': "white", 'family': "Arial"})
    return fig


# ====================================================
# Dashboard development
# ====================================================
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = ['assests/styling.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Create layout for the dashboard
app.layout = html.Div(
    children=[
        # Main headers
        html.Div(
            children=[
                html.P(children="🥑", className="header-emoji", style={'textAlign': 'center'}),
                html.H1(
                    children="Sweanty Analytics",
                    className="header-title",
                    style={'textAlign': 'Center', 'color': colors['text']}
                ),
                html.P(
                    children="Athlete studies: Know your sweat id(dentity)",
                    className="header-description",
                    style={'textAlign': 'Center', 'color': colors['text']}
                ),
            ],
            className="header",
        ),
        html.Hr(),
        # Content
        html.Div(
            # style={'background': colors['text']},
            children=[
                html.Div([
                    html.Div("Aside probe", style={'color': 'white'}, className="four columns"),

                    ],
                    className="columns"
                ),
                html.Div([
                    html.Div(
                    # style={'background': colors['text'], 'width': '49%', 'float': 'center', 'padding': '10px'},
                        children=dcc.Graph(
                            id="salt losses",
                            config={"displayModeBar": False},
                            figure=salt_loss_figure()
                        ),
                        className="five columns",
                        style={'border': 'white', 'borderwidth': 2},
                    ),
                    html.Div(
                        # style={'background': colors['text'], 'width': '49%', 'float': 'center', 'padding': '10px'},
                        children=dcc.Graph(
                            id="salt losses 2",
                            config={"displayModeBar": False},
                            figure=salt_loss_figure()
                        ),
                        className="five columns",
                        style={'border': 'white', 'borderwidth': 2},
                    ),
                    html.Div(
                        # style={'background': colors['text']},
                        children=dcc.Graph(
                            style={'background': colors['text']},
                            id="base conductivity",
                            config={"displayModeBar": False},
                            figure=sweat_id_figure(),
                        ),
                        className="four columns",
                        # style={'width': '49%', 'float': 'right', 'display': 'inline-b', 'padding': '10px'},
                    ),
                    html.Div(
                        children=dcc.Graph(
                            style={'background': colors['text']},
                            id="conductivity",
                            config={"displayModeBar": False},
                            figure=sweat_id_figure(),
                        ),
                        className="four columns",
                        # style={'width': '49%', 'float': 'center', 'display': 'inline-b', 'padding': '10px',
                        #        'background': 'black'},
                    ),
                    ],
                    className="columns",
                    # style={'width': '49%', 'float': 'right', 'display': 'inline-b'},
                ),
            ],
            # className="content"
        ),
        # Final paragaph before footer
        html.Div(
            html.P("New paragraph between footer and figures"),
        ),
        # Footer
        html.Div(
            children=[
                html.Footer(children="SWEANTY footer", style={'textAlign': 'Center', 'color': colors['text']})
            ]
        ),
    ],
    style={'backgroundColor': colors['background']},
    # className=
)

if __name__ == "__main__":
    app.run_server(debug=True)
