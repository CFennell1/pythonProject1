# https://www.kaggle.com/wyattowalsh/basketball
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
con = engine.connect()

# Perform query: rs
rs = con.execute("SELECT * FROM Player_Attributes")

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())
df.columns = rs.keys()

print(df.shape)
print(df.index)
print(df.columns)
print(df.head())
print(df["WEIGHT"].head)
print(df.head())

df["HEIGHT_m"] = df["HEIGHT"] * 0.0254
df["WEIGHT_kg"] = df["WEIGHT"] * 0.454

print(df["HEIGHT_m"].mean())
print(df["HEIGHT_m"].median())
print(df["HEIGHT_m"].max())
print(df["HEIGHT_m"].min())
print(df["WEIGHT_kg"].mean())
print(df["WEIGHT_kg"].median())
print(df["WEIGHT_kg"].max())
print(df["WEIGHT_kg"].min())

df_Position_Data = df.groupby("POSITION")["HEIGHT_m"].agg([np.min, np.max, np.mean, np.median])
print(df_Position_Data.head(10))
print(df_Position_Data.shape)


def bmi(w, h):
    return w / h ** 2


df["BMI"] = bmi(df["WEIGHT_kg"], df["HEIGHT_m"])
# # Calculate the BMI: bmi
print(df.head())
# bmi=np_weight_kg/np_height_m**2

print(df["ROSTERSTATUS"].head())
df_Active_Players = df[df["ROSTERSTATUS"] == "Active"]
print(df_Active_Players.head())
print(df_Active_Players.shape)
print(df_Active_Players["SCHOOL"].head())

max_height = 0.00
min_height = 3.00
row_range = 0
min_height_row_range = 0
print(row_range)
print(max_height)
height_col = df_Active_Players.columns.get_loc("HEIGHT_m")
print(height_col)
print(df_Active_Players.iloc[0, height_col])
print(df_Active_Players.iloc[1, height_col])
# print(df_Active_Players["HEIGHT_m"].column)
# print(df_Active_Players.iloc[[0,df_Active_Players["HEIGHT_m"].column]])
# for i in range(409):
for i in range(0, df_Active_Players.shape[0]):
    # print(i)
    if df_Active_Players.iloc[i, height_col] > max_height:
        row_range = i
        max_height = df_Active_Players.iloc[i, height_col]
    if df_Active_Players.iloc[i, height_col] < min_height:
        min_height_row_range = i
        min_height = df_Active_Players.iloc[i, height_col]
print(row_range)
print(min_height_row_range)
max_height = max_height.round(2)
min_height = min_height.round(2)
print(max_height)
first_name = df_Active_Players.iloc[row_range, df_Active_Players.columns.get_loc("FIRST_NAME")]
last_name = df_Active_Players.iloc[row_range, df_Active_Players.columns.get_loc("LAST_NAME")]
team_city = df_Active_Players.iloc[row_range, df_Active_Players.columns.get_loc("TEAM_CITY")]
team_name = df_Active_Players.iloc[row_range, df_Active_Players.columns.get_loc("TEAM_NAME")]
print(df_Active_Players.iloc[row_range, 4])
print(first_name)
print(last_name)
print(team_city)
print(team_name)
print("The tallest player in the NBA is " + str(first_name) + " " + str(last_name) + " who plays for the " + str(
    team_city) + " " + str(team_name) + ". He is " + str(max_height) + " metres in height.")

first_name = df_Active_Players.iloc[min_height_row_range, df_Active_Players.columns.get_loc("FIRST_NAME")]
last_name = df_Active_Players.iloc[min_height_row_range, df_Active_Players.columns.get_loc("LAST_NAME")]
team_city = df_Active_Players.iloc[min_height_row_range, df_Active_Players.columns.get_loc("TEAM_CITY")]
team_name = df_Active_Players.iloc[min_height_row_range, df_Active_Players.columns.get_loc("TEAM_NAME")]
print("The shortest player in the NBA is " + str(first_name) + " " + str(last_name) + " who plays for the " + str(
    team_city) + " " + str(team_name) + ". He is " + str(min_height) + " metres in height.")

df_Active_Players.to_csv(r'C:\Users\colin.fennell\Documents\df_Active_Players.csv')
print(i)
# df_unique_school = df_Active_Players["SCHOOL"].unique()

# nique_schools = df_unique_school.shape
# df_school = df_Active_Players["SCHOOL"]
# print(df_school.head())
# print(df_school.shape)

# df_school["Num_Players"]=df_school.groupby["SCHOOL"].count()
# print(df_school.head(10))

# for i in range(0,df_unique_school.shape[0]):
#    df_unique_school["Player_Count"]=i
#    print(i)

# print(df_unique_school.head())
# print(df_unique_school.index)
# print(df_unique_school.iloc[[10]:])

max_height = 0.00
min_height = 3.0
max_weight = 0.00
min_weight = 1000
max_bmi = 0
min_bmi = 100
height_col = 0

player_stats = ["max height", max_height, "min height", min_height, "max weight", max_weight, "max bmi", max_bmi,
                "min bmi", min_bmi]
print(player_stats)
max_height_player_details = ["first name", "", "last name", "", "team", "", "city", ""]
min_height_player_details = ["first name", "", "last name", "", "team", "", "city", ""]
# max_weight_player_details = ["first name", "", "last name", "", "team", "", "city", ""]
# min_weight_player_details = ["first name", "", "last name", "", "team", "", "city", ""]
# max_bmi_player_details = ["first name", "", "last name", "", "team", "", "city", ""]
# min_bmi_player_details = ["first name", "", "last name", "", "team", "", "city", ""]
print(max_height_player_details)
print(player_stats[1])
for i in range(0, df_Active_Players.shape[0]):
    print(i)
    if df_Active_Players.iloc[i, height_col] > player_stats[[1]]:
        player_stats[1] = df_Active_Players.iloc[i, height_col]
        max_height_player_details[1] = df_Active_Players.iloc[
            player_stats[1], df_Active_Players.columns.get_loc("FIRST_NAME")]
        max_height_player_details[3] = df_Active_Players.iloc[
            player_stats[1], df_Active_Players.columns.get_loc("LAST_NAME")]
        max_height_player_details[5] = df_Active_Players.iloc[
            player_stats[1], df_Active_Players.columns.get_loc("TEAM_NAME")]
        max_height_player_details[7] = df_Active_Players.iloc[
            player_stats[1], df_Active_Players.columns.get_loc("TEAM_CITY")]
    if df_Active_Players.iloc[i, height_col] < min_height:
        min_height_row_range = i
        min_height = df_Active_Players.iloc[i, height_col]

print(player_stats[1])
print(max_height_player_details)


