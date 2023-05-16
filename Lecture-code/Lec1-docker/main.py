import plotly_express as px
import numpy as np
from dash import Dash, dcc, html
from dash.dependencies import Output, Input

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1("Dice simulator"),
        html.P("Choose number of dices and number of rolls and enjoy the histogram"),
        dcc.Graph(id="dice-graph"),
        html.H2("Number of rolls"),
        dcc.Dropdown(
            id="number_rolls",
            options=[
                {"label": f"{rolls} rolls", "value": rolls}
                for rolls in [10, 100, 1000, 10000]
            ],
            value=100,
        ),
        html.H2("Number of dices"),
        dcc.Slider(
            id="num_dices_slider",
            min=1,
            max=6,
            step=1,
            value=2,
            marks={i: f"{i}" for i in range(1, 7)},
        ),
    ]
)

@app.callback(
    Output("dice-graph", "figure"),
    Input("num_dices_slider", "value"),
    Input("number_rolls", "value"),
)
def _dice_simulator_histogram(number_dices=2, number_rolls=100):
    dices = np.random.randint(1, 7, size=(number_dices, number_rolls))

    return px.histogram(dices.sum(axis=0))



if __name__ == "__main__":
    print("Hello from Docker container")
    app.run_server(host = "0.0.0.0", debug=True, port=8081)
