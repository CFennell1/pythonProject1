# source is https://www.kaggle.com/wyattowalsh/basketball

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


import matplotlib.pyplot as plt
plt.tight_layout()
df_Num1_Post_1970.plot(x="Team Name", y ="Count of Number 1 Picks",kind="bar", title="Number 1 picks by Team")
plt.show()


########################################
#merge this to the teams
rs=con.execute(("Select * from Team"))
df_team = pd.DataFrame(rs.fetchall())
df_team.columns=rs.keys()
# Close connection

print(df_team.head())
df_team_updated = df_team.merge(df2,left_on="full_name",right_on="nameTeam",how="left",)
print(df_team_updated.head())
print(df_team_updated.shape)


#update to fix up errors
df_team_updated=df_team_updated.fillna(0)
print(df_team_updated.head(31))
print(df_team_updated.shape)