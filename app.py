import pandas as pd
import os
import dash
from dash import dcc
from dash import html, Input, Output, callback_context
import plotly.express as px
from prepare_data import change_column_names

DATA_DIR = r"C:\Users\Kleve\Downloads\meineIdee"
desease_dataset = "20220327 annual-number-of-deaths-by-cause.csv"

df_original = pd.read_csv(os.path.join(DATA_DIR, desease_dataset))
df_changed_columns = change_column_names(df_original)
df = df_changed_columns.sort_values(by=["Entity","Year"])

app = dash.Dash()
app.layout = html.Div([
    # dcc.Graph(id="figure_slider"),
    html.H4("Death rates over years after illness"),
    html.P("Select an animation:"),
    dcc.RadioItems(
        id="selection",
        options=[disease for disease in df.columns],
        value="Diabetesmellitus"),
    dcc.Loading(dcc.Graph(id="graph"), type="cube")
])


@app.callback(
    Output("graph", "figure"),
    Input("selection", "value"))
def update_output(selection):


    animations = {
        "Diabetesmellitus": px.choropleth(
            df,
            locations="Code",
            color="Diabetesmellitus",
            range_color=(0,100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Meningitis": px.choropleth(
            df,
            locations="Code",
            color="Meningitis",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        )





    }
    return animations[selection]


if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=True)  # Turn off reloader if inside Jupyter
