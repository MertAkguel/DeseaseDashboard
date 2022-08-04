import pandas as pd
import numpy as np





def change_column_names(df):
    for column in list(df.columns):
        try:
            if column == 'Deaths - Self-harm - Sex: Both - Age: All Ages (Number)':
                df.rename(columns={column: "Self-harm"}, inplace=True)
            if column == 'Deaths - Protein-energy malnutrition - Sex: Both - Age: All Ages (Number)':
                df.rename(columns={column: "Protein-energy malnutrition"}, inplace=True)

            df.rename(columns={column: column.split("-")[1].replace(" ","")}, inplace=True)

        except:
            pass
    return df


