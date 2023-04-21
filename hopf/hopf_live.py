import numpy as np
import plotly.graph_objs as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from hopf import hopf_fibration_circle, cross_product_matrix, num_points, num_circles, R, r, theta

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.Graph(id="graph", style={"height": "85vh"})
    ]),
    html.Div([
        html.Div([
            html.Label("Number of Circles"),
            dcc.Slider(id="num_circles", min=1, max=100, value=50, step=1),
        ], style={"width": "30%", "padding": "0 10px"}),
        html.Div([
            html.Label("r"),
            dcc.Slider(id="r", min=0.1, max=2.0, value=1.5, step=0.1),
        ], style={"width": "30%", "padding": "0 10px"}),
        html.Div([
            html.Label("theta"),
            dcc.Slider(id="theta", min=0, max=2 * np.pi, value=np.pi / 6, step=0.01),
        ], style={"width": "30%", "padding": "0 10px"}),
    ], style={"display": "flex", "justify-content": "space-around", "padding": "0 10px"})
])

@app.callback(
    Output("graph", "figure"),
    [
        Input("num_circles", "value"),
        Input("r", "value"),
        Input("theta", "value"),
    ],
)
def update_figure(num_circles, r, theta):
    data = []
    R = 1.0
    axis_range = R + r + 0.2

    for i in range(num_circles):
        phi = 2 * np.pi * i / num_circles
        x, y, z = hopf_fibration_circle(phi, theta, num_points, R=R, r=r)
        trace = go.Scatter3d(x=x, y=y, z=z, mode="lines")
        data.append(trace)

    layout = go.Layout(
        scene=dict(
            xaxis_title="X",
            yaxis_title="Y",
            zaxis_title="Z",
            xaxis=dict(range=[-axis_range, axis_range]),
            yaxis=dict(range=[-axis_range, axis_range]),
            zaxis=dict(range=[-r, r]),
        )
    )

    fig = go.Figure(data=data, layout=layout)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
