from dash import dcc, html
import dash_bootstrap_components as dbc

from .styles.main_styles import SIDEBAR_STYLE


def build_side():
    side = html.Div(
        # id="side-panel",
        children=[
            html.H2("Stock Dashboard"),
            html.Hr(),
            html.P("Auto-trading log"),
            dbc.Nav(
                children=[
                    dbc.NavLink(
                        "Home",
                        href="/",
                        active="exact",
                        external_link=True,
                    ),
                    dbc.NavLink(
                        "List of stocks",
                        href="/stock-list",
                        active="exact",
                        external_link=True,
                    ),
                    dbc.NavLink(
                        "Trading log",
                        href="/auto-trading-log",
                        active="exact",
                        external_link=True,
                    ),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style=SIDEBAR_STYLE,
    )
    return side


def layout_home(table, donut, bar):
    return html.Div(
        [
            dbc.Container(
                [
                    dbc.Row(
                        [
                            html.H4("Rate of return"),
                            dbc.Row(
                                dcc.Graph(id="bar chart", figure=bar), align="center"
                            ),
                        ],
                    ),
                    dbc.Row(
                        [
                            html.H4("Current Account"),
                            dbc.Col(
                                dcc.Graph(id="table chart", figure=table),
                                align="center",
                            ),
                            dbc.Col(
                                dcc.Graph(id="donut chart", figure=donut),
                                align="center",
                            ),
                        ],
                        # style={"marginBottom": "-5%"},
                    ),
                ]
            ),
        ]
    )


def layout_list(line):
    return html.Div(
        [
            dbc.Container(
                [
                    dbc.Row(
                        [
                            html.H4("Stock forecast"),
                            dcc.Dropdown(
                                id="ticker",
                                options=[
                                    {"label": "{}".format(i), "value": i}
                                    for i in ["Samsung", "SK", "LG"]
                                ],
                                value=[10, 15, 10, 15, 10],
                                clearable=False,
                            ),
                            dcc.Graph(id="line chart", figure=line),
                        ],
                    ),
                ]
            ),
        ]
    )


def layout_log(log_table):
    return html.Div(
        [
            dbc.Container(
                [
                    dbc.Row(
                        [
                            html.H4("Trading log"),
                            dbc.Row(dcc.Graph(id="trading log", figure=log_table)),
                        ]
                    )
                ]
            )
        ]
    )
