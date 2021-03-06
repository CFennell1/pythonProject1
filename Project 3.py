import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df_Player_Info = pd.read_csv("df_Active_Players.csv",)
print(df_Player_Info.head())

Not_drafted = ["None","Undrafted"]
df_Player_Info_Drafted = df_Player_Info[~df_Player_Info["DRAFT_NUMBER"].str.contains('|'.join(Not_drafted))]

print(df_Player_Info_Drafted.head())
print(df_Player_Info_Drafted.shape)


df_Player_Info_Top5 = df_Player_Info_Drafted[df_Player_Info_Drafted["DRAFT_NUMBER"].astype(int)<=5]
df_Player_Info_Top5.sort_values(by=["DRAFT_NUMBER"])

print(df_Player_Info_Top5.head())
print(df_Player_Info_Top5.shape)
draft_pick_order =[]
for i in range(5):
    draft_pick_order = draft_pick_order+[""+str(i+1)+""]

print(draft_pick_order)
sns.catplot(kind="box",x="DRAFT_NUMBER", y="PTS", data=df_Player_Info_Top5,order = draft_pick_order)
plt.ylim(0,40)
plt.show()
#hue="location",hue_order=("Rural","Urban"))

df_Player_Info_Top5['PTS'].plot.hist()
plt.show()
sns.distplot(df_Player_Info_Top5['PTS'],
             kde=False,
             bins=20)

sns.distplot(df_Player_Info_Top5['PTS'],
             hist=False,
             rug=True,
             kde_kws={'shade':True})

# Plot the results
plt.show()

###########################





sns.set(style='darkgrid')

df_Player_Info_Top5["Combined_PTS_AST_REB"] = df_Player_Info_Top5["PTS"]+df_Player_Info_Top5["AST"]+df_Player_Info_Top5["REB"]
print(df_Player_Info_Top5["Combined_PTS_AST_REB"].head())

df_Player_Info_Top5['Combined_PTS_AST_REB'].plot.hist()
plt.show()

#plt.ylim(0,50)
sns.catplot(kind="box",x="DRAFT_NUMBER", y="Combined_PTS_AST_REB", data=df_Player_Info_Top5,order = draft_pick_order)
plt.show()

#sns.countplot(x="SCHOOL", data=df_Player_Info_Top5, palette="Greens_d")
#sns.catplot(kind="count", y="SCHOOL", data=df_Player_Info_Top5, palette="Greens_d")
g = sns.catplot(kind="count", x="SCHOOL", data=df_Player_Info_Top5,order=df_Player_Info_Top5["SCHOOL"].value_counts().index,palette=["#39A7D0","#36ADA4"])
g.set_xticklabels(rotation =90)
plt.title("Number of Top 5 Draft Picks per School")
plt.tight_layout()
plt.show()