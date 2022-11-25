import plotly.graph_objects as go


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
            'x': 0.1,
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