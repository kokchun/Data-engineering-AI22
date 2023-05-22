import plotly_express as px
import numpy as np
from dash import Dash, dcc, html
from dash.dependencies import Output, Input, State
from pathlib import Path
import pandas as pd

simulation_path = Path(__file__).parent / "simulations"
simulation_path.mkdir(exist_ok=True)


app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1("Dice simulator"),
        html.P("Choose number of dices and number of rolls and enjoy the histogram"),
        dcc.Graph(id="dice-graph"),
        html.Button("Save simulation", id="save-button"),
        html.H2("Number of rolls", id="header"),
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
        dcc.Store(id="simulation-data"),
        dcc.Download(id="download-csv"),
    ]
)


@app.callback(
    Output("download-csv", "data"),
    Input("save-button", "n_clicks"),
    State("simulation-data", "data"),
    prevent_initial_call=True,
)
def download_csv(n_clicks, data):
    saved_filepath = (simulation_path / f"simulation{n_clicks}.csv").as_posix()

    if n_clicks:
        csv_string = pd.DataFrame(data).to_csv(index=False)

        with open(saved_filepath, "w") as file:
            file.write(csv_string)
        return dcc.send_file(saved_filepath)


@app.callback(Output("dice-graph", "figure"), Input("simulation-data", "data"))
def _dice_histogram(dices):
    return px.histogram(np.array(dices).sum(axis=0))


@app.callback(
    Output("simulation-data", "data"),
    Input("num_dices_slider", "value"),
    Input("number_rolls", "value"),
)
def _dice_simulation(number_dices=2, number_rolls=100):
    dices = np.random.randint(1, 7, size=(number_dices, number_rolls))
    return dices


if __name__ == "__main__":
    print("Hello from Docker container")
    app.run_server(host="0.0.0.0", debug=True, port=8050)
