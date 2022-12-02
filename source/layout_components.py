""" Module containing html components"""

from datetime import datetime
from dash import Dash, dcc, html
from source import data
import dash_bootstrap_components as dbc


def header(app: Dash) -> html.Div:
    """HEADER"""
    sweanty_icon = app.get_asset_url("img/logo_sweanty_1-184x81.png")

    return html.Div(
        className="header_container",
        children=[
            html.Div(
                className="cell_image",
                children=[
                    html.Img(className="icon_left", src=sweanty_icon)]
                ),
            html.Div(
                className="Dashboard_title",
                children=[html.H1("Swenty results dashboard")],
                ),
            html.Div(
                className="weather_info",
                children=[
                    html.Div(
                        className="hour_container",
                        children=[
                            html.P(className="weather_title", children="Hour"),
                            html.P(
                                className='weather_value',
                                id='current_datetime',
                                children=f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
                                ),
                            ],
                        ),
                    html.Div(
                        className="temperature_container",
                        children=[
                            html.P(className="weather_title", children="Temperature"),
                            html.P(className='weather_value', children="23.5 C"),
                            html.Meter(
                                className="meter_indicator",
                                value="23.5",
                                min='0', max='40', low='15', high='35'
                                )
                            ]
                        ),
                    html.Div(
                        className="humidity_container",
                        children=[
                            html.P(className="weather_title", children="Humidity"),
                            html.P(className='weather_value', children="60%"),
                            html.Meter(
                                className="meter_indicator",
                                value="60",
                                min='0', max='100', low='40', high='75', optimum='60'
                                )
                            ]
                        ),
                    ],
                ),
            ]
        )


def main_content(app: Dash) -> html.Div:
    """# Main Content"""
    return html.Div(
        className="main_content_container",
        children=[
            left_column(app),
            right_column(app),
            ]
        )


def right_column(app: Dash) -> html.Div:
    """# RightColumn"""
    return html.Div(
        className="rightcolumn",
        children=[
            html.Div(
                className="sub_header",
                children=html.H3("USER STATISTICS"),
                ),
            html.Div(
                className="graphs_container",
                children=[
                    html.Div(
                        className="first_col",
                        children=[
                            html.Div(
                                className="graph_box",
                                children=[
                                    html.H4("Sweat ID"),
                                    dcc.Graph(
                                        className="dcc_graph_info",
                                        id="sweat_id",
                                        config={"displayModeBar": False},
                                        ),
                                    ],
                                ),
                            html.Div(
                                className="graph_box",
                                children=[
                                    html.H4("Tendency to lose salt"),
                                    dcc.Graph(
                                        className="dcc_graph_info",
                                        id="salt_losses",
                                        config={"displayModeBar": False},
                                        ),
                                    ],
                                ),
                            html.Div(
                                className="graph_box",
                                children=[
                                    html.H4("Weight comparison"),
                                    dcc.Graph(
                                        className="dcc_graph",
                                        id="weight_graph",
                                        config={"displayModeBar": False},
                                        ),
                                    ]
                                ),
                            ],
                        ),
                    html.Div(
                        className="second_col",
                        children=[
                            html.Div(
                                className="dcc_graph_three_columns",
                                children=[
                                    html.H4("Salt amount"),
                                    dcc.Graph(
                                        id="bar_graph",
                                        className="dcc_graph",
                                        config={"displayModeBar": False},
                                        ),
                                    ],
                                ),
                            html.Div(
                                className="dcc_graph_three_columns",
                                children=[
                                    html.H4("Measured voltage & User age"),
                                    dcc.Graph(
                                        id="bar_graph_2",
                                        className="dcc_graph",
                                        config={"displayModeBar": False},
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )


def left_column(app: Dash) -> html.Div:
    """# LeftColumn"""
    user_profile_img = app.get_asset_url("img/user_profile.png")
    return html.Div(
        className='leftcolumn',
        children=[
            html.H3("USER PROFILE"),
            html.Img(
                className="user_image",
                src=user_profile_img,
                ),
            dcc.Dropdown(
                id='user',
                className="user_dropdown",
                options=data.get_plot_data()['user_name'],
                placeholder="Select a user..."
                ),
            dbc.Row(
                children=[
                    dbc.Col(html.Div(html.B("Name:"))),
                    dbc.Col(html.Div(html.P(id="user_name", children="Not selected"))),
                    ],
                ),
            dbc.Row(
                children=[
                    dbc.Col(html.Div(html.B("Lastname:"))),
                    dbc.Col(html.Div(html.P(id="user_lastname", children="Not selected"))),
                    ],
                ),
            dbc.Row(
                children=[
                    dbc.Col(html.Div(html.B("Age:"))),
                    dbc.Col(html.Div(html.P(id="user_age", children="Not selected"))),
                    ],
                ),
            dbc.Row(
                children=[
                    dbc.Col(html.Div(html.B("Sport:"))),
                    dbc.Col(html.Div(html.P(id="user_sport", children="Not selected"))),
                    ],
                ),
            ],
        )


def footer(app: Dash) -> html.Div:
    """# FOOTER"""
    return html.Div(
        className="footer_container",
        children=[
            html.H4("Footer section"),
            html.P(
                "This is the final part of the Dashboard, "
                "like a footer but using a paragraph html element"
                ),
            ]
        )
