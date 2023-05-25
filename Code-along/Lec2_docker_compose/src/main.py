#%%
import plotly_express as px
import numpy as np
import pandas as pd 
from dash import Dash, dcc, Output, Input, State
from dash.html import H1, Div, P, H2, Button
from pathlib import Path

simulation_path = Path(__file__).parent / "simulations"
simulation_path.mkdir(exist_ok=True)
print(simulation_path)


dropdown_options = [{"label": f"{rolls} rolls", "value": rolls} for rolls in [10,100,1000,10000]]

#%%

app = Dash(__name__)

app.layout = Div([
    H1("Dice simulator"),
    P("Choose number of dices and number of rolls and enjoy the results"),
    dcc.Graph(id = "dice-graph"),
    Button("Save dice rolls", id = "save-button"),
    H2("Number of rolls"),
    dcc.Dropdown(id = "number-rolls", options = dropdown_options, value=100),
    H2("Number of dices"),
    dcc.Slider(id ="number-dices", min=1, max=6, step=1, value=2, ),
    dcc.Store(id = "simulation-data"),
    dcc.Download(id = "download-csv")
])

@app.callback(Output("download-csv", "data"), Input("save-button", "n_clicks"), State("simulation-data", "data"))
def download_csv(n_clicks, data):

    saved_filepath = (simulation_path/f"simulation{n_clicks}.csv").as_posix()

    if n_clicks:
        csv_string = pd.DataFrame(data).to_csv(index = False)

        with open(saved_filepath, "w") as file:
            file.write(csv_string)

        return dcc.send_file(saved_filepath)

@app.callback(Output("simulation-data", "data"), Input("number-dices", "value"), Input("number-rolls", "value"))
def _dice_simulation(number_dices, rolls):
    dices = np.random.randint(1,7, size=(rolls, number_dices))
    return dices

@app.callback(Output("dice-graph", "figure"), Input("simulation-data", "data"))
def _dice_simulator_histogram(dices):
    return px.histogram(np.array(dices).sum(axis = 1))





if __name__ == "__main__":
    print('Hello from the docker side')

    app.run_server(host = "0.0.0.0", debug = True, port = 8050)
