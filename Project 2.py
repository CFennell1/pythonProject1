#https://www.kaggle.com/wyattowalsh/basketball
# Import necessary module
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

# Create engine: engine
engine = create_engine('sqlite:///basketball.sqlite')


# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)


# Open engine connection: con
con=engine.connect()

# Perform query: rs
rs = con.execute("SELECT * FROM Player_Attributes")

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())
df.columns=rs.keys()

print(df.shape)
print(df.index)
print(df.columns)
print(df.head())
print(df["WEIGHT"].head)
print(df.head())

df["HEIGHT_m"] = df["HEIGHT"]*0.0254
df["WEIGHT_kg"] = df["WEIGHT"]*0.454

print(df["HEIGHT_m"].mean())
print(df["HEIGHT_m"].median())
print(df["HEIGHT_m"].max())
print(df["HEIGHT_m"].min())
print(df["WEIGHT_kg"].mean())
print(df["WEIGHT_kg"].median())
print(df["WEIGHT_kg"].max())
print(df["WEIGHT_kg"].min())

df_Position_Data=df.groupby("POSITION")["HEIGHT_m"].agg([np.min, np.max, np.mean, np.median])
print(df_Position_Data.head(10))
print(df_Position_Data.shape)

def bmi(w,h):
    return w/h**2

df["BMI"]=bmi(df["WEIGHT_kg"],df["HEIGHT_m"])
# # Calculate the BMI: bmi
print(df.head())
# bmi=np_weight_kg/np_height_m**2