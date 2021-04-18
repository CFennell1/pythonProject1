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

df1 = df[df["numberPickOverall"]==1]

#df1=df(numerPickOverall ==1)
print(df1.head())
print(df1.shape)
print(df1["namePlayer"])
print(df1['nameTeam'])

num1_by_team = df1.groupby("nameTeam")["numberPickOverall"].sum()
print(num1_by_team)

#merge this to the teams