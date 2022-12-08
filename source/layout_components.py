""" Module containing html components"""

from datetime import datetime
from dash import Dash, dcc, html
from source import data
from resources import images
import dash_bootstrap_components as dbc


def create_new_session(app: Dash) -> html.Div:
    return html.Div(
        className='create_new_session',
        children=[
            html.Div(
                className='form_fields_container',
                children=[
                    html.P(className='form_title', children=["Session name:"]),
                    dcc.Input(
                        className='form_field',
                        id="session_name_input",
                        children=["Session name"],
                        placeholder="Enter the session name"),
                    ],
                ),
            html.Button(
                children='Create New Session',
                className='register_user_button',
                id='new_session_button',
                n_clicks=0,),
            ])


def register_new_user(app: Dash) -> html.Div:
    return html.Div(
        className='register_new_user',
        children=[
            html.Div(
                className='form_fields_container',
                children=[
                    html.P(className='form_title', children=["User name:"]),
                    dcc.Input(
                        className='form_field',
                        id='user_name_field',
                        placeholder="Enter the name",
                        type="text"
                        ),
                    ],
                ),
            html.Div(
                className='form_fields_container',
                children=[
                    html.P(className='form_title', children=["User surnames:"]),
                    dcc.Input(
                        className='form_field',
                        id='user_surname_field',
                        placeholder="Enter the surnames",
                         type="text"),
                        ],
                ),
            html.Div(
                className='form_fields_container',
                children=[
                    html.P(className='form_title', children=["User age:"]),
                    dcc.Input(
                        className='form_field',
                        id='user_age_field',
                        placeholder="Enter the age",
                        type="number"),
                    ]
                ),
            html.Div(
                className='form_fields_container',
                children=[
                    html.P(className='form_title', children=["User sport:"]),
                    dcc.Input(
                        className='form_field',
                        id='user_sport_field',
                        placeholder="Enter the sport",
                        type="text"),
                    ],
                ),
            html.Button(
                children='Register New User',
                id='register_user_button',
                className='register_user_button',
                n_clicks=0),
            ])


def select_user_info(app: Dash) -> html.Div:
    user_profile_img = app.get_asset_url(images.USER_PROFILE_IMG)
    return html.Div(
        className='select_user_info',
        children=[
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
            ]
        )


def header(app: Dash) -> html.Div:
    """HEADER"""
    sweanty_icon = app.get_asset_url(images.SWEANTY_LOGO)

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
                                children=f"{datetime.now().hour:02d}:{datetime.now().minute:02d}:{datetime.now().second:02d}"
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
    return html.Div(
        className='leftcolumn',
        children=[
            dbc.Tabs(
                id='custom-tabs-container-id',
                className='custom-tabs-container',
                active_tab='new_session_tab_id',
                children=[
                    dbc.Tab(
                        id='new_session_tab',
                        tab_id='new_session_tab_id',
                        tab_class_name='custom-tab',
                        label_class_name='custom-title-tab',
                        active_tab_class_name='custom-tab--selected',
                        active_label_class_name='custom-title-tab--selected',
                        children=[create_new_session(app)],
                        label='Create session',
                        disabled=False,
                        ),
                    dbc.Tab(
                        id='new_user_tab',
                        tab_id='new_user_tab_id',
                        tab_class_name='custom-tab',
                        label_class_name='custom-title-tab',
                        active_tab_class_name='custom-tab--selected',
                        active_label_class_name='custom-title-tab--selected',
                        children=[register_new_user(app)],
                        label='New User',
                        disabled=False,
                        ),
                    dbc.Tab(
                        id='user_profile_tab',
                        tab_id='user_profile_tab_id',
                        tab_class_name='custom-tab',
                        label_class_name='custom-title-tab',
                        active_tab_class_name='custom-tab--selected',
                        active_label_class_name='custom-title-tab--selected',
                        children=[select_user_info(app)],
                        label='User Profile',
                        disabled=False,
                        ),
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
