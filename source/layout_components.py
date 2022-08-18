from dash import Dash, dcc, html
from source import data


def header(app: Dash) -> html.Div:
    # HEADER
    sweanty_icon = app.get_asset_url("img/logo_sweanty_1-184x81.png")
    bewolfish_icon = app.get_asset_url("img/bewolfish_logo_color.png")

    return html.Div(
        className="header_container",
        children=[
            html.Div(
                className="cell",
                children=[html.Img(className="icon_left", src=sweanty_icon)]
                ),
            html.Div(
                className="cell",
                children=[html.H1(className="header_title", children="SWEANTY-BEWOLFISH STUDY")],
                ),
            html.Div(
                className="cell",
                children=[html.Img(className="icon_right", src=bewolfish_icon)]
                ),
            ]
        )


def main_content(app: Dash) -> html.Div:
    # Main Content
    return html.Div(
        className="main_content_container",
        children=[
            html.Div(
                children=[left_column(app)]
                ),
            html.Div(
                children=[right_column(app)]
                )
            ]
        )


def right_column(app: Dash) -> html.Div:
    # RightColumn
    return html.Div(
        className="rightcolumn",
        children=[
            html.Div(
                className="sub_header",
                children=html.Div(
                    html.H2("USER STATISTICS"),
                    )
                ),
            html.Div(
                className="matrix_graph",
                children=[
                    html.Div(
                        className="graph_box",
                        children=dcc.Graph(
                            className="dcc_graph", id="salt_losses", config={"displayModeBar": False},
                            # figure=salt_loss_figure(0),
                            ),
                        ),
                    html.Div(
                        className="graph_box",
                        children=dcc.Graph(
                            className="dcc_graph", id="sweat_id", config={"displayModeBar": False},
                            # figure=sweat_id_figure(0),
                            ),
                        ),
                    html.Div(
                        className="dcc_graph_two_columns",
                        children=dcc.Graph(
                            className="dcc_graph", id="weight_graph", config={"displayModeBar": False},
                            # figure=weight_figure(None, 0, 0)
                            )
                        ),
                    html.Div(
                        className="dcc_graph_three_columns",
                        children=dcc.Graph(
                            id="bar_graph", className="dcc_graph", config={"displayModeBar": False},
                            # figure=salt_amount([0], [0])
                            ),
                        ),
                    ],
                )
            ],
        )


def left_column(app: Dash) -> html.Div:
    user_profile_img = app.get_asset_url("img/user_profile.png")
    # LeftColumn
    return html.Div(
        className='leftcolumn',
        children=[
            html.H2("USER PROFILE", style={'textAlign': 'center', 'color': 'white'}),
            dcc.Dropdown(
                id='user', className="user_dropdown", options=data.get_plot_data()['user_name'],
                placeholder="Select a user..."
                ),
            html.Img(className="user_image", src=user_profile_img, ),
            html.B("Name:"),
            html.P(id="user_name"),
            html.B("LastName:"),
            html.P(id="user_lastname"),
            html.B("Age:"),
            html.P(id="user_age"),
            html.B("Sport:"),
            html.P(id="user_sport"),
            ],
        )


def footer(app: Dash) -> html.Div:
    # FOOTER
    return html.Div(
        className="footer_container",
        children=[
            html.Div(
                children=[
                    html.H4("Footer section"),
                    html.P("This is the final part of the Dashboard, like a footer but using a paragraph html element"),
                    ]
                )
            ],
        )
