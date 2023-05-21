# %%
import plotly.express as px
import pandas as pd
from setup import paths_directory
from dash import dcc, Dash, Output, Input
from dash.html import H1, H2, H3, P
from dash_bootstrap_components import Row, Col, Card, CardImg, Container, themes
import base64

image_paths = [path.as_posix() for path in paths_directory["avatars"].iterdir()]


df = pd.read_csv(paths_directory["data_warehouse"] / "users.csv", index_col=1).drop(
    columns="Unnamed: 0"
)

df.insert(len(df.columns), "image", image_paths)

# %%


# unfortunately the longitdude and latitude data was made up randomly, and
# didn't correspond to real cities

def user_map():
    fig = px.scatter_mapbox(
        data_frame=df,
        lat="latitude",
        lon="longitude",
        hover_name="name",
        zoom=2,
    )

    fig.update_layout(
        mapbox_style="open-street-map",
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        mapbox=dict(center=dict(lat=40.7749, lon=-96.4194)),
    )
    return fig


# HACKS - workaround to load local images to dash
def image_to_base64(image_path):
    with open(image_path, "rb") as file:
        encoded_image = base64.b64encode(file.read()).decode("utf-8")
    return encoded_image


name_list = df["name"].to_list()
id_list = df.index.to_list()

user_options = [
    {
        "label": name,
        "value": id_,
    }
    for name, id_ in zip(name_list, id_list)
]

app = Dash(__name__, external_stylesheets=[themes.FLATLY])

app.layout = Container(
    [
        Row(H1("Tracking users", className="text-primary text-center p-3")),
        Row(
            [
                Col(
                    [
                        H2("Map"),
                        dcc.Graph(id="user-map", figure=user_map()),
                    ],
                    width=8,
                ),
                Col(
                    [
                        H2(
                            "User data",
                            id="card-header",
                        ),
                        Card(id="user-card"),
                        dcc.Dropdown(
                            id="users-dropdown",
                            options=user_options,
                            value=id_list[0],
                            className="mt-4",
                            placeholder=name_list[0],
                        ),
                    ],
                    className="mx-5",
                ),
            ]
        ),
    ],
    fluid=False,
)


@app.callback(Output("user-card", "children"), Input("users-dropdown", "value"))
def user_card(user_id):
    image_path = (paths_directory["avatars"] / f"{user_id}.png").as_posix()
    encoded_image = image_to_base64(image_path)

    user = df.loc[user_id]
    card = Row(
        [
            Col(
                CardImg(src=f"data:image/png;base64,{encoded_image}"),
                className="col-md-4",
            ),
            Col(
                [
                    H3(
                        f"{user['name']}",
                        className="mt-2",
                    ),
                    P(f"{user['date_of_birth']}", className="card-info"),
                    P(f"{user['city']}", className="card-info"),
                ],
            ),
        ]
    )
    return card


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)

# %%
