from dash import Dash
from dash.dependencies import Input, Output
from source import plot_figure, data


def update_input_data(app: Dash) -> plot_figure:
    @app.callback([Output('bar_graph', 'figure'), Output('user', 'options')],
                  Input('interval_data', 'n_intervals'))
    def inner_update_input_data(n):
        updated_data = data.get_plot_data()
        return plot_figure.salt_amount(updated_data['user_name'], updated_data['salt_amount']), updated_data['user_name']


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
            return plot_figure.sweat_id_figure(0), plot_figure.salt_loss_figure(0), plot_figure.weight_figure(None, 0, 0), None, None, None, None

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
