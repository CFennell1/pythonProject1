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

#Print out the teams that have never had the number 1 pick
print ("The teams that never had the number 1 pick are as follows:")
for i, row in df_Team_Updated.iterrows():
    if row["numberPickOverall"]==0:
        print(row["full_name"])


##############################################################################
# Now we will look at some player attributes
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Player_Attributes")
    df_All_Player_Data = pd.DataFrame(rs.fetchall())
    df_All_Player_Data.columns = rs.keys()


# Create columns to show the height and weight of players in metric format
df_All_Player_Data["HEIGHT_m"] = df_All_Player_Data["HEIGHT"] * 0.0254
df_All_Player_Data["WEIGHT_kg"] = df_All_Player_Data["WEIGHT"] * 0.454

# Create a function to calculate BMI
def bmi(w, h):
    return w / h ** 2

# Use the BMI function to add in a BMI column to the dataframe
df_All_Player_Data["BMI"] = bmi(df_All_Player_Data["WEIGHT_kg"], df_All_Player_Data["HEIGHT_m"])


#Use numpy to calculate summary stats for height, weight and BMI for all players all time
df_Summary_Height_Data = df_All_Player_Data["HEIGHT_m"].agg([np.min, np.max, np.mean, np.median])
df_Summary_Weight_Data = df_All_Player_Data["WEIGHT_kg"].agg([np.min, np.max, np.mean, np.median])
df_Summary_BMI = df_All_Player_Data["BMI"].agg([np.min, np.max, np.mean, np.median])

print(df_Summary_Height_Data)
print(df_Summary_Weight_Data)
print(df_Summary_BMI)

#Let us look at height per position
print(df_All_Player_Data.shape)

# Remove player data with no position value
df_All_Player_Data = df_All_Player_Data[df_All_Player_Data.POSITION !=""]

# Remove player data with no height value
df_All_Player_Data = df_All_Player_Data[df_All_Player_Data.HEIGHT_m.notnull()]

print(df_All_Player_Data.shape)

df_Position_Data = df_All_Player_Data.groupby("POSITION")["HEIGHT_m"].agg([np.min, np.max, np.mean, np.median])


print(df_Position_Data)

# Consider currently active players
df_Active_Players = df_All_Player_Data[df_All_Player_Data["ROSTERSTATUS"] == "Active"]

print(df_Active_Players.shape)
# Height per position for active players
df_Active_Position_Data = df_Active_Players.groupby("POSITION")["HEIGHT_m"].agg([np.min, np.max, np.mean, np.median])
print(df_Active_Position_Data)

fig = plt.figure()

ax = fig.add_subplot()
ax2 = ax.twinx()

width = 0.4

df_Position_Data.plot(kind='bar', y="mean", color='orange', ax=ax, width=width, position=1)
df_Active_Position_Data.plot(kind='bar', y="mean", color='green', ax=ax2, width=width, position=0)

ax.set(ylim=[1.80,2.15])
ax2.set(ylim=[1.80,2.15])
ax.set(title = "Average Height per Position Historical vs Current Players")
ax.set_ylabel('Historical Players Avg Height')
ax2.set_ylabel('Current Players Avg Height')
ax.legend(["Historical"], loc="upper center")
ax2.legend(["Current"], loc = "upper right")
fig.tight_layout()
plt.show()

# Look to see who is the tallest and shortest current NBA players
# Initial values that will get updated
max_height = 0.00
min_height = 3.00
max_height_row_range = 0
min_height_row_range = 0

height_col = df_Active_Players.columns.get_loc("HEIGHT_m")


for i in range(0, df_Active_Players.shape[0]):

    if df_Active_Players.iloc[i, height_col] > max_height:
        max_height_row_range = i
        max_height = df_Active_Players.iloc[i, height_col]

    if df_Active_Players.iloc[i, height_col] < min_height:
        min_height_row_range = i
        min_height = df_Active_Players.iloc[i, height_col]


max_height = max_height.round(2)
min_height = min_height.round(2)

