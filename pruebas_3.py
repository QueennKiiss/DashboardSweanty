import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go


# Data
def get_plot_data():
    df = pd.read_csv("sweat_registers.csv")

    if df['voltage'].dtype == 'object':
        df["voltage"] = df["voltage"].str.replace(',', '-').astype("float")
    if df['weight_initial'].dtype == 'object':
        df['weight_initial'] = df['weight_initial'].str.replace(',', '-').astype("float")
    if df['weight_final'].dtype == 'object':
        df['weight_final'] = df['weight_final'].str.replace(',', '-').astype("float")

    df['sweat_id'] = df['voltage']*0.023/0.011
    df['salt_amount'] = 9*(df['weight_initial']-df['weight_final'])*df['sweat_id']

    return df

# ====================================================
# Graphs
# ====================================================


def sweat_id_figure(data):
    fig = go.Figure(go.Indicator(
        mode="number",
        value=data,
        domain={'x': [0, 1], 'y': [0, 1]},
        ))
    fig.update_layout(
        font={'color': "white", 'family': "Arial"},
        margin=dict(l=0, r=0, t=50, b=10, pad=0),
        paper_bgcolor='cadetblue',
        title={
            'text': "Sweat ID",
            'font': {'size': 30},
            'xref': 'container',
            'x': 0.5,
            }
        )

    return fig


def salt_loss_figure(data):
    fig = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=data,
        mode="gauge",
        gauge={
            'shape': "bullet",
            'bordercolor': 'white',
            'borderwidth': 2,
            'axis': {
                'range': [None, 90],
                'tickmode': 'array',
                'tickvals': [15, 45, 75],
                'ticktext': ["Low", "Middle", "High"],
                'tickfont': {'size': 20},
                'tickcolor': 'white'
                },
            'bar': {'color': 'lightgray'},
            'steps': [
               {'range': [0, 30], 'color': "white"},
               {'range': [30, 60], 'color': "lightblue"},
               {'range': [60, 90], 'color': "blue"}]}),
        )
    fig.update_layout(
        font={'color': "white", 'family': "Arial"},
        title={
            'text': "Tendency to lose salt",
            'font': {'size': 30},
            'xref': 'container',
            'x': 0.25,
            },
        margin=dict(l=10, r=10, t=50, b=50, pad=4),
        paper_bgcolor='cadetblue',
        )
    return fig


def salt_amount(users, salt_amounts):
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=users, y=salt_amounts,
            name='base_cond',
            marker_color='lightblue'
            )
        )
    fig.update_layout(
        # height=500,
        margin=dict(l=20, r=20, t=40, b=20),
        title={
            'text': 'Salt amount',
            'font': {'size': 30},
            'xref': 'container',
            'x': 0.5,
            'y': 0.98,
            },
        xaxis_tickfont_size=14,
        xaxis=dict(
             tickfont_size=18,
            ),
        yaxis=dict(
            title='Salt amount (a.u.)',
            titlefont_size=22,
            tickfont_size=18,
            ),
        legend=dict(
            x=0, y=0.9,
            bordercolor='black',
            borderwidth=1
            ),
        barmode='group',
        bargap=0.15,  # gap between bars of adjacent location coordinates.
        bargroupgap=0.1,  # gap between bars of the same location coordinate.
        paper_bgcolor='cadetblue',
        plot_bgcolor='cadetblue',
        font={'color': 'white'}
        )
    return fig


def weight_figure(user, weight_before, weight_after):
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=[user], y=[weight_before],
            name='before',
            marker_color='lightblue'
            )
        )
    fig.add_trace(
        go.Bar(
            x=[user], y=[weight_after],
            name='after',
            marker_color='blue'
            )
        )
    fig.update_layout(
        font={'color': "white", 'family': "Arial"},
        title={
            'text': "Weight comparison",
            'font': {'size': 30},
            'xref': 'container',
            'x': 0.5,
            },
        xaxis=dict(
            tickfont_size=20,
            ),
        yaxis=dict(
            title='Weight (kg)',
            titlefont_size=22,
            tickfont_size=20,
            range=[0, 100]
            ),
        legend=dict(
            font={'size': 20}
            ),
        margin=dict(l=0, r=5, t=50, b=50, pad=4),
        paper_bgcolor='cadetblue',
        plot_bgcolor='cadetblue',
        )
    return fig


app = dash.Dash(__name__)

# Images and Icons
user_profile_img = app.get_asset_url("img/user_profile.png")
sweanty_icon = app.get_asset_url("img/logo_sweanty_1-184x81.png")
bewolfish_icon = app.get_asset_url("img/bewolfish_logo_color.png")

