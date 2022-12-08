import logging
import requests
from datetime import datetime
from dash import Dash
from dash.dependencies import Input, Output, State
from source import plot_figure, data
from database import connection


def create_new_session(app: Dash):
    @app.callback(
        Output('custom-tabs-container-id', 'active_tab'),
        Output('session_name_input', 'value'),
        Input('new_session_button', 'n_clicks'),
        State('session_name_input', 'value'),
        State('custom-tabs-container-id', 'active_tab')
        )
    def inner_create_new_session(n_clicks: int, session_name: str, prev_active_tab: str):
        if n_clicks > 0:
            db_connector = connection.DBConnector()
            engine = db_connector.engine_connection()
            session = db_connector.create_db_session(engine)
            db_connector.insert_to_table(
                'DashboardSession', session, session_name=session_name
                )
            # TODO: Insert query to know the id of the session
            return 'new_user_tab_id', ''
        # Return the previous active tab to avoid empty content
        return prev_active_tab, ''


def create_new_user(app: Dash):
    @app.callback([
        Output('user_name_field', 'value'),
        Output('user_surname_field', 'value'),
        Output('user_age_field', 'value'),
        Output('user_sport_field', 'value'),
        ],
        [Input('register_user_button', 'n_clicks'),
        State('user_name_field', 'value'),
        State('user_surname_field', 'value'),
        State('user_age_field', 'value'),
        State('user_sport_field', 'value'),
        ])
    def inner_create_new_user(
            n_clicks: int,
            user_name: str,
            user_surname: str,
            user_age: int,
            user_sport: str,
            # session_id: int,
            ):
        if n_clicks > 0:
            db_connector = connection.DBConnector()
            engine = db_connector.engine_connection()
            session = db_connector.create_db_session(engine)
            db_connector.insert_to_table(
                'Athletes', session,
                name=user_name, surname=user_surname,
                age=user_age, sport=user_sport, session_id=2
                )
        return '', '', '', ''


def update_input_data(app: Dash) -> plot_figure:
    @app.callback([
        Output('bar_graph', 'figure'),
        Output('bar_graph_2', 'figure'),
        Output('user', 'options'),
        Output('current_datetime', 'children')
        ],
        Input('interval_data', 'n_intervals'))
    def inner_update_input_data(_):
        updated_data = data.get_plot_data()
        current_datetime = datetime.now()
        current_time = f"{current_datetime.hour:02d}:{current_datetime.minute:02d}:{current_datetime.second:02d}"
        return \
            plot_figure.salt_amount(
                updated_data['user_name'], updated_data['salt_amount']), \
            plot_figure.accumulative_plot(
                updated_data['user_name'], updated_data['voltage'], updated_data['user_age']),\
            updated_data['user_name'], current_time


def update_volunteer_data(app: Dash) -> plot_figure:
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
    def inner_update_volunteer_data(user_name):
        if user_name is None:
            return \
                plot_figure.sweat_id_figure(0), \
                plot_figure.salt_loss_figure(0), \
                plot_figure.weight_figure(None, 0, 0), \
                "Not selected", "Not selected", "Not selected", "Not selected"

        updated_data = data.get_plot_data()
        sweat_id = updated_data[updated_data['user_name'] == user_name]['sweat_id'].values[0]
        salt_amount = updated_data[updated_data['user_name'] == user_name]['salt_amount'].values[0]
        user_lastname = updated_data[updated_data['user_name'] == user_name]['user_lastname'].values[0]
        user_age = updated_data[updated_data['user_name'] == user_name]['user_age'].values[0]
        user_sport = updated_data[updated_data['user_name'] == user_name]['user_sport'].values[0]
        weight_init = updated_data[updated_data['user_name'] == user_name]['weight_initial'].values[0]
        weight_final = updated_data[updated_data['user_name'] == user_name]['weight_final'].values[0]

        return \
            plot_figure.sweat_id_figure(sweat_id), \
            plot_figure.salt_loss_figure(salt_amount), \
            plot_figure.weight_figure(user_name, weight_init, weight_final), \
            user_name, user_lastname, user_age, user_sport
