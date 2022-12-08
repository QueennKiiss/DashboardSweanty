import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from source import layout_components, callbacks


def main() -> None:
    """ Main function """
    # dbc.themes.BOOTSTRAP is needed to use dbc components
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
    # Build App layout
    app.layout = html.Div(
        id='body',
        className="body",
        children=[
            dcc.Interval(
                id='interval_data',
                interval=1 * 1000,  # in milliseconds
                n_intervals=0
                ),
            # HEADER
            layout_components.header(app),
            # Main Content
            layout_components.main_content(app),
            # FOOTER
            # layout_components.footer(app),
            ]
        )

    # App Callbacks
    callbacks.update_volunteer_data(app)
    callbacks.update_input_data(app)
    callbacks.create_new_session(app)
    callbacks.create_new_user(app)

    # Run the app server
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