# Build App layout
app.layout = html.Div(
    id='body',
    className="body",
    children=[
        dcc.Interval(
            id='interval_data',
            interval=1 * 2000,  # in milliseconds
            n_intervals=0
        ),
        # HEADER
        html.Div(
            className='header',
            children=[
                html.Div(
                    className="cell",
                    children=[html.Img(className="icon_left", src=sweanty_icon)]
                    ),
                html.Div(
                    className="cell",
                    children=[html.H1(className="h1", children="SWEANTY-BEWOLFISH STUDY")],
                    ),
                html.Div(
                    className="cell",
                    children=[html.Img(className="icon_right", src=bewolfish_icon)]
                    ),
                ]
            ),
        # Main Content
        html.Div(
            className='row',
            children=[
                # LeftColumn
                html.Div(
                    className='leftcolumn',
                    children=[
                        html.H2("USER PROFILE", style={'textAlign': 'center',  'color': 'white'}),
                        dcc.Dropdown(
                            id='user',
                            className="user_dropdown",
                            options=get_plot_data()['user_name'],
                            placeholder="Select a user..."
                            ),
                        html.Img(
                            className="user_image",
                            src=user_profile_img,
                            ),
                        html.B("Name:"),
                        html.P(id="user_name"),
                        html.B("LastName:"),
                        html.P(id="user_lastname"),
                        html.B("Age:"),
                        html.P(id="user_age"),
                        html.B("Sport:"),
                        html.P(id="user_sport"),
                        ],
                    ),
                # RightColumn
                html.Div(
                    className="rightcolumn",
                    children=[
                        html.Div(
                            html.H2("USER STATISTICS"),
                            className="h2"
                            ),
                        html.Div(
                            className="matrix_graph",
                            children=[
                                html.Div(
                                    className="graph_box",
                                    children=dcc.Graph(
                                        className="dcc_graph",
                                        id="salt_losses",
                                        config={"displayModeBar": False},
                                        # figure=salt_loss_figure(0),
                                        ),
                                    ),
                                html.Div(
                                    className="graph_box",
                                    children=dcc.Graph(
                                        className="dcc_graph",
                                        id="sweat_id",
                                        config={"displayModeBar": False},
                                        # figure=sweat_id_figure(0),
                                        ),
                                    ),
                                html.Div(
                                    className="dcc_graph_two_columns",
                                    children=dcc.Graph(
                                        className="dcc_graph",
                                        id="weight_graph",
                                        config={"displayModeBar": False},
                                        # figure=weight_figure(None, 0, 0)
                                        )
                                    ),
                                html.Div(
                                    className="dcc_graph_three_columns",
                                    children=dcc.Graph(
                                        id="bar_graph",
                                        className="dcc_graph",
                                        config={"displayModeBar": False},
                                        # figure=salt_amount([0], [0])
                                        ),
                                    ),
                                ],
                            )
                        ],
                    ),
                ],
            ),
        # # FOOTER
        # html.Div(
        #     className="footer",
        #     children=[html.Footer("Footer section")],
        #     ),
        ]
    )


@app.callback([Output('bar_graph', 'figure'), Output('user', 'options')],
              Input('interval_data', 'n_intervals'))
def update_input_data(n):
    updated_data = get_plot_data()
    return salt_amount(updated_data['user_name'], updated_data['salt_amount']), updated_data['user_name']


@app.callback([
    Output('sweat_id', 'figure'),
    Output('salt_losses', 'figure'),
    Output('weight_graph', 'figure'),
    Output('user_name', 'children'),
    Output('user_lastname', 'children'),
    Output('user_age', 'children'),
    Output('user_sport', 'children')
    ],
    Input('user', 'value'))
def update_volunteer_data(user_name):
    if user_name is None:
        return sweat_id_figure(0), salt_loss_figure(0), weight_figure(None, 0, 0), None, None, None, None

    updated_data = get_plot_data()
    sweat_id = updated_data[updated_data['user_name'] == user_name]['sweat_id'].values[0]
    salt_amount = updated_data[updated_data['user_name'] == user_name]['salt_amount'].values[0]
    user_lastname = updated_data[updated_data['user_name'] == user_name]['user_lastname'].values[0]
    user_age = updated_data[updated_data['user_name'] == user_name]['user_age'].values[0]
    user_sport = updated_data[updated_data['user_name'] == user_name]['user_sport'].values[0]
    weight_init = updated_data[updated_data['user_name'] == user_name]['weight_initial'].values[0]
    weight_final = updated_data[updated_data['user_name'] == user_name]['weight_final'].values[0]

    return \
        sweat_id_figure(sweat_id), \
        salt_loss_figure(salt_amount), \
        weight_figure(user_name, weight_init, weight_final), \
        user_name, user_lastname, user_age, user_sport


if __name__ == "__main__":
    app.run_server(debug=True)
