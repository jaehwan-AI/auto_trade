import plotly.express as px
import plotly.graph_objects as go


def table_chart(head, values):
    fig = go.Figure(
        data=[
            go.Table(
                header=dict(values=head),
                cells=dict(values=values),
            )
        ]
    )
    return fig


def log_table_chart(head, values):
    fig = go.Figure(
        data=[
            go.Table(
                header=dict(values=head),
                cells=dict(values=values),
            )
        ]
    )
    return fig


def donut_chart(names, values):
    # data = px.data.tips()  # replace with your own data sources
    # fig = px.pie(data, values=values, names=names, hole=0.3)
    fig = go.Figure(data=[go.Pie(labels=names, values=values, hole=0.3)])
    return fig


def line_chart(date, data):
    fig = go.Figure(data=go.Scatter(x=date, y=data))
    return fig


def bar_chart(date, data):
    fig = go.Figure(
        data=[
            go.Bar(name="domestic earnings", x=date, y=data),
            go.Bar(name="foreign earnings", x=date, y=data),
        ]
    )
    fig.update_layout(barmode="stack")
    return fig
