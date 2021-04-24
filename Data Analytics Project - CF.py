# source is https://www.kaggle.com/wyattowalsh/basketball

from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create engine: engine
engine = create_engine('sqlite:///basketball.sqlite')


# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)

# Open engine connection: con
con=engine.connect()

# Take down data from Team file
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Team")
    df_Team = pd.DataFrame(rs.fetchall())
    df_Team.columns = rs.keys()

print(df_Team.head())
print(df_Team.columns)

# Take down data from Draft file
with engine.connect() as con:
    rs=con.execute(("Select * from Draft"))
    df_Draft = pd.DataFrame(rs.fetchall())
    df_Draft.columns = rs.keys()

print(df_Draft.head())
print(df_Draft.columns)

#Consider number 1 draft picks since 1970
df_Draft_Post_1970 = df_Draft[(df_Draft["numberPickOverall"]==1) & (df_Draft["yearDraft"]>=1970)]

#Count the number 1 picks per team
df_Num1_Post_1970 = df_Draft_Post_1970.groupby("nameTeam")["numberPickOverall"].sum()
df_Num1_Post_1970.columns=['Team_Name', 'Count_of_Number_1_Picks']
print(df_Num1_Post_1970)
print(df_Num1_Post_1970.columns)


#show a bar chart of the number 1 picks per team
df_Num1_Post_1970.plot(x="Team Name", y ="Count of Number 1 Picks",kind = "bar", title = "Number 1 picks by Team since 1970", xlabel = "Team Name")
plt.tight_layout()
plt.show()


#merge the team data with the number 1 picks data
df_Team_Updated = df_Team.merge(df_Num1_Post_1970, left_on = "full_name", right_on = "nameTeam", how = "left",)
print(df_Team_Updated.head())
print(df_Team_Updated.shape)


#Fix up errors for teams that have never had the number 1 pick
df_Team_Updated=df_Team_Updated.fillna(0)
print(df_Team_Updated.head())
print(df_Team_Updated.shape)

print ("The teams that never had the number 1 pick are as follows:")
for i, row in df_Team_Updated.iterrows():
    if row["numberPickOverall"]==0:
        print(row["full_name"])