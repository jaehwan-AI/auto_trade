import flask
import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, dash_table, Input, Output

import pandas as pd

from templates.layouts import build_side, layout_home, layout_list, layout_log
from templates.graphs import (
    table_chart,
    donut_chart,
    line_chart,
    bar_chart,
    log_table_chart,
)
from templates.styles.main_styles import CONTENT_STYLE

# define app
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

# data
head, account = ["국내", "해외"], [[100], [100]]

labels = ["one", "two", "three", "four"]
values = [10, 20, 30, 40]

date_list, stock_data = ["01/01", "02/01", "03/01", "04/01", "05/01"], [
    10,
    20,
    10,
    20,
    10,
]
ratio = [10, 15, 20, 25, 30]

table = table_chart(head=head, values=account)
donut = donut_chart(names=labels, values=values)
line = line_chart(date=date_list, data=stock_data)
bar = bar_chart(date=date_list, data=ratio)
log_table = log_table_chart(head=head, values=account)

side = build_side()
main = html.Div(id="page-content", style=CONTENT_STYLE)

# layout
app.layout = html.Div([dcc.Location(id="url"), side, main])


@app.callback(
    Output(component_id="page-content", component_property="children"),
    # Output(component_id="table chart", component_property="figure"),
    # Output(component_id="donut chart", component_property="figure"),
    # Output(component_id="line chart", component_property="figure"),
    # Output(component_id="bar chart", component_property="figure"),
    # Output(component_id="trading log", component_property="figure"),
    [
        Input("url", "pathname"),
        # Input("ticker", "value"),
    ],
)
# def render_page_content(pathname, ticker):
def render_page_content(pathname):
    if pathname == "/":
        return layout_home(table, donut, bar)
    if pathname == "/stock-list":
        # line = line_chart(date=date_list, data=stock_data)
        return layout_list(line)
    elif pathname == "/auto-trading-log":
        return layout_log(log_table)

    # If the user tries to reach a different page, return a 404 message!
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
    )


if __name__ == "__main__":
    app.run_server(debug=True)