first_name = df_Active_Players.iloc[max_height_row_range, df_Active_Players.columns.get_loc("FIRST_NAME")]
last_name = df_Active_Players.iloc[max_height_row_range, df_Active_Players.columns.get_loc("LAST_NAME")]
team_city = df_Active_Players.iloc[max_height_row_range, df_Active_Players.columns.get_loc("TEAM_CITY")]
team_name = df_Active_Players.iloc[max_height_row_range, df_Active_Players.columns.get_loc("TEAM_NAME")]

print("The tallest player in the NBA is " + str(first_name) + " " + str(last_name) + " who plays for the " + str(
     team_city) + " " + str(team_name) + ". He is " + str(max_height) + " metres in height.")

first_name = df_Active_Players.iloc[min_height_row_range, df_Active_Players.columns.get_loc("FIRST_NAME")]
last_name = df_Active_Players.iloc[min_height_row_range, df_Active_Players.columns.get_loc("LAST_NAME")]
team_city = df_Active_Players.iloc[min_height_row_range, df_Active_Players.columns.get_loc("TEAM_CITY")]
team_name = df_Active_Players.iloc[min_height_row_range, df_Active_Players.columns.get_loc("TEAM_NAME")]

print("The shortest player in the NBA is " + str(first_name) + " " + str(last_name) + " who plays for the " + str(
     team_city) + " " + str(team_name) + ". He is " + str(min_height) + " metres in height.")


# Save the active players dataframe to a csv file
df_Active_Players.to_csv(r'C:\Users\colin.fennell\Documents\df_Active_Players.csv')


# Read back in the csv and call it Player_Info
df_Player_Info = pd.read_csv("df_Active_Players.csv",)
print(df_Player_Info.head())

# Remove players that were not drafted
Not_drafted = ["None","Undrafted"]
df_Player_Info_Drafted = df_Player_Info[~df_Player_Info["DRAFT_NUMBER"].str.contains('|'.join(Not_drafted))]

print(df_Player_Info_Drafted.shape)

# Consider players that were drafted in the top 5
df_Player_Info_Top5 = df_Player_Info_Drafted[df_Player_Info_Drafted["DRAFT_NUMBER"].astype(int)<=5]


print(df_Player_Info_Top5.shape)
print(df_Player_Info_Top5.head())

sns.set_style("darkgrid")

# See which school has the most top 5 draft picks
g = sns.catplot(kind="count", x="SCHOOL", data=df_Player_Info_Top5,order=df_Player_Info_Top5["SCHOOL"].value_counts().index,palette=["#39A7D0","#36ADA4"])
g.set_xticklabels(rotation =90)
plt.title("Number of Top 5 Draft Picks per School")
plt.tight_layout()
plt.show()

# Prepare a list to use when for ordering when producing graphs
draft_pick_order =[]
for i in range(5):
    draft_pick_order = draft_pick_order+[""+str(i+1)+""]



# box plot to look at points for the top 5 draft picks

sns.catplot(kind="box",x="DRAFT_NUMBER", y="PTS", data=df_Player_Info_Top5,order = draft_pick_order, whis=[0, 100])
plt.ylim(0,35)
plt.ylabel("Points")
plt.title("Average Points per Game")
plt.show()


# Consider points, assists and rebounds added together
df_Player_Info_Top5["Combined_PTS_AST_REB"] = df_Player_Info_Top5["PTS"] + df_Player_Info_Top5["AST"] + df_Player_Info_Top5["REB"]


sns.catplot(kind="box",x="DRAFT_NUMBER", y="Combined_PTS_AST_REB", data=df_Player_Info_Top5,order = draft_pick_order, whis=[0, 100])
plt.ylim(0,50)
plt.title("Combined Average Points, Rebounds and Assists per Game")
plt.ylabel("Points + Rebounds + Assists")
plt.show()

df_Player_Info_Top5["DRAFT_NUMBER"]=pd.to_numeric((df_Player_Info_Top5["DRAFT_NUMBER"]))

sns.relplot(y="SCHOOL", x="PTS",
            data=df_Player_Info_Top5, kind="scatter",
            ci=None,
            hue="DRAFT_NUMBER",markers=True, dashes = False, palette=sns.color_palette("coolwarm",n_colors=5))
plt.title("Average Number of Points per Game per School/College" )
plt.xlabel("Points per Game")
plt.show()
