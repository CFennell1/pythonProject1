#https://www.kaggle.com/wyattowalsh/basketball
# Import necessary module
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///basketball.sqlite')


# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)


# Open engine connection: con
con=engine.connect()

# Perform query: rs
rs = con.execute("SELECT * FROM Team")

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())
df.columns=rs.keys()
# Close connection
#con.close()

# Print head of DataFrame df
print(df.head())

rs=con.execute(("Select * from Player_Salary"))
df = pd.DataFrame(rs.fetchall())
df.columns=rs.keys()
# Close connection
#con.close()

# Print head of DataFrame df
print(df.head())
print(df.shape)
print(df.columns)

rs=con.execute(("Select * from Draft"))
df = pd.DataFrame(rs.fetchall())
df.columns=rs.keys()
# Close connection
#con.close()
print(df.head())
print(df.shape)
print(df.columns)



df1 = df[df["numberPickOverall"]==1]
df1=df1[df1["yearDraft"]>1970]
#df1 = df[df["yearDraft">=1970] and df["numberPickOverall"==1]]

#df1=df(numerPickOverall ==1)
print(df1.head())
print(df1.shape)
print(df1["namePlayer"])
print(df1['nameTeam'])

#df2= df1.groupby("nameTeam")["numberPickOverall"].sum()
df2= df1.groupby("nameTeam")["numberPickOverall"].sum()
df2.columns=['Team_Name', 'Count_of_Number_1_Picks']

#num1_by_team = num1_by_team.sort_values("numberPickOverall",ascending = False)
print(df2)
print(df2.columns)


import matplotlib.pyplot as plt

df2.plot(x="Team Name", y ="Count of Number 1 Picks",kind="bar", title="Number 1 picks by Team")
plt.show()


#merge this to the teams
rs=con.execute(("Select * from Team"))
df_team = pd.DataFrame(rs.fetchall())
df_team.columns=rs.keys()
# Close connection

print(df_team.head())
df_team_updated = df_team.merge(df2,left_on="full_name",right_on="nameTeam",)
print(df_team_updated.head())
print(df_team_updated.shape)

#taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))
