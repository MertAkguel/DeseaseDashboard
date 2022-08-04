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
df = df_changed_columns.sort_values(by=["Entity", "Year"])
app = dash.Dash()
app.layout = html.Div([
    # dcc.Graph(id="figure_slider"),
    html.H2("Death rates over years after illness", style={'textAlign': 'center'}),
    html.P("Select an animation:"),
    dcc.RadioItems(
        sorted([{'label': 'Meningitis', 'value': 'Meningitis'},
         {'label': 'Neoplasms', 'value': 'Neoplasms'},
         {'label': 'Fire, heat, and hot substances', 'value': 'Fire,heat,andhotsubstances'},
         {'label': 'Malaria', 'value': 'Malaria'},
         {'label': 'Drowning', 'value': 'Drowning'},
         {'label': 'Interpersonal violence', 'value': 'Interpersonalviolence'},
         {'label': 'HIV/AIDS', 'value': 'HIV/AIDS'},
         {'label': 'Drug use disorders', 'value': 'Drugusedisorders'},
         {'label': 'Tuberculosis', 'value': 'Tuberculosis'},
         {'label': 'Roadinjuries', 'value': 'Roadinjuries'},
         {'label': 'Maternal disorders', 'value': 'Maternaldisorders'},
         {'label': 'Lower respiratory infections', 'value': 'Lowerrespiratoryinfections'},
         {'label': 'Neonatal disorders', 'value': 'Neonataldisorders'},
         {'label': 'Alcohol use disorders', 'value': 'Alcoholusedisorders'},
         {'label': 'Exposure to forces of nature', 'value': 'Exposuretoforcesofnature'},
         {'label': 'Diarrheal diseases', 'value': 'Diarrhealdiseases'},
         {'label': 'Environmental heat and cold exposure', 'value': 'Environmentalheatandcoldexposure'},
         {'label': 'Nutritional deficiencies', 'value': 'Nutritionaldeficiencies'},
         {'label': 'Self-harm', 'value': 'Self-harm'},
         {'label': 'Conflict and terrorism', 'value': 'Conflictandterrorism'},
         {'label': 'Diabetes mellitus', 'value': 'Diabetesmellitus'},
         {'label': 'Poisonings', 'value': 'Poisonings'},
         {'label': 'Protein-energy malnutrition', 'value': 'Protein-energy malnutrition'},
         {'label': 'Terrorism (deaths)', 'value': 'Terrorism (deaths)'},
         {'label': 'Cardiovascular diseases', 'value': 'Cardiovasculardiseases'},
         {'label': 'Chronickidney disease', 'value': 'Chronickidneydisease'},
         {'label': 'Chronic respiratory diseases', 'value': 'Chronicrespiratorydiseases'},
         {'label': 'Cirrhosis and other chronic liver diseases', 'value': 'Cirrhosisandotherchronicliverdiseases'},
         {'label': 'Digestive diseases', 'value': 'Digestivediseases'},
         {'label': 'Acute hepatitis', 'value': 'Acutehepatitis'},
         {'label': "Alzheimer's disease and other dementias", 'value': "Alzheimer'sdiseaseandotherdementias"},
         {'label': "Parkinson's disease", 'value': "Parkinson'sdisease"},
         ],key=lambda desease:desease['value']),
        id="selection",

        value="Diabetesmellitus",
        inline=True),
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
            range_color=(0, 100000),
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
        ),
        "HIV/AIDS": px.choropleth(
            df,
            locations="Code",
            color="HIV/AIDS",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Neoplasms": px.choropleth(
            df,
            locations="Code",
            color="Neoplasms",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Fire,heat,andhotsubstances": px.choropleth(
            df,
            locations="Code",
            color="Fire,heat,andhotsubstances",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Malaria": px.choropleth(
            df,
            locations="Code",
            color="Malaria",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Drowning": px.choropleth(
            df,
            locations="Code",
            color="Drowning",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Interpersonalviolence": px.choropleth(
            df,
            locations="Code",
            color="Interpersonalviolence",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Drugusedisorders": px.choropleth(
            df,
            locations="Code",
            color="Drugusedisorders",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Tuberculosis": px.choropleth(
            df,
            locations="Code",
            color="Tuberculosis",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Roadinjuries": px.choropleth(
            df,
            locations="Code",
            color="Roadinjuries",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Maternaldisorders": px.choropleth(
            df,
            locations="Code",
            color="Maternaldisorders",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Lowerrespiratoryinfections": px.choropleth(
            df,
            locations="Code",
            color="Lowerrespiratoryinfections",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Neonataldisorders": px.choropleth(
            df,
            locations="Code",
            color="Neonataldisorders",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Alcoholusedisorders": px.choropleth(
            df,
            locations="Code",
            color="Alcoholusedisorders",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Exposuretoforcesofnature": px.choropleth(
            df,
            locations="Code",
            color="Exposuretoforcesofnature",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Diarrhealdiseases": px.choropleth(
            df,
            locations="Code",
            color="Diarrhealdiseases",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Environmentalheatandcoldexposure": px.choropleth(
            df,
            locations="Code",
            color="Environmentalheatandcoldexposure",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Nutritionaldeficiencies": px.choropleth(
            df,
            locations="Code",
            color="Nutritionaldeficiencies",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Self-harm": px.choropleth(
            df,
            locations="Code",
            color="Self-harm",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Conflictandterrorism": px.choropleth(
            df,
            locations="Code",
            color="Conflictandterrorism",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Poisonings": px.choropleth(
            df,
            locations="Code",
            color="Poisonings",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Protein-energy malnutrition": px.choropleth(
            df,
            locations="Code",
            color="Protein-energy malnutrition",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Terrorism (deaths)": px.choropleth(
            df,
            locations="Code",
            color="Terrorism (deaths)",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Cardiovasculardiseases": px.choropleth(
            df,
            locations="Code",
            color="Cardiovasculardiseases",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Chronickidneydisease": px.choropleth(
            df,
            locations="Code",
            color="Chronickidneydisease",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Chronicrespiratorydiseases": px.choropleth(
            df,
            locations="Code",
            color="Chronicrespiratorydiseases",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Cirrhosisandotherchronicliverdiseases": px.choropleth(
            df,
            locations="Code",
            color="Cirrhosisandotherchronicliverdiseases",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Digestivediseases": px.choropleth(
            df,
            locations="Code",
            color="Digestivediseases",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Acutehepatitis": px.choropleth(
            df,
            locations="Code",
            color="Acutehepatitis",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Alzheimer'sdiseaseandotherdementias": px.choropleth(
            df,
            locations="Code",
            color="Alzheimer'sdiseaseandotherdementias",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        ),
        "Parkinson'sdisease": px.choropleth(
            df,
            locations="Code",
            color="Parkinson'sdisease",
            range_color=(0, 100000),
            hover_name="Entity",
            color_continuous_scale=px.colors.sequential.Turbo,
            animation_frame="Year"
        )

    }
    return animations[selection]


if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=True)  # Turn off reloader if inside Jupyter
