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
df_team_updated = df_team.merge(df2,left_on="full_name",right_on="nameTeam",how="left",)
print(df_team_updated.head())
print(df_team_updated.shape)


#update to fix up errors
df_team_updated=df_team_updated.fillna(0)
print(df_team_updated.head(31))
print(df_team_updated.shape)

# player info on number 1 pick
print(df1.head())
print(df1.columns)

rs=con.execute(("Select * from Player_Attributes"))
df_Player_Attributes = pd.DataFrame(rs.fetchall())
df_Player_Attributes.columns=rs.keys()
print(df_Player_Attributes.head())
print(df_Player_Attributes.columns)


df_Num1_Player_Info=pd.concat([df_Player_Attributes,df1],keys=["ID", "idPlayer"])
#df_Num1_Player_Info=df1.merge(df_Player_Attributes,left_on="idPlayer", right_on="ID", how ="left")
print(df_Num1_Player_Info.head())
print(df_Num1_Player_Info.columns)
print(df_Num1_Player_Info.shape)

#picks=df_Num1_Player_Info["DRAFT_NUMBER"].unique()
print(df_Num1_Player_Info.iloc[2,:])#good
#print(df_Num1_Player_Info.loc[12,'DRAFT_NUMBER'])
draft_number_index = df_Num1_Player_Info.columns.get_loc('DRAFT_NUMBER')
print(draft_number_index)
print(df_Num1_Player_Info.index)
print(df_Player_Attributes.index)

i=0
# print(df_Num1_Player_Info.iloc[i,draft_number_index])
# for index,row in df_Num1_Player_Info.iterrows():
#     i=i+1
#     if int(df_Num1_Player_Info.iloc[i,draft_number_index])=='None':
#         print("Hi")
#     elif int(df_Num1_Player_Info.iloc[i, draft_number_index]) <11:
#         print(i)
#     else:
#         print("do nothing")

df_Player_Attributes = df_Player_Attributes[df_Player_Attributes["DRAFT_NUMBER"]!="None"]
print(df_Player_Attributes.shape)
print(df_Player_Attributes.head())
draft_number_index = df_Player_Attributes.columns.get_loc('DRAFT_NUMBER')
print(draft_number_index)

for index, row in df_Player_Attributes.iterrows():
    if int(df_Player_Attributes.iloc[row,draft_number_index])<11:
        df_Top_Ten_Pick=df_Top_Ten_Pick+df_Player_Attributes.iloc[row,31]

#df_top_ten = df_Player_Attributes[int(df_Player_Attributes["DRAFT_NUMBER"])<=10]
print(df_top_ten.head())
print(df+df_top_ten.shape)
#print(df_top_ten.head())