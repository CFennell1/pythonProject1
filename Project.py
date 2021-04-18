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
con.close()
print(df.head())
print(df.shape)
print(df.columns)

# Get the total number of avocados sold of each size
#nb_sold_by_size=avocados.groupby("size")["nb_sold"].sum()

#df1 = df[df["numberPickOverall"]==1]
df1 = df[df["yearDraft">1969] and df["numberPickOverall"==1]]

#df1=df(numerPickOverall ==1)
print(df1.head())
print(df1.shape)
print(df1["namePlayer"])
print(df1['nameTeam'])

#df2= df1.groupby("nameTeam")["numberPickOverall"].sum()
df2= df1.groupby("nameTeam")["numberPickOverall"].sum()

#num1_by_team = num1_by_team.sort_values("numberPickOverall",ascending = False)
print(df2)


import matplotlib.pyplot as plt

df2.plot(x="team",kind="bar", title="Number 1 picks by Team")
plt.show()

#vocados.plot(x="nb_sold", y ="avg_price", kind = "scatter", title="Number of avocados sold vs. average price")


# Plot a bar-chart of gold medals as a function of country
#ax.bar(num1_by_team["nameTeam"])

# Set the x-axis tick labels to the country names
#ax.set_xticklabels(medals.index, rotation = 90)

# Set the y-axis label
#ax.set_ylabel("Number of medals")

#plt.show()


#merge this to the teams