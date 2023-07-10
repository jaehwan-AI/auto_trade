import dash_bootstrap_components as dbc
from dash import dcc, html

from .styles.main_styles import CONTENT_STYLE, SIDEBAR_STYLE


def layout_home(table, donut, bar, line, log_table):
    return html.Div(
        [
            html.Div(
                [
                    html.H4("Current Account"),
                    html.Div(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            dcc.Graph(id="table chart", figure=table),
                                        ],
                                        width=5,
                                    ),
                                    dbc.Col(
                                        [
                                            dcc.Graph(id="donut chart", figure=donut),
                                        ],
                                        width=5,
                                    ),
                                ]
                            )
                        ]
                    ),
                ],
                id="info_container",
                className="row_container_display",
            ),
            html.Div(
                [
                    html.H4("Rate of return"),
                    dcc.Graph(id="bar chart", figure=bar),
                ],
                id="rate_of_return",
                className="pretty_container",
            ),
            html.Div(
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
            html.Div(
                [
                    html.H4("Trading log"),
                    dbc.Row(dcc.Graph(id="trading log", figure=log_table)),
                ]
            ),
        ],
        id="main_container",
        style=CONTENT_STYLE,
    )


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
